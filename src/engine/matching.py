# matching.py
# this file compares resume skills with job skills
# and tells us what skills match and what skills are missing

def match_skills(resume_skills, job_skills):
    # turn both lists into sets so we can compare them easily
    resume_set = set([s.lower() for s in resume_skills])  # skills from resume
    job_set = set([s.lower() for s in job_skills])        # skills required by job

    # find skills that appear in both resume and job
    matched = resume_set.intersection(job_set)

    # find skills the job wants but the resume does not have
    missing = job_set - resume_set

    # calculate match score (percentage)
    if len(job_set) > 0:
        match_score = round((len(matched) / len(job_set)) * 100, 2)
    else:
        match_score = 0  # avoid division by zero

    # return everything in a dictionary
    return {
        "matched_skills": list(matched),
        "missing_skills": list(missing),
        "match_score": match_score
    }


def rank_jobs(resume_skills, job_list):
    # this function compares resume skills with multiple jobs
    # and returns the jobs ranked by match score

    results = []

    for job in job_list:
        job_skills = job["skills"]  # to will extract skills before calling this
        match = match_skills(resume_skills, job_skills)

        results.append({
            "title": job["title"],
            "company": job["company"],
            "match_score": match["match_score"],
            "matched_skills": match["matched_skills"],
            "missing_skills": match["missing_skills"],
            "description": job["description"]
        })

    # sort jobs from best match to worst match
    results.sort(key=lambda x: x["match_score"], reverse=True)

    return results
