import requests
from src.nlp.text_cleaning import clean_text
from src.nlp.skill_extraction import extract_skills

RAPID_API_KEY = "e06cd25339mshd574e9edf490cb9p17af01jsn104f06a7d7d0"


HEADERS = {
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

def fetch_jobs(query: str, location: str = None, pages: int = 1):
    """
    Fetch job postings from the JSearch API.
    Returns a list of job dictionaries.
    """

    url = "https://jsearch.p.rapidapi.com/search"

    params = {
        "query": query,
        "num_pages": pages
    }

    if location:
        params["location"] = location

    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code != 200:
        print("Error fetching jobs:", response.text)
        return []

    data = response.json().get("data", [])
    jobs = []

    for job in data:
        title = job.get("job_title", "")
        company = job.get("employer_name", "")
        raw_desc = job.get("job_description", "")

        # clean + extract skills using your existing engine
        cleaned_desc = clean_text(raw_desc)
        skills = extract_skills(cleaned_desc)

        jobs.append({
            "title": title,
            "company": company,
            "description": cleaned_desc,
            "skills": skills,
            "raw": job
        })

    return jobs
