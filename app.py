# app.py
# just using this file to test stuff while building the project

from src.data.job_ingestion import load_job_description
from src.nlp.skill_extraction import extract_skills
from src.data.job_api import fetch_jobs
from src.data.resume_parser import load_resume


"""# test for loading a local job file + extracting skills
def test_local_job_file():
    text = load_job_description("sample_job_cleaned")
    skills = extract_skills(text)
    print("skills from local file:", skills)
"""
# test for checking if the job API works
def test_job_api():
    jobs = fetch_jobs("data analyst", "USA")
    print("jobs from API:", jobs)

# Test forthe Resume parser feature 
def test_resume_parser():
    text = load_resume("CONRAD TOKE_Data Science Intern_20260508.pdf")
    print("resume text:", text[:500])  # print first 500 chars

    skills = extract_skills(text)
    print("skills from resume:", skills)

# choose which test to run
if __name__ == "__main__":
    # test_local_job_file()   # old test, keeping it here for later
    # test_job_api()            # running the API test for now
    test_resume_parser()


