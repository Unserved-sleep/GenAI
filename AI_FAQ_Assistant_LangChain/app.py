import streamlit as st

from graph.graph import build_graph
from rag.indexer import build_index

# ---------------------------
# Load graph only once
# ---------------------------

@st.cache_resource
def load_graph():
    vectorstore, _ = build_index()
    return build_graph(vectorstore)

graph = load_graph()

# ---------------------------
# Session Initialization
# ---------------------------

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "demo-user"

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# UI
# ---------------------------

st.set_page_config(
    page_title="Insurance FAQ Assistant",
    page_icon="🤖",
)

st.title("🤖 Insurance FAQ Assistant")

st.write(
    "Ask questions about Health, Travel, and Motor Insurance."
)

# ---------------------------
# Display Chat History
# ---------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------
# User Input
# ---------------------------

question = st.chat_input("Ask your question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    config = {
        "configurable": {
            "thread_id": st.session_state.thread_id
        }
    }

    response = graph.invoke(
        {
            "question": question,
            "retry_count": 0,
        },
        config=config,
    )

    answer = response["answer"]

    with st.chat_message("assistant"):
        st.markdown(answer)

        if "category" in response:
            st.caption(f"Category: {response['category']}")

        if "confidence" in response:
            st.caption(f"Confidence: {response['confidence']:.2f}")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )


#streamlit run app.py