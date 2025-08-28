# utils/ranker.py
from typing import List, Dict
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Cache model so it loads only once
_MODEL = None

def _get_model():
    global _MODEL
    if _MODEL is None:
        _MODEL = SentenceTransformer("all-MiniLM-L6-v2")
    return _MODEL

def compute_similarity(job_desc: str, resumes: List[str]) -> np.ndarray:
    """
    Compute cosine similarity between job description and resumes.

    Args:
        job_desc (str): Job description text
        resumes (List[str]): List of resume texts

    Returns:
        np.ndarray: Similarity scores for each resume
    """
    model = _get_model()
    jd_embedding = model.encode([job_desc], show_progress_bar=False)
    resumes_embeddings = model.encode(resumes, show_progress_bar=False)
    scores = cosine_similarity(jd_embedding, resumes_embeddings)[0]
    return scores

def rank_resumes(names: List[str], scores: np.ndarray) -> List[Dict]:
    """
    Rank resumes by similarity scores.

    Args:
        names (List[str]): Resume file names
        scores (np.ndarray): Similarity scores

    Returns:
        List[Dict]: Ranked list of resumes with scores
    """
    ranked = sorted(zip(names, scores.tolist()), key=lambda x: x[1], reverse=True)
    return [{"name": n, "score": float(s)} for n, s in ranked]
