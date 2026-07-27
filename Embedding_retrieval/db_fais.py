import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Health insurance covers hospitalization.",
    "Motor insurance covers accidents.",
    "Travel insurance covers trip cancellation.",
    "Cashless treatment is available."
]

# Generate embeddings
embeddings = model.encode(documents)

# Convert to float32 (required by FAISS)
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add vectors
index.add(embeddings)

# Query
query = "Hospital treatment claim"
query_embedding = model.encode([query]).astype("float32")

# Search Top 2
distances, indices = index.search(query_embedding, k=2)

print("Top Results:\n")

for idx in indices[0]:
    print(documents[idx])