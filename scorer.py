from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def score_resumes(job_desc, resumes):
    # Combine job description with resumes for joint vectorization
    documents = [job_desc] + resumes

    # TF-IDF with stopword removal and bigrams
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
    tfidf_matrix = vectorizer.fit_transform(documents)

    job_vec = tfidf_matrix[0]
    resume_vecs = tfidf_matrix[1:]

    scores = cosine_similarity(job_vec, resume_vecs)[0]
    return scores
