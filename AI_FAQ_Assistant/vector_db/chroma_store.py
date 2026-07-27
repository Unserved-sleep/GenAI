import chromadb


class ChromaStore:

    def __init__(
        self,
        db_path="vector_db/chroma_db",
        collection_name="insurance_documents",
    ):

        self.client = chromadb.PersistentClient(path=db_path)

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_chunks(
        self,
        chunks,
        embeddings,
    ):

        self.collection.add(

            ids=[
                chunk.id
                for chunk in chunks
            ],

            documents=[
                chunk.text
                for chunk in chunks
            ],

            embeddings=embeddings.tolist(),

            metadatas=[
                chunk.metadata
                for chunk in chunks
            ]
        )

    def search(
        self,
        query_embedding,
        top_k=3,
    ):

        return self.collection.query(

            query_embeddings=[
                query_embedding.tolist()
            ],

            n_results=top_k,

            include=[
                "documents",
                "metadatas",
                "distances",
            ]
        )

    def reset(self):

        self.client.delete_collection(
            "insurance_documents"
        )

        self.collection = self.client.create_collection(
            "insurance_documents"
        )