Resume Screening Tool

## Approach

This project is a Streamlit web application that helps automate the process of screening resumes against a job description. The approach is as follows:

- The user uploads a job description and multiple resumes (PDF or TXT).
- Each resume and the job description are cleaned and converted to plain text.
- The tool uses TF-IDF vectorization and cosine similarity to score how well each resume matches the job description.
- Results are displayed in a ranked table for easy review.

## Libraries Used

- **streamlit**: For building the interactive web application.
- **pandas**: For data manipulation and displaying results.
- **nltk**: For text processing and cleaning.
- **pdfplumber**: For extracting text from PDF files.
- **scikit-learn**: For TF-IDF vectorization and cosine similarity scoring.
- **numpy**: For numerical operations.

## How to Run the Project

1. **Clone or download the project to your local machine.**
2. **Navigate to the project directory in your terminal.**
3. **Create and activate a virtual environment (optional but recommended):**
   ```
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```
4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```
   If you don't have a `requirements.txt`, install manually:
   ```
   pip install streamlit pandas nltk pdfplumber scikit-learn numpy
   ```
5. **Run the Streamlit app:**
   ```
   python -m streamlit run app.py
   ```
6. **Open the provided local URL (usually http://localhost:8501) in your browser to use the app.**

---

Feel free to modify or extend the project as needed for your use case!
