import streamlit as st
from services.insurance_assistant import InsuranceAssistant

st.set_page_config(
    page_title="AI Insurance Assistant",
    page_icon="🛡",
    layout="wide"
)

if "assistant" not in st.session_state:
    st.session_state.assistant = InsuranceAssistant()

assistant = st.session_state.assistant

st.title("🛡 Context-Aware Insurance Assistant")

question = st.text_input("Ask an insurance question")

if st.button("Send"):
    if question.strip():
        with st.spinner("Thinking..."):
            response = assistant.ask(question)

        st.markdown("### 🤖 Assistant")

        # Show only the answer
        st.markdown(response.answer)

        st.divider()

        # Confidence
        st.write(f"**Confidence:** {response.confidence:.2f}")

        # Sources
        st.write("**Sources:**")
        for source in response.sources:
            st.write(f"• {source.document} (Chunk {source.chunk})")