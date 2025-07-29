# agents/learning_path_agent.py
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

def generate_learning_plan(skill_gap_text):
    llm = ChatGroq(
    temperature=0,
    model_name="llama3-8b-8192",  
    groq_api_key=os.getenv("GROQ_API_KEY")
)
    prompt = f"""
    I have the following skill gaps: {skill_gap_text}
    Create a 30-day learning plan with:
    - Daily goals
    - Course/video/blog recommendations
    - Weekly review tasks
    Tailor it for a B.Tech CSE AIML student looking for AI/ML career roles.
    """
    return llm.predict(prompt)
