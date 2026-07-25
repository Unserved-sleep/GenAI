from pydantic import BaseModel
from imp_json import *
import json

class InsuranceResponse(BaseModel):
    answer: str
    confidence: str
    source: str


data = json.loads(response)
validated = InsuranceResponse(**data)