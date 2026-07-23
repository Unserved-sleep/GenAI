from llm.providers._groq import client
from config.settings import settings


def generate_response(messages):

    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=messages,
        temperature=settings.TEMPERATURE,
        max_tokens=settings.MAX_TOKENS
    )

    return response.choices[0].message.content