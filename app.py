import pandas as pd
import streamlit as st
import os
import tempfile
from resume_parser import (
    extract_text_from_pdf,
    extract_text_from_txt,
    clean_text,
)
from scorer import score_resumes


st.title('Resume Screening Tool')

st.write('Upload a job description and multiple resumes (PDF or TXT). The tool will rank resumes based on their match to the job description.')

job_desc = st.text_area('Paste the Job Description here:')
resume_files = st.file_uploader('Upload Resumes (PDF or TXT, multiple allowed)', type=[
                                'pdf', 'txt'], accept_multiple_files=True)

if st.button('Check Resumes'):
    if not job_desc or not resume_files:
        st.warning(
            'Please provide both a job description and at least one resume.')
    else:
        cleaned_job_desc = clean_text(job_desc)
        resume_texts = []
        resume_names = []
        for uploaded_file in resume_files:
            # Save to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name
            if uploaded_file.name.lower().endswith('.pdf'):
                text = extract_text_from_pdf(tmp_path)
            else:
                text = extract_text_from_txt(tmp_path)
            cleaned = clean_text(text)
            resume_texts.append(cleaned)
            resume_names.append(uploaded_file.name)
            os.remove(tmp_path)
        scores = score_resumes(cleaned_job_desc, resume_texts)
        results = pd.DataFrame({'Resume': resume_names, 'Score': scores})
        results = results.sort_values(
            'Score', ascending=False).reset_index(drop=True)
        st.subheader('Results:')
        st.dataframe(results)
