from config.settings import settings
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

        query_embedding = self.embedding_service.embed_text(
            query
        )

        results = self.store.search(
            query_embedding,
            top_k,
        )

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        retrieved_chunks = []

        if settings.DEBUG:
            print("\n========== Retrieval ==========")

        for text, metadata, distance in zip(
            documents,
            metadatas,
            distances,
        ):

            if distance <= settings.MAX_RETRIEVAL_DISTANCE:
                retrieved_chunks.append(
                    {
                        "text": text,
                        "metadata": metadata,
                        "distance": distance,
                    }
                )
                if settings.DEBUG:
                    print(
                        f"✓ {metadata['document_id']} "
                        f"(distance={distance:.3f})"
                    )

            else:
                if settings.DEBUG:
                    print(
                        f"✗ Filtered "
                        f"{metadata['document_id']} "
                        f"(distance={distance:.3f})"
                    )

        if settings.DEBUG:
            print("===============================\n")
        return retrieved_chunks