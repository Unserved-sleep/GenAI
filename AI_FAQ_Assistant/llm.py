from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME
from prompts import FAQ_PROMPT

client = Groq(api_key=GROQ_API_KEY)

def ask_llm(question: str):
    prompt = FAQ_PROMPT.format(
        question=question
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content