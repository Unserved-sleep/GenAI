from models.response_models import InsuranceResponse

class OutputGuardrail:
    @staticmethod
    def validate(response: InsuranceResponse):
        if not response.answer.strip():
            return (
                False,
                "The assistant generated an empty response."
            )
        if not (0.0 <= response.confidence <= 1.0):
            return (
                False,
                "Invalid confidence score."
            )
        return True, ""