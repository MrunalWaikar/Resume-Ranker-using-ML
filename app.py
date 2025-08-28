# app.py
import streamlit as st
from parser.parser import extract_text_from_pdf
from utils.ranker import compute_similarity, rank_resumes
from utils.visualization import plot_score_bars

def main():
    st.title("📄 AI-Powered Resume Ranker")
    st.write("Upload resumes and provide a job description to rank resumes by similarity.")

    # Upload resumes
    uploaded_files = st.file_uploader("Upload Resumes (PDF only)", type="pdf", accept_multiple_files=True)

    # Job description input
    job_description = st.text_area("Paste Job Description here")

    if st.button("Rank Resumes"):
        if not uploaded_files or not job_description.strip():
            st.warning("Please upload at least one resume and enter a job description.")
            return

        # Extract text from resumes
        resume_texts, names = [], []
        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            resume_texts.append(text)
            names.append(file.name)

        # Compute similarity scores
        scores = compute_similarity(job_description, resume_texts)
        ranked = rank_resumes(names, scores)

        # Display ranking
        st.subheader("📊 Ranked Resumes")
        for i, r in enumerate(ranked, 1):
            st.write(f"**{i}. {r['name']}** - Score: {r['score']:.4f}")

        # Show visualization
        st.pyplot(plot_score_bars(ranked))

if __name__ == "__main__":
    main()
