from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Health insurance covers hospitalization.",
    "Medical insurance pays hospital expenses.",
    "Cats love drinking milk."
]

query = "How do I claim hospital insurance?"

# Generate embeddings
sentence_embeddings = model.encode(sentences)
query_embedding = model.encode([query])

# Compute cosine similarity
scores = cosine_similarity(query_embedding, sentence_embeddings)[0]

# Print results
for sentence, score in zip(sentences, scores):
    print(f"{score:.4f}  ->  {sentence}")