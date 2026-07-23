"""
Knowledge Base

Provides insurance knowledge for the assistant.
"""

from knowledge.insurance_data import INSURANCE_DATA


class KnowledgeBase:

    def __init__(self):
        self.data = INSURANCE_DATA

    def get_context(
        self,
        product: str,
        topic: str,
    ) -> str | None:

        product = product.lower()
        topic = topic.lower()

        if product not in self.data:
            return None

        return self.data[product].get(topic)