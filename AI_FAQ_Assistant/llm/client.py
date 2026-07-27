import json

from llm.providers._groq import client
from config.settings import settings
from models.response_models import InsuranceResponse


def generate_response(messages):

    if settings.DEBUG:
        print("=" * 50)
        print("===== Conversation Sent to LLM =====")

        for message in messages:
            print(f"{message['role'].upper()}: {message['content']}")

        print("=" * 50)

    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=messages,
        temperature=settings.TEMPERATURE,
        max_tokens=settings.MAX_TOKENS
    )

    response_text = response.choices[0].message.content
    response_dict = json.loads(response_text)

    return InsuranceResponse.model_validate(response_dict)