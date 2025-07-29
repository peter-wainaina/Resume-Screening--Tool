from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def score_resumes(job_desc, resumes):
    # resumes: list of resume texts
    documents = [job_desc] + resumes
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    job_vec = tfidf_matrix[0]
    resume_vecs = tfidf_matrix[1:]
    scores = cosine_similarity(job_vec, resume_vecs)[0]
    return scores 