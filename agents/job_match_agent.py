# agents/job_match_agent.py
import json
import os
from langchain_groq import ChatGroq

def find_matching_jobs(resume_text):
    with open("data/jobs.json") as f:
        jobs = json.load(f)

    # Construct prompt with resume and job titles/descriptions
    prompt = f"""Based on this resume: {resume_text}
    Match it to these jobs and rank them:
    {jobs}
    """

    llm = ChatGroq(temperature=0.5, groq_api_key=os.getenv("GROQ_API_KEY"))
    return llm.predict(prompt)
