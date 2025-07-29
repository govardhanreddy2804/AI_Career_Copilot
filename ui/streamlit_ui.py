# ui/streamlit_ui.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from agents.resume_agent import analyze_resume_against_jd
from agents.learning_path_agent import generate_learning_plan
from agents.tools import extract_text_from_resume
from agents.cover_letter_agent import generate_cover_letter



st.set_page_config(page_title="AI Career Copilot", layout="wide")
st.title("🎯 AI Career Copilot")

resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
jd_text = st.text_area("Paste the Job Description")

if resume_file and jd_text:
    os.makedirs("data/resumes", exist_ok=True)
    file_path = f"data/resumes/{resume_file.name}"
    with open(file_path, "wb") as f:
        f.write(resume_file.read())

    with st.spinner("🔍 Extracting text from resume..."):
        resume_text = extract_text_from_resume(file_path)

    with st.spinner("🧠 Analyzing skill gaps..."):
        gaps = analyze_resume_against_jd(resume_text, jd_text)
    st.subheader("🧩 Skill Gap Analysis")
    st.write(gaps)

    with st.spinner("📚 Generating personalized learning plan..."):
        plan = generate_learning_plan(gaps)
    st.subheader("📘 30-Day Learning Plan")
    st.code(plan, language="markdown")

    with st.spinner("✍️ Generating cover letter..."):
        cover_letter = generate_cover_letter(resume_text, jd_text)

    st.subheader("📄 Suggested Cover Letter")
    st.code(cover_letter, language="markdown")

user_email = st.text_input("Enter your email to save your results (optional):")
