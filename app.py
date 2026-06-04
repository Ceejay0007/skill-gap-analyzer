from src.data.job_ingestion import load_job_description
from src.nlp.skill_extraction import extract_skills

text = load_job_description("sample_job_cleaned")
skills = extract_skills(text)

print("Skills found:", skills)
