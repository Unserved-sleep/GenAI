from services.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "What is the waiting period for pre-existing diseases?"
)

print(results)