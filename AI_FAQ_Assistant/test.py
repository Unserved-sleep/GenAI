from services.insurance_assistant import InsuranceAssistant

assistant = InsuranceAssistant()

response = assistant.ask(
    "Can I renew it online?"
)

print(response)