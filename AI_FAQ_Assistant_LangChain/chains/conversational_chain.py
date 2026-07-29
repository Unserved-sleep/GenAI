from langchain_core.runnables.history import RunnableWithMessageHistory

from chains.rag_chain import create_rag_chain
from memory.chat_history import get_session_history


def create_conversational_chain(retriever):

    rag_chain = create_rag_chain(retriever)

    conversational_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="question",
        history_messages_key="chat_history",
    )

    return conversational_chain