"""
Insurance Assistant Service

Main entry point for interacting with the AI assistant.
"""
from llm.query_rewriter import QueryRewriter
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
from llm.memory_updater import MemoryUpdater
from llm.multi_query_generator import MultiQueryGenerator



class InsuranceAssistant:

    def __init__(self):
        self.memory = MemoryManager()
        self.retriever = Retriever()
        self.multi_query_generator = MultiQueryGenerator()
        self.query_rewriter = QueryRewriter()
        self.memory_updater = MemoryUpdater()
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

        conversation = self.conversation.get_messages()

        active_product = self.memory_updater.update(
            question,
            conversation,
        )

        if active_product == "HEALTH":
            self.memory.set_active_product(
                InsuranceType.HEALTH
            )

        elif active_product == "MOTOR":
            self.memory.set_active_product(
                InsuranceType.MOTOR
            )

        elif active_product == "TRAVEL":
            self.memory.set_active_product(
                InsuranceType.TRAVEL
            )
        current_product = self.memory.get_active_product().value

        if settings.DEBUG:
            print(f"Detected Product : {active_product}")
            print(f"Current Product : {current_product}")

        # 2. Save user message
        self.conversation.add_user_message(question)
        conversation = self.conversation.get_messages()
        # 3. Retrieve context

        rewritten_question = self.query_rewriter.rewrite(
            question,
            conversation,
            current_product
        )
        search_queries = self.multi_query_generator.generate(
            rewritten_question
        )
        search_queries = list(dict.fromkeys(search_queries))
        
        if settings.DEBUG:
            print("\n===== Search Queries =====")

            for q in search_queries:
                print(q)

        # Step 2: Retrieve using the rewritten question
        retrieved_chunks = []

        for query in search_queries:
            chunks = self.retriever.retrieve(query)
            retrieved_chunks.extend(chunks)

        # Remove duplicate chunks
        unique_chunks = []
        seen = set()

        for chunk in retrieved_chunks:
            metadata = chunk["metadata"]

            key = (
                metadata["document_id"],
                metadata["chunk_number"]
            )

            if key not in seen:
                seen.add(key)
                unique_chunks.append(chunk)

        retrieved_chunks = unique_chunks

        if settings.DEBUG:
            print(f"\nOriginal Question : {question}")
            print(f"Rewritten Question: {rewritten_question}")

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