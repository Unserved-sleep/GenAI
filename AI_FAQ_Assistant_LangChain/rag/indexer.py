from rag.vectorstore import load_vectorstore
from rag.retriever import create_retriever

def build_index():

    vectorstore = load_vectorstore()

    retriever = create_retriever(vectorstore)

    return vectorstore, retriever