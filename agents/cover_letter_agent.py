from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

def generate_cover_letter(resume_text, job_text):
    groq_api_key = os.getenv("GROQ_API_KEY")

    llm = ChatGroq(
        temperature=0.5,
        groq_api_key=groq_api_key,
        model_name="llama3-8b-8192"  # or "llama3-70b-8192"
    )

    prompt = f"""
    Based on the resume below and the job description, write a personalized cover letter.

    Resume:
    {resume_text[:2000]}

    Job Description:
    {job_text[:2000]}

    Cover Letter:
    """

    return llm.invoke(prompt)
