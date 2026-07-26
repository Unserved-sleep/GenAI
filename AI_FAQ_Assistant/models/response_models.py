from pydantic import BaseModel
from typing import List

class Source(BaseModel):
    document: str
    chunk: int

class InsuranceResponse(BaseModel):
    answer: str
    confidence: float
    sources: List[Source]