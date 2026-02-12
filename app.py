import streamlit as st

st.set_page_config(page_title="CodeGuru", layout="wide")

st.title("🧠 CodeGuru – AI Interview Preparation")
st.write("Upload your resume and prepare for HR & Technical interviews")

language = st.selectbox(
    "Choose Language",
    ["English", "Hindi", "Hinglish"]
)

mode = st.radio(
    "Interview Mode",
    ["HR Interview", "Technical Interview", "Mock Interview"]
)

uploaded_resume = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

from utils import extract_text_from_pdf

if uploaded_resume:
    st.success("✅ Resume uploaded successfully!")

    if st.button("Extract Resume Text"):
        resume_text = extract_text_from_pdf(uploaded_resume)

        st.write("### Extracted Resume Text Preview:")
        st.write(resume_text[:1000])  


user_query = st.text_input("Ask your interview question")

if st.button("Submit"):
    st.info("AI response will be implemented in the next version.")
