from langchain_core.vectorstores import VectorStoreRetriever

def create_retriever(
    vectorstore,
    k=4,
):
    """
    Create a retriever from the vector store.
    """
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": k,
            "fetch_k": 10
        }
    )
    return retriever