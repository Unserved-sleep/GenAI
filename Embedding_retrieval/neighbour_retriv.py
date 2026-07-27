from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Health insurance covers hospitalization.",
    "Medical insurance pays hospital expenses.",
    "Travel insurance covers trip cancellation.",
    "Motor insurance covers accidents.",
    "Cats love drinking milk."
]

# Generate embeddings
doc_embeddings = model.encode(documents)

query = "Hospital insurance claim"
query_embedding = model.encode([query])

# Exact search (compare with every document)
scores = cosine_similarity(query_embedding, doc_embeddings)[0]

# Get Top-3
top_k = 3
top_indices = np.argsort(scores)[::-1][:top_k]

print("Top Results:\n")

for idx in top_indices:
    print(f"Score: {scores[idx]:.4f}")
    print(f"Document: {documents[idx]}")
    print("-" * 40)