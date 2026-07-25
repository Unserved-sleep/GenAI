documents = [
    {
        "text": "Health insurance covers hospitalization.",
        "product": "Health",
        "topic": "Coverage",
        "page": 12,
        "source": "HealthPolicy.pdf"
    },
    {
        "text": "Motor insurance covers accidental damage.",
        "product": "Motor",
        "topic": "Coverage",
        "page": 8,
        "source": "MotorPolicy.pdf"
    },
    {
        "text": "Travel insurance covers trip cancellation.",
        "product": "Travel",
        "topic": "Benefits",
        "page": 5,
        "source": "TravelPolicy.pdf"
    }
]

for doc in documents:
    print("=" * 40)
    print("Text:", doc["text"])
    print("Source:", doc["source"])
    print("Page:", doc["page"])
    print("Product:", doc["product"])