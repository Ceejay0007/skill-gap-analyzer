import re

# a simple list of skills we want to look for
# later we can expand this or load it from a file to match the full skill set
SKILL_KEYWORDS = [
    "python", "sql", "excel", "machine learning", "deep learning",
    "pandas", "numpy", "communication", "teamwork", "data analysis",
    "aws", "azure", "tensorflow", "pytorch", "nlp", "statistics"
]

# this function finds which skills appear in the cleaned job text
def extract_skills(text: str):
    """
    checks the job description text and returns
    a list of skills that were found
    """

    found_skills = []

    # loop through each skill and check if it's in the text
    for skill in SKILL_KEYWORDS:
        # using regex to match whole words
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills

'''I created a simple skill extraction module that uses a list of known 
skills and checks if they appear in the cleaned job description text. 
It uses regex to match whole words so we do not get false matches. Later, 
I will replace this with a more advanced embedding based extractor.'''