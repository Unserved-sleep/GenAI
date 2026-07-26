from vector_db.chunk import Chunk

class TextChunker:
    def __init__(self, chunk_size=300, overlap=50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_documents(self, documents):
        chunks = []

        for document in documents:
            text = document.text
            start = 0
            chunk_number = 1

            while start < len(text):
                end = start + self.chunk_size
                chunk_text = text[start:end]
                chunk = Chunk(
                    id=f"{document.id}_chunk_{chunk_number}",
                    text=chunk_text,
                    metadata={
                        **document.metadata,
                        "document_id": document.id,
                        "chunk_number": chunk_number
                    }
                )
                chunks.append(chunk)

                start += self.chunk_size - self.overlap
                chunk_number += 1
        return chunks