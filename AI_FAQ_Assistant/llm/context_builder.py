"""
Context Builder

Combines all available context before sending it to the LLM.
"""
from textwrap import dedent

from config.prompts import SYSTEM_PROMPT
from memory.manager import MemoryManager
from memory.conversation import ConversationManager

class ContextBuilder:
    def __init__(
        self,
        memory_manager: MemoryManager,
        conversation_manager: ConversationManager,
    ):
        self.memory_manager = memory_manager
        self.conversation_manager = conversation_manager

    def _format_knowledge(self, retrieved_chunks):
        if not retrieved_chunks:
            return "No relevant knowledge found."

        context = "Relevant Insurance Knowledge:\n\n"
        for chunk in retrieved_chunks:
            context += chunk["text"]
            context += "\n\n"

        return context

    def build(
            self,
            question: str,
            retrieved_chunks: list[dict],
    ) -> list[dict]:

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
                "content": self._format_conversation(),
            },
            {
                "role": "system",
                "content": self._format_knowledge(retrieved_chunks),
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

    def _format_conversation(self) -> str:
        messages = self.conversation_manager.get_messages()
        if not messages:
            return "Conversation History:\nNone"

        history = "Conversation History:\n\n"

        # Last 6 messages
        for message in messages[-6:]:
            history += (
                f"{message['role'].upper()}: "
                f"{message['content']}\n"
            )

        return history


