from groq import Groq

from config.settings import settings


client = Groq(
    api_key=settings.GROQ_API_KEY
)