from sentence_transformers import CrossEncoder

# Load a reranker model
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

query = "How do I renew my health insurance?"

documents = [
    "Health insurance renewal is available online.",
    "Motor insurance covers accidental damage.",
    "Cashless hospitalization is available.",
    "Travel insurance protects against trip cancellation."
]

# Create query-document pairs
pairs = [[query, doc] for doc in documents]

# Get relevance scores
scores = reranker.predict(pairs)

# Sort by score
results = sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)

print("Reranked Results:\n")

for doc, score in results:
    print(f"{score:.4f} -> {doc}")