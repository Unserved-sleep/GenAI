from llm.multi_query_generator import MultiQueryGenerator

generator = MultiQueryGenerator()

queries = generator.generate(
    "What is cashless treatment?"
)

print(queries)