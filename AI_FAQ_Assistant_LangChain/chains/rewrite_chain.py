from langchain_core.output_parsers import StrOutputParser

from llm.chat_model import llm
from prompts.rewrite_prompt import rewrite_prompt


rewrite_chain = (
    rewrite_prompt
    | llm
    | StrOutputParser()
)