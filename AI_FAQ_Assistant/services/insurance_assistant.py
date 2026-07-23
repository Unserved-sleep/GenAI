"""
Insurance Assistant Service

Main entry point for interacting with the AI assistant.
"""

from knowledge.knowledge_base import KnowledgeBase
from llm.client import generate_response
from llm.context_builder import ContextBuilder
from memory.manager import MemoryManager
from memory.models import InsuranceType, ResponseLength
from memory.conversation import ConversationManager

class InsuranceAssistant:

    def __init__(self):
        self.memory = MemoryManager()
        self.knowledge = KnowledgeBase()
        self.conversation = ConversationManager(self.memory)

        self.builder = ContextBuilder(
            self.memory,
            self.knowledge,
        )

        # Default preferences
        self.memory.set_active_product(
            InsuranceType.HEALTH
        )

        self.memory.set_response_preference(
            ResponseLength.DETAILED
        )

    def ask(
        self,
        question: str,
    ) -> str:
        # Save user message
        self.conversation.add_user_message(question)
        messages = self.builder.build(question)
        response = generate_response(messages)

        # Save assistant response
        self.conversation.add_assistant_message(response)
        return response