from sentence_transformers import SentenceTransformer

# Load a pre-trained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Health insurance covers hospitalization.",
    "Medical insurance pays hospital expenses.",
    "Cats love drinking milk."
]

embeddings = model.encode(sentences)

print("Embedding Shape:", embeddings.shape)

print("\nFirst 10 values of the first embedding:")
print(embeddings[0][:10])