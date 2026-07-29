from typing import TypedDict
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage

class GraphState(TypedDict):
    question: str
    rewritten_question: str
    context: str
    documents: list[Document]
    scores: list[float]
    answer: str
    retry_count: int
    chat_history: list[BaseMessage]
    active_product: str | None
    guardrail_triggered: bool
    guardrail_message: str | None