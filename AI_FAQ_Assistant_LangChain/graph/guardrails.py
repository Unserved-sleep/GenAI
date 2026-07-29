
BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "system prompt",
    "reveal your prompt",
    "forget your instructions",
    "jailbreak",
]

def input_guardrail(question: str):
    question = question.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in question:
            return (
                True,
                "This request isn't allowed because it attempts to override the assistant's instructions."
            )

    return False, None