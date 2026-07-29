from langchain_core.prompts import ChatPromptTemplate

rewrite_prompt = ChatPromptTemplate.from_template(
"""
You are an expert at rewriting search queries.

You are rewriting questions for semantic search over an insurance knowledge base.

Rewrite the question only if necessary.

Preserve the original meaning.

If the question depends on previous conversation,
make it self-contained.

Do not broaden the scope.

Return only the rewritten query.

Do not answer the question.

Only rewrite it.

Question:
{question}
"""
)