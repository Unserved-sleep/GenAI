import json

response = """
{
    "answer": "Yes, you can renew online.",
    "confidence": "high",
    "source": "knowledge_base"
}
"""

data = json.loads(response)

print(data)
print(data["answer"])
print(data["confidence"])