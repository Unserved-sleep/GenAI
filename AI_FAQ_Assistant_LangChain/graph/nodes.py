from utils.document_formatter import format_documents
from langchain_core.messages import HumanMessage, AIMessage
from chains.rewrite_chain import rewrite_chain
from graph.guardrails import input_guardrail

def input_guardrail_node(state):
    blocked, message = input_guardrail(state["question"])

    return {
        "guardrail_triggered": blocked,
        "guardrail_message": message,
    }


def blocked_node(state):
    return {
        "answer": state["guardrail_message"],
        "documents": [],
        "scores": [],
    }


def retrieve_node(state, vectorstore):

    question = state.get("rewritten_question") or state["question"]

    product = state.get("active_product")

    if product:
        results = vectorstore.similarity_search_with_score(
            question,
            k=3,
            filter={"product": product}
        )
    else:
        results = vectorstore.similarity_search_with_score(
            question,
            k=3,
        )

    documents = [doc for doc, score in results]
    scores = [score for doc, score in results]

    context = format_documents(documents)

    for doc, score in results:
        print("=" * 60)
        print(f"Score: {score:.4f}")
        print(f"Source: {doc.metadata['source']}")

    print("Question:", question)
    print("Active Product:", product)
    print("Results:", len(results))

    return {
        "documents": documents,
        "scores": scores,
        "context": context,
    }


from chains.generation_chain import create_generation_chain
generation_chain = create_generation_chain()


def generate_node(state):

    response = generation_chain.invoke(
        {
            "context": state["context"],
            "question": state["question"],
            "chat_history": state.get("chat_history", []),
        }
    )

    history = state.get("chat_history", []).copy()

    history.append(
        HumanMessage(content=state["question"])
    )

    history.append(
        AIMessage(content=response.answer)
    )

    return {
        "answer": response.answer,
        "category": response.category,
        "confidence": response.confidence,
        "chat_history": history,
    }


def rewrite_node(state):
    rewritten = rewrite_chain.invoke(
        {
            "question": state["question"]
        }
    )

    retry_count = state.get("retry_count", 0)

    return {
        "rewritten_question": rewritten,
        "retry_count": retry_count + 1,
    }

def no_documents_node(state):
    return {
        "answer": "Sorry, I couldn't find relevant information in the knowledge base."
    }


def active_product_node(state):

    question = state["question"].lower()
    active_product = state.get("active_product")

    if "health" in question:
        active_product = "health"

    elif "motor" in question or "car" in question or "vehicle" in question:
        active_product = "motor"

    elif "travel" in question or "trip" in question:
        active_product = "travel"

    return {
        "active_product": active_product
    }