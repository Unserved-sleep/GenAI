from pydantic import BaseModel, Field

class InsuranceResponse(BaseModel):
    answer: str = Field(
        description="Answer to the user's question"
    )

    category: str = Field(
        description="Insurance category"
    )

    confidence: float = Field(
        description="Confidence score between 0 and 1"
    )