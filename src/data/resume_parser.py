# resume_parser.py
# simple resume parser to extract text from pdf or docx

import docx2txt
import pdfplumber   # NEW

def parse_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def parse_docx(path):
    text = docx2txt.process(path)
    return text


def load_resume(path):
    if path.endswith(".pdf"):
        return parse_pdf(path)
    elif path.endswith(".docx"):
        return parse_docx(path)
    else:
        print("unsupported file type")
        return ""
