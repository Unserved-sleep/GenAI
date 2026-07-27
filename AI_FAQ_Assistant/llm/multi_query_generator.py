from llm.client import generate_multi_queries


class MultiQueryGenerator:

    def __init__(self):
        pass

    def generate(
        self,
        question: str,
    ) -> list[str]:

        prompt = f"""
                You are a search query generation assistant.
                
                Generate 3 different search queries for retrieving information from an insurance knowledge base.
                
                Rules:
                - Preserve the user's intent.
                - Use different wording.
                - Keep each query concise.
                - Do NOT answer the question.
                - Return ONLY the search queries.
                - Return one query per line.
                
                User Question:
                
                {question}
                """

        response = generate_multi_queries(prompt)

        queries = [
            line.strip()
            for line in response.splitlines()
            if line.strip()
        ]

        return queries