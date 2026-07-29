from rag.loader import load_documents
from rag.splitter import split_documents
from rag.vectorstore import create_vectorstore

documents = load_documents()

chunks = split_documents(documents)
print("Chunks created:", len(chunks))
for chunk in chunks:

    source = chunk.metadata["source"]

    if "health" in source.lower():
        chunk.metadata["product"] = "health"

    elif "travel" in source.lower():
        chunk.metadata["product"] = "travel"

    elif "motor" in source.lower():
        chunk.metadata["product"] = "motor"

vectorstore = create_vectorstore(chunks)

print("Collection count:", vectorstore._collection.count())
print("Index built successfully!")