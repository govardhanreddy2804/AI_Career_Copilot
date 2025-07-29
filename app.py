# AI Career Copilot - Main Starter File

# app.py (Entry point)
import streamlit as st
from agents.resume_agent import analyze_resume_against_jd
from agents.learning_path_agent import generate_learning_plan
from agents.tools import extract_text_from_resume
import os

st.set_page_config(page_title="AI Career Copilot", layout="wide")
st.title("🎯 AI Career Copilot")

# Upload Resume
resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
# Paste JD
jd_input = st.text_area("Paste Job Description")

if resume_file and jd_input:
    file_path = f"data/resumes/{resume_file.name}"
    os.makedirs("data/resumes", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(resume_file.read())

    # Extract resume text
    resume_text = extract_text_from_resume(file_path)

    # Analyze Skill Gaps
    skill_gaps = analyze_resume_against_jd(resume_text, jd_input)
    st.subheader("🧩 Skill Gaps")
    st.write(skill_gaps)

    # Generate Learning Plan
    st.subheader("📚 Learning Plan")
    learning_plan = generate_learning_plan(skill_gaps)
    st.code(learning_plan)
