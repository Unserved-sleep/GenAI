from langchain_chroma import Chroma
from rag.embeddings import get_embeddings


def create_vectorstore(
    chunks,
    persist_directory="chroma_db",
):

    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory,
    )

    return vectorstore


def load_vectorstore(
    persist_directory="chroma_db",
):

    embeddings = get_embeddings()

    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
    )