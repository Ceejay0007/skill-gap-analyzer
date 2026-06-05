import streamlit as st
import sys
import os

# Make sure Streamlit Cloud can find the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.data.resume_parser import load_resume
from src.data.job_api import fetch_jobs
from src.nlp.skill_extraction import extract_skills
from src.engine.matching import rank_jobs
import tempfile 

st.set_page_config(page_title="Skill Gap Analyzer", layout="wide")

st.title("🔍 Skill Gap Analyzer")
st.write("Upload your resume and compare it to real job postings instantly.")

# --- Resume Upload ---
uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp:
        tmp.write(uploaded_file.getbuffer())
        temp_path = tmp.name

    resume_text = load_resume(temp_path)

    st.success("Resume uploaded successfully!")

    # Extract skills
    resume_skills = extract_skills(resume_text)

    st.subheader("📌 Extracted Skills From Your Resume")
    st.write(", ".join(resume_skills) if resume_skills else "No skills detected.")

    # --- Job Search ---
    st.subheader("🔎 Search for Jobs")
    job_title = st.text_input("Job title", "data analyst")
    location = st.text_input("Location", "USA")

    if st.button("Find Matching Jobs"):
        with st.spinner("Fetching jobs..."):
            jobs = fetch_jobs(job_title, location)

            # Extract skills for each job
            for job in jobs:
                job["skills"] = extract_skills(job["description"])

            ranked_jobs = rank_jobs(resume_skills, jobs)

        st.subheader("🏆 Top Matching Jobs")

        for job in ranked_jobs[:5]:
            st.markdown(f"""
            ### **{job['title']}**  
            **Company:** {job['company']}  
            **Match Score:** {job['match_score']}%  

            **Matched Skills:** {", ".join(job['matched_skills']) if job['matched_skills'] else "None"}  
            **Missing Skills:** {", ".join(job['missing_skills']) if job['missing_skills'] else "None"}  

            ---
            """)
