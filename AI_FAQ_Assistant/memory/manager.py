"""
Memory Manager

Handles all updates to the conversation memory.
"""

from memory.models import (
    ConversationMemory,
    InsuranceType,
    ResponseLength,
)

class MemoryManager:
    def __init__(self):
        self.memory = ConversationMemory()

    def get_memory(self) -> ConversationMemory:
        return self.memory

    def reset(self):
        self.memory = ConversationMemory()

    def set_active_product(
        self,
        product: InsuranceType,
    ):
        self.memory.user.active_product = product

    def set_policy_number(
        self,
        policy_number: str,
    ):
        self.memory.user.policy_number = policy_number

    def set_response_preference(
        self,
        preference: ResponseLength,
    ):
        self.memory.preferences.response_length = preference

    def get_active_product(self):
        return self.memory.user.active_product