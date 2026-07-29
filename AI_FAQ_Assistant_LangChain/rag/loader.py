from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
)

def load_documents(
    path: str = "knowledge",
    pattern: str = "*.txt",
):
    """
    Load all knowledge documents.
    """
    loader = DirectoryLoader(
        path,
        glob=pattern,
        loader_cls=TextLoader,
    )
    return loader.load()