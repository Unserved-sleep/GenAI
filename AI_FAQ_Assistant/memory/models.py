"""
Memory Models

Defines the application's structured memory.
"""

from dataclasses import dataclass, field
from enum import Enum

class InsuranceType(Enum):
    HEALTH = "Health Insurance"
    MOTOR = "Motor Insurance"
    TRAVEL = "Travel Insurance"

class ResponseLength(Enum):
    SHORT = "short"
    MEDIUM = "medium"
    DETAILED = "detailed"

@dataclass
class UserPreferences:
    response_length: ResponseLength = ResponseLength.MEDIUM
    language: str = "English"

@dataclass
class UserContext:
    active_product: InsuranceType | None = None
    policy_number: str | None = None

@dataclass
class ConversationMemory:
    """
    Main application memory.
    """
    user: UserContext = field(default_factory=UserContext)
    preferences: UserPreferences = field(default_factory=UserPreferences)
    recent_messages: list[dict] = field(default_factory=list)
    conversation_summary: str = ""