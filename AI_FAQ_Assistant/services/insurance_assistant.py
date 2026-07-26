"""
Insurance Assistant Service

Main entry point for interacting with the AI assistant.
"""

from llm.client import generate_response
from llm.context_builder import ContextBuilder
from memory.manager import MemoryManager
from memory.models import InsuranceType, ResponseLength
from memory.conversation import ConversationManager
from services.retriever import Retriever
from models.response_models import Source
from models.response_models import InsuranceResponse


class InsuranceAssistant:

    def __init__(self):
        self.memory = MemoryManager()
        self.retriever = Retriever()
        self.conversation = ConversationManager(self.memory)

        self.builder = ContextBuilder(
            self.memory,
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
    ) -> InsuranceResponse:
        self.conversation.add_user_message(question)
        retrieved_chunks = self.retriever.retrieve(question)
        messages = self.builder.build(
            question,
            retrieved_chunks,
        )

        response = generate_response(messages)
        sources = []
        for chunk in retrieved_chunks:
            metadata = chunk["metadata"]
            sources.append(
                Source(
                    document=metadata["document_id"],
                    chunk=metadata["chunk_number"]
                )
            )

        response.sources = sources
        self.conversation.add_assistant_message(
            response.answer
        )
        return response