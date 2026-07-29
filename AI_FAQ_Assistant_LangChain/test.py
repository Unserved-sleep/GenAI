from graph.graph import build_graph
from rag.indexer import build_index

vectorstore, _ = build_index()
graph = build_graph(vectorstore)

config = {
    "configurable": {
        "thread_id": "demo-user"
    }
}

graph.invoke(
    {
        "question": "What is health insurance?"
    },
    config=config,
)

graph.invoke(
    {
        "question": "What are waiting periods?"
    },
    config=config,
)

state = graph.get_state(config)

print(state.values)