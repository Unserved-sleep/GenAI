from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "llama-3.3-70b-versatile"
    )

    TEMPERATURE = 0.3
    MAX_TOKENS = 1024

    # Debug Mode
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"


settings = Settings()