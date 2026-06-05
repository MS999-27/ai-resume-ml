from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Job role profiles (training data for our ML model)
JOB_PROFILES = {
    "Software Engineer": "python java javascript coding algorithms data structures git docker system design",
    "Data Scientist": "python machine learning deep learning tensorflow pytorch statistics pandas numpy data analysis visualization",
    "Web Developer": "html css javascript react nodejs frontend backend databases api restful",
    "ML Engineer": "machine learning deep learning mlops deployment pytorch tensorflow scikit-learn python pipelines",
    "Data Analyst": "sql excel tableau power bi data analysis statistics reporting visualization python",
    "DevOps Engineer": "docker kubernetes aws azure ci cd linux bash terraform cloud infrastructure",
    "Cybersecurity Analyst": "network security penetration testing firewall linux python ethical hacking",
}

def match_job_roles(user_skills: list, top_n: int = 3):
    """
    Uses TF-IDF vectorization + cosine similarity (ML technique)
    to find the best matching job roles for a candidate's skills.
    """
    print("🤖 Running ML skill matching (TF-IDF + Cosine Similarity)...")
    
    # Combine user skills into one string
    user_text = " ".join(user_skills).lower()
    
    # Prepare corpus: job profiles + user skills
    job_titles = list(JOB_PROFILES.keys())
    job_texts = list(JOB_PROFILES.values())
    
    corpus = job_texts + [user_text]
    
    # Apply TF-IDF Vectorization (ML step)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # Cosine similarity between user and each job profile
    user_vector = tfidf_matrix[-1]  # last item is user
    job_vectors = tfidf_matrix[:-1]
    
    similarities = cosine_similarity(user_vector, job_vectors)[0]
    
    # Rank jobs by similarity score
    ranked_indices = np.argsort(similarities)[::-1][:top_n]
    
    results = []
    for i in ranked_indices:
        results.append({
            "job_title": job_titles[i],
            "match_score": round(float(similarities[i]) * 100, 2)
        })
    
    return results


def suggest_missing_skills(user_skills: list, target_job: str):
    """
    Suggests skills the user is missing for their target job
    """
    if target_job not in JOB_PROFILES:
        return []
    
    job_skills = set(JOB_PROFILES[target_job].lower().split())
    user_skills_set = set([s.lower() for s in user_skills])
    
    missing = job_skills - user_skills_set
    return list(missing)[:6]  # top 6 missing skills


if __name__ == "__main__":
    # Test it
    skills = ["Python", "Machine Learning", "TensorFlow", "Pandas", "Statistics"]
    matches = match_job_roles(skills)
    print("Top job matches:", matches)
    
    missing = suggest_missing_skills(skills, "Data Scientist")
    print("Missing skills:", missing)