from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()

from graph.state import GraphState
from graph.nodes import (
    retrieve_node,
    generate_node, rewrite_node, no_documents_node, active_product_node, input_guardrail_node, blocked_node,
)
from graph.router import route_after_retrieval, guardrail_router


def build_graph(vectorstore):
    builder = StateGraph(GraphState)

    builder.add_node("input_guardrail", input_guardrail_node)
    builder.add_node("blocked", blocked_node)

    builder.add_node("active_product", active_product_node)

    builder.add_edge(START, "input_guardrail")

    builder.add_conditional_edges(
        "input_guardrail",
        guardrail_router,
        {
            "continue": "active_product",
            "blocked": "blocked",
        },
    )

    builder.add_edge("blocked", END)

    builder.add_edge("active_product", "retrieve")

    builder.add_node(
        "retrieve",
        lambda state: retrieve_node(state, vectorstore),
    )

    builder.add_node(
        "generate",
        generate_node,
    )

    builder.add_node(
        "rewrite",
        rewrite_node,
    )

    builder.add_node(
        "no_documents",
        no_documents_node,
    )


    builder.add_conditional_edges(
        "retrieve",
        route_after_retrieval,
        {
            "generate": "generate",
            "rewrite": "rewrite",
            "no_documents": "no_documents",
        },
    )

    builder.add_edge(
        "generate",
        END,
    )

    builder.add_edge(
        "rewrite",
        "retrieve",
    )

    graph = builder.compile(
        checkpointer=memory
    )
    return graph