from llm.client import rewrite_query
class QueryRewriter:
    def __init__(self):
        pass

    def rewrite(
        self,
        question: str,
        conversation: list,
        active_product: str
    ) -> str:
        history = self._format_conversation(conversation)
        if not history:
            history = "No previous conversation."

        product_name = (
            active_product.replace("_", " ").title()
            if active_product
            else "Unknown"
        )

        prompt = f"""
            You are a query rewriting assistant.
            
            Rewrite the user's latest question into a complete standalone question.
            
            Rules:
            - Preserve the user's intent.
            - Use the conversation history only when necessary.
            - Do NOT answer the question.
            - Do NOT add extra information.
            - Return ONLY the rewritten question.
            
            Current Active Product:
            {product_name}
            
            Conversation:
            {history}
            
            Current User Question:
            {question}
            """

        rewritten_question = rewrite_query(prompt)
        return rewritten_question.strip()

    def _format_conversation(self, conversation):
        history = []

        for msg in conversation:
            role = msg["role"].upper()
            history.append(f"{role}: {msg['content']}")

        return "\n".join(history)