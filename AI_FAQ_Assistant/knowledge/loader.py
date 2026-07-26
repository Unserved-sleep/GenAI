from pathlib import Path
from knowledge.document import Document

class DocumentLoader:
    """
    Loads all text documents from the knowledge/documents folder.
    """
    def __init__(self, documents_path: str = "knowledge/documents"):
        self.documents_path = Path(documents_path)

    def load_documents(self):
        documents = []

        for file in self.documents_path.glob("*.txt"):
            with open(file, "r", encoding="utf-8") as f:
                text = f.read()

            document = Document(
                id=file.stem,
                text=text,
                metadata={
                    "source": file.name
                }
            )
            documents.append(document)
        return documents