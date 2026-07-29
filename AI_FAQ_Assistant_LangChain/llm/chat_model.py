from langchain_groq import ChatGroq
from config.settings import settings
from schemas.response_schema import InsuranceResponse



llm = ChatGroq(
    model=settings.MODEL_NAME,
    temperature=settings.TEMPERATURE,
    api_key=settings.GROQ_API_KEY,
)

structured_llm = llm.with_structured_output(
    InsuranceResponse
)