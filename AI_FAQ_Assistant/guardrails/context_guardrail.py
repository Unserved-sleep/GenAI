from typing import List, Tuple

class ContextGuardrail:
    @staticmethod
    def validate(retrieved_chunks: List) -> Tuple[bool, str]:
        if not retrieved_chunks:
            return (
                False,
                "The available knowledge does not contain that information."
            )
        return True, ""