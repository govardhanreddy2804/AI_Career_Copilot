from agents.resume_agent import analyze_resume_against_jd
from agents.learning_path_agent import generate_learning_plan
from agents.cover_letter_agent import generate_cover_letter
from agents.job_match_agent import find_matching_jobs

def run_full_career_analysis(resume_text, jd_text):
    gaps = analyze_resume_against_jd(resume_text, jd_text)
    plan = generate_learning_plan(gaps)
    cover_letter = generate_cover_letter(resume_text, jd_text)
    jobs = find_matching_jobs(resume_text)
    return {
        "skill_gaps": gaps,
        "learning_plan": plan,
        "cover_letter": cover_letter,
        "matched_jobs": jobs
    }
