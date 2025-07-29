# agents/tools.py
import docx
import pdfminer.high_level

def extract_text_from_resume(file_path):
    if file_path.endswith(".pdf"):
        return pdfminer.high_level.extract_text(file_path)
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return "Unsupported file format"


import json

def save_user_profile(email, resume_text, skill_gaps, learning_plan):
    profile = {
        "resume": resume_text,
        "skill_gaps": skill_gaps,
        "learning_plan": learning_plan
    }
    with open(f"data/user_profiles/{email.replace('@', '_')}.json", "w") as f:
        json.dump(profile, f, indent=2)
