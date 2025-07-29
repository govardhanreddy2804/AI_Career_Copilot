# agents/resume_agent.py
import os
from langchain.agents import initialize_agent, Tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# def analyze_resume_against_jd(resume_text, job_text):
#     llm = ChatGroq(temperature=0, model_name="llama3-8b-8192", groq_api_key=os.getenv("GROQ_API_KEY"))

#     tools = [
#         Tool(name="ResumeText", func=lambda x: resume_text, description="Provides the resume text"),
#         Tool(name="JDText", func=lambda x: job_text, description="Provides the job description")
#     ]

#     agent = initialize_agent(
#         tools=tools,
#         llm=llm,
#         agent_type="zero-shot-react-description",
#         verbose=True
#     )

#     return agent.run("Compare ResumeText and JDText. List the skills missing in the resume.")
def analyze_resume_against_jd(resume_text, job_text):
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama3-8b-8192"
    )

    prompt = f"""
    Below is a resume and a job description.
    Identify the missing skills in the resume based on the job description.

    Resume:
    {resume_text[:3000]}  # ✅ truncate to ~3000 chars to stay under limit

    Job Description:
    {job_text[:3000]}

    List the missing skills.
    """

    return llm.invoke(prompt)

