from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a helpful insurance assistant.

            Answer clearly.

            If you don't know the answer,
            say you don't know.
            """
        ),
        (
            "human",
            "{question}"
        ),
    ]
)