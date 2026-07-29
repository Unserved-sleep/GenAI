from rag.vectorstore import load_vectorstore

vs = load_vectorstore()

print(vs._collection.count())