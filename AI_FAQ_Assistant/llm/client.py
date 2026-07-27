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


def rewrite_query(prompt: str) -> str:

    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You rewrite conversational questions into standalone questions."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_tokens=150,
    )

    return response.choices[0].message.content.strip()

def classify_active_product(
    prompt: str,
) -> str:

    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
        max_tokens=10,
    )

    return response.choices[0].message.content.strip().upper()

def generate_multi_queries(
    prompt: str,
) -> str:

    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You generate multiple search queries for retrieving "
                    "information from an insurance knowledge base."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=150,
    )

    return response.choices[0].message.content.strip()