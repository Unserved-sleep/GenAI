"""
LLM-based Memory Updater

Updates the session memory based on the current conversation.
"""

from llm.client import classify_active_product


class MemoryUpdater:

    def update(
        self,
        question: str,
        conversation: list,
    ) -> str:

        prompt = f"""
You are an insurance session manager.

Determine which insurance product the user is currently discussing.

Possible outputs:

HEALTH
MOTOR
TRAVEL
UNCHANGED

Rules:
- If the user changes topics, return the new product.
- If the user continues discussing the same product, return UNCHANGED.
- Use the conversation history when needed.
- Return ONLY one word.

Conversation:

{self._format_conversation(conversation)}

Current Question:

{question}
"""

        return classify_active_product(prompt)

    def _format_conversation(
        self,
        conversation,
    ):

        if not conversation:
            return "No previous conversation."

        lines = []

        for msg in conversation:

            role = msg["role"].upper()

            lines.append(
                f"{role}: {msg['content']}"
            )

        return "\n".join(lines)