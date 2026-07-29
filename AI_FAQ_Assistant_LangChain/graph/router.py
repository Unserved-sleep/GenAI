def route_after_retrieval(state):

    best_score = min(state["scores"])

    THRESHOLD = 1.0

    if best_score < THRESHOLD:
        return "generate"

    retry_count = state.get("retry_count", 0)

    if retry_count == 0:
        return "rewrite"

    return "no_documents"

def guardrail_router(state):
    if state["guardrail_triggered"]:
        return "blocked"
    return "continue"