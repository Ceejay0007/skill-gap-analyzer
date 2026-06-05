#import libraries
import requests
import json
from pathlib import Path

# setting up the folder where job descriptions will be saved
DATA_DIR = Path("data/jobs")
DATA_DIR.mkdir(parents=True, exist_ok=True)  # creates the folder if it doesn't exist


def fetch_job_description(url: str) -> str:
    """
    gets the raw job description from a URL
    right now it just downloads the HTML page
    """
    response = requests.get(url)  # send a GET request to the page
    return response.text  # return the page content as text


def save_job_description(text: str, filename: str):
    """
    saves the job description text into a .txt file
    """
    filepath = DATA_DIR / f"{filename}.txt"  # build the file path
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)  # write the text into the file


def load_job_description(filename: str) -> str:
    """
    loads a saved job description from the folder
    """
    filepath = DATA_DIR / f"{filename}.txt"  # build the file path
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()  # read and return the file content
