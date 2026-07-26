from knowledge.loader import DocumentLoader
from vector_db.chunker import TextChunker
from vector_db.embedding_service import EmbeddingService
from vector_db.chroma_store import ChromaStore


def initialize():
    loader = DocumentLoader()
    documents = loader.load_documents()

    print(f"Loaded {len(documents)} documents")
    chunker = TextChunker(
        chunk_size=300,
        overlap=50
    )
    chunks = chunker.chunk_documents(documents)
    print(f"Created {len(chunks)} chunks")

    embedding_service = EmbeddingService()
    embeddings = embedding_service.embed_texts(
        [chunk.text for chunk in chunks]
    )
    print("Generated embeddings")

    store = ChromaStore()
    store.reset()
    store.add_chunks(
        chunks,
        embeddings
    )
    print("Stored in ChromaDB")
    print("Vector Database Ready!")

if __name__ == "__main__":
    initialize()