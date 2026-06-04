import re
from bs4 import BeautifulSoup

# this function cleans the raw HTML we get from job postings
def clean_text(raw_html: str) -> str:
    """
    takes the raw HTML from a job posting
    and returns clean text that we can use for NLP
    """

    # remove all the HTML tags and keep only the text
    soup = BeautifulSoup(raw_html, "html.parser")
    text = soup.get_text()

    # make everything lowercase so it's consistent
    text = text.lower()

    # remove extra spaces, newlines, tabs, etc.
    text = re.sub(r"\s+", " ", text).strip()

    return text

'''This function takes the raw HTML from a 
job posting,strips out all the tags using 
BeautifulSoup,lowercases the text, removes
extra whitespace,and returns clean text ready
for NLP'''