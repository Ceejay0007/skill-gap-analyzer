# app.py
# just using this file to test stuff while building the project

from src.data.job_ingestion import load_job_description
from src.nlp.skill_extraction import extract_skills
from src.data.job_api import fetch_jobs
from src.data.resume_parser import load_resume
from src.engine.matching import match_skills
from src.engine.matching import match_skills, rank_jobs


"""# test for loading a local job file + extracting skills
def test_local_job_file():
    text = load_job_description("sample_job_cleaned")
    skills = extract_skills(text)
    print("skills from local file:", skills)
"""
"""# test for checking if the job API works
def test_job_api():
    jobs = fetch_jobs("data analyst", "USA")
    print("jobs from API:", jobs)
"""
"""# Test forthe Resume parser feature 
def test_resume_parser():
    text = load_resume("Conrad_Toke_Resume.pdf")
    print("resume text:", text[:500])  # print first 500 chars

    skills = extract_skills(text)
    print("skills from resume:", skills)
"""
# Resume matching to job describtion
def test_matching_engine():
    # STEP 1: load the resume and extract skills
    resume_text = load_resume("Conrad_Toke_Resume.pdf")  # load your resume file
    resume_skills = extract_skills(resume_text)          # get skills from resume

    # STEP 2: fetch a job and extract its skills
    jobs = fetch_jobs("data analyst", "USA")             # get job results
    job = jobs[0]                                        # pick the first job
    job_skills = extract_skills(job["description"])      # get skills from job description

    # STEP 3: compare resume skills with job skills
    result = match_skills(resume_skills, job_skills)

    # STEP 4: print the results
    print("Matched skills:", result["matched_skills"])
    print("Missing skills:", result["missing_skills"])
    print("Match score:", result["match_score"], "%")

def test_rank_multiple_jobs():
    # STEP 1: load resume and extract skills
    resume_text = load_resume("Conrad_Toke_Resume.pdf")
    resume_skills = extract_skills(resume_text)

    # STEP 2: fetch multiple jobs
    jobs = fetch_jobs("data analyst", "USA")

    # STEP 3: extract skills for each job
    for job in jobs:
        job["skills"] = extract_skills(job["description"])

    # STEP 4: rank jobs by match score
    ranked = rank_jobs(resume_skills, jobs)

    # STEP 5: print top 5 jobs
    for job in ranked[:5]:
        print("\nJob Title:", job["title"])
        print("Company:", job["company"])
        print("Match Score:", job["match_score"], "%")
        print("Matched Skills:", job["matched_skills"])
        print("Missing Skills:", job["missing_skills"])
        
    # print resume skills ONCE
    print("\nExtracted resume skills:", resume_skills)
    print(resume_text[:1000])

# choose which test to run
if __name__ == "__main__":
    # test_local_job_file()   # old test, keeping it here for later
    # test_job_api()            # running the API test for now
    #test_resume_parser()
   # test_matching_engine()
   test_rank_multiple_jobs()


