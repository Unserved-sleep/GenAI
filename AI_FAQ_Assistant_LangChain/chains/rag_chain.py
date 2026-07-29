from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from llm.chat_model import llm
from prompts.rag_prompt import rag_prompt
from utils.document_formatter import format_documents


def create_rag_chain(retriever):

    chain = (
        {
            "context": itemgetter("question")
                       | retriever
                       | RunnableLambda(format_documents),

            "question": itemgetter("question"),
        }
        | rag_prompt
        | llm
        | StrOutputParser()
    )

    return chain