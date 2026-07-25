documents = [
    {
        "id": "doc1",
        "text": "Health insurance covers hospitalization.",
        "embedding": [0.21, -0.44, 0.91],
        "metadata": {
            "product": "Health",
            "page": 12
        }
    },
    {
        "id": "doc2",
        "text": "Motor insurance covers accidents.",
        "embedding": [-0.18, 0.62, 0.35],
        "metadata": {
            "product": "Motor",
            "page": 8
        }
    }
]

for doc in documents:
    print(f"ID: {doc['id']}")
    print(f"Text: {doc['text']}")
    print(f"Metadata: {doc['metadata']}")
    print("-" * 40)