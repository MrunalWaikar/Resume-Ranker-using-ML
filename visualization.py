# utils/visualization.py
from typing import List, Dict
import matplotlib.pyplot as plt

def plot_score_bars(ranked: List[Dict]):
    """
    Create a bar chart of similarity scores for ranked resumes.

    Args:
        ranked (List[Dict]): List of {"name": str, "score": float}

    Returns:
        matplotlib.figure.Figure
    """
    names = [r["name"] for r in ranked]
    scores = [r["score"] for r in ranked]

    fig = plt.figure(figsize=(8, 4))
    plt.bar(names, scores)
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Similarity Score")
    plt.title("Resume Ranking Scores")
    plt.tight_layout()
    return fig
