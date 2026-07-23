"""
Context Builder

Combines all available context before sending it to the LLM.
"""
from textwrap import dedent

from config.prompts import SYSTEM_PROMPT
from knowledge.knowledge_base import KnowledgeBase
from memory.manager import MemoryManager

class ContextBuilder:

    def __init__(
        self,
        memory_manager: MemoryManager,
        knowledge_base: KnowledgeBase,
    ):
        self.memory_manager = memory_manager
        self.knowledge_base = knowledge_base

    def _format_knowledge(self) -> str:
        knowledge = self.knowledge_base.get_context(
            "health",
            "renewal"
        )

        if knowledge is None:
            return "No relevant knowledge found."

        return dedent(f"""
        Relevant Knowledge

        {knowledge}
        """)

    def build(
        self,
        question: str,
    ) -> list[dict]:
        """
        Build the final messages list.
        """
        memory = self.memory_manager.get_memory()
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "system",
                "content": self._format_memory(),
            },
            {
                "role": "system",
                "content": self._format_knowledge(),
            },
            {
                "role": "user",
                "content": question,
            }
        ]
        return messages

    def _format_memory(self) -> str:
        memory = self.memory_manager.get_memory()

        return dedent(f"""
    Current User Context

    Active Product:
    {memory.user.active_product.value if memory.user.active_product else "Not Set"}

    Policy Number:
    {memory.user.policy_number}

    Preferred Response Length:
    {memory.preferences.response_length.value}

    Language:
    {memory.preferences.language}
    """)