import streamlit as st

st.title("🧠 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your Resume (PDF Only)", type=["pdf"])

if uploaded_file:
    st.success("Resume Uploaded Successfully ✅")
