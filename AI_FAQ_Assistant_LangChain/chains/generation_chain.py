from llm.chat_model import llm, structured_llm
from prompts.rag_prompt import rag_prompt

def create_generation_chain():
    generation_chain = (
            rag_prompt
            | structured_llm
    )

    return generation_chain