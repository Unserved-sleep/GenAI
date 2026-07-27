from typing import Tuple

class InputGuardrail:
    INSURANCE_KEYWORDS = {
        "insurance",
        "policy",
        "premium",
        "claim",
        "coverage",
        "health",
        "motor",
        "travel",
        "life",
        "hospital",
        "accident",
        "renewal"
    }

    @staticmethod
    def validate(question: str, conversation=None):
        text = question.lower()

        # Include recent conversation
        if conversation:
            for msg in conversation[-4:]:
                text += " " + msg["content"].lower()

        if any(keyword in text for keyword in InputGuardrail.INSURANCE_KEYWORDS):
            return True, ""

        return False, "I can only answer insurance-related questions."