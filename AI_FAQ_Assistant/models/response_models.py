from pydantic import BaseModel
from typing import List

class Source(BaseModel):
    document: str
    chunk: int


from pydantic import BaseModel, Field

class InsuranceResponse(BaseModel):
    answer: str
    confidence: float
    sources: list[Source] = Field(default_factory=list)