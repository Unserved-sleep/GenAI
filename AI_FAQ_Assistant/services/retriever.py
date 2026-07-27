from vector_db.embedding_service import EmbeddingService
from vector_db.chroma_store import ChromaStore

class Retriever:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.store = ChromaStore()

    def retrieve(
            self,
            query: str,
            top_k: int = 3,
    ) -> list[dict]:
        query_embedding = self.embedding_service.embed_text(query)

        results = self.store.search(
            query_embedding,
            top_k
        )

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        return [
            {
                "text": text,
                "metadata": metadata
            }
            for text, metadata in zip(documents, metadatas)
        ]