"""
Conversation History

Stores recent conversation messages.
"""

from memory.manager import MemoryManager

class ConversationManager:
    def __init__(
        self,
        memory_manager: MemoryManager,
    ):
        self.memory_manager = memory_manager

    def add_user_message(
        self,
        message: str,
    ):
        self.memory_manager.memory.recent_messages.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_assistant_message(
        self,
        message: str,
    ):
        self.memory_manager.memory.recent_messages.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    def get_messages(self):
        return self.memory_manager.memory.recent_messages

    def clear(self):
        self.memory_manager.memory.recent_messages.clear()