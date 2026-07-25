keyword_scores = {
    "Doc1": 0.90,
    "Doc2": 0.40,
    "Doc3": 0.20
}

semantic_scores = {
    "Doc1": 0.70,
    "Doc2": 0.95,
    "Doc3": 0.10
}

print("Hybrid Scores:\n")

for doc in keyword_scores:
    final_score = (
        keyword_scores[doc] +
        semantic_scores[doc]
    ) / 2

    print(
        f"{doc}: {final_score:.2f}"
    )