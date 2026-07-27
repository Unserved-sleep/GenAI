"""
Insurance Assistant Service

Main entry point for interacting with the AI assistant.
"""
from guardrails.context_guardrail import ContextGuardrail
from guardrails.input_guardrail import InputGuardrail
from guardrails.output_guardrail import OutputGuardrail
from llm.client import generate_response
from llm.context_builder import ContextBuilder
from memory.manager import MemoryManager
from memory.models import InsuranceType, ResponseLength
from memory.conversation import ConversationManager
from services.retriever import Retriever
from models.response_models import Source
from models.response_models import InsuranceResponse
from config.settings import settings



class InsuranceAssistant:

    def __init__(self):
        self.memory = MemoryManager()
        self.retriever = Retriever()
        self.conversation = ConversationManager(self.memory)

        self.builder = ContextBuilder(
            self.memory,
            self.conversation,
        )

        # Default preferences
        self.memory.set_active_product(
            InsuranceType.HEALTH
        )

        self.memory.set_response_preference(
            ResponseLength.DETAILED
        )

    def _error_response(self, message: str) -> InsuranceResponse:
        response = InsuranceResponse(
            answer=message,
            confidence=0.0,
            sources=[]
        )
        self.conversation.add_assistant_message(response.answer)
        return response



    def ask(
            self,
            question: str,
    ) -> InsuranceResponse:

        # 1. Validate input
        conversation = self.conversation.get_messages()

        is_valid, message = InputGuardrail.validate(
            question,
            conversation
        )

        if settings.DEBUG:
            print("=" * 60)
            print("QUESTION:", repr(question))
            print("Input guardrail:", is_valid, message)
            print("=" * 60)


        if not is_valid:
            self.conversation.add_user_message(question)
            return self._error_response(message)


        # 2. Save user message
        self.conversation.add_user_message(question)

        # 3. Retrieve context
        retrieved_chunks = self.retriever.retrieve(question)

        # 4. Validate retrieved context
        is_valid, message = ContextGuardrail.validate(retrieved_chunks)
        if not is_valid:
            return self._error_response(message)

        # 5. Build prompt
        messages = self.builder.build(
            question,
            retrieved_chunks
        )

        # 6. Generate response
        if settings.DEBUG:
            print("Calling LLM...")
            print()
        response = generate_response(messages)

        is_valid, message = OutputGuardrail.validate(response)

        if not is_valid:
            return self._error_response(message)
        # 7. Attach sources
        seen = set()
        sources = []

        for chunk in retrieved_chunks:
            metadata = chunk["metadata"]

            key = (
                metadata["document_id"],
                metadata["chunk_number"]
            )

            if key not in seen:
                seen.add(key)
                sources.append(
                    Source(
                        document=metadata["document_id"],
                        chunk=metadata["chunk_number"]
                    )
                )
        response.sources = sources

        # 8. Save assistant response
        self.conversation.add_assistant_message(
            response.answer
        )
        return response