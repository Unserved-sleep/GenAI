import streamlit as st
from llm import ask_llm

st.set_page_config(
    page_title="AI FAQ Assistant",
    page_icon="🤖"
)

st.title("🤖 AI FAQ Assistant")
st.write(
    "Ask any insurance-related question."
)

question = st.text_area(
    "Your Question"
)

if st.button("Ask"):
    if question.strip():
        with st.spinner("Thinking..."):
            answer = ask_llm(question)

        st.success("Answer")
        st.write(answer)

    else:
        st.warning("Please enter a question.")