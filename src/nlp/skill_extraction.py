import re

SKILL_KEYWORDS = [
    "python", "sql", "r", "pandas", "numpy", "scikit-learn", "matplotlib",
    "seaborn", "pyspark", "nltk", "aws", "terraform", "excel", "power bi",
    "machine learning", "deep learning", "data analysis", "cloud", "etl",
    "communication", "teamwork"
]

def extract_skills(text):
    text = text.lower()

    # normalize punctuation: replace commas, slashes, hyphens with spaces
    text = re.sub(r"[,/()-]", " ", text)

    found = []
    for skill in SKILL_KEYWORDS:
        if skill in text:
            found.append(skill)

    return found
