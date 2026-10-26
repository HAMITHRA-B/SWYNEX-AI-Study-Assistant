import os
import streamlit as st
from google import genai

st.set_page_config(page_title="AI Study Assistant", page_icon="📚", layout="centered")

def get_api_key():
    """Read the API key from Streamlit secrets first, then environment variables."""
    try:
        key = st.secrets.get("GEMINI_API_KEY", "")
        if key:
            return key
    except Exception:
        pass
    return os.getenv("GEMINI_API_KEY", "")

st.title("📚 AI Study Assistant")
st.write("Ask a study question and get a clear, student-friendly explanation powered by Google's Gemini API.")

with st.sidebar:
    st.header("Study settings")
    level = st.selectbox("Explanation level", ["Beginner", "Intermediate", "Advanced"])
    answer_style = st.selectbox("Answer style", ["Short explanation", "Step-by-step", "Bullet points", "Example-based"])
    st.caption("AI answers can make mistakes. Verify important facts with your course materials.")

question = st.text_area(
    "Enter your question",
    placeholder="Example: Explain machine learning with a real-life example.",
    height=120,
    max_chars=2000,
)

if st.button("Generate answer", type="primary", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        api_key = get_api_key()
        if not api_key:
            st.error("API key not found. Add GEMINI_API_KEY to .streamlit/secrets.toml or your environment variables.")
        else:
            try:
                client = genai.Client(api_key=api_key)
                prompt = f"""
You are a helpful AI Study Assistant for students.
Explain the answer at this level: {level}.
Use this answer style: {answer_style}.
Be accurate, clear, and student-friendly. Define important terms.
If the question is unclear, briefly ask for clarification.
Question: {question.strip()}
"""
                with st.spinner("Generating your study answer..."):
                    response = client.interactions.create(
                        model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
                        input=prompt,
                    )
                answer = getattr(response, "output_text", None)
                if answer:
                    st.subheader("Answer")
                    st.markdown(answer)
                    st.caption("Generated using the Gemini API.")
                else:
                    st.error("The API returned no text. Please try again.")
            except Exception as exc:
                st.error("The request failed. Check your internet connection, API key, API access, and model availability.")
                st.caption(f"Technical detail: {exc}")

st.divider()
st.caption("SWYNEX Internship · Task 2 · Model/API Integration")
