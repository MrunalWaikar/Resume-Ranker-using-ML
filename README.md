# Resume-Ranker-using-ML
# 📌 ML-Powered Resume Ranker

An AI-driven system that **automatically parses, analyzes, and ranks resumes** against a job description. This project helps recruiters save time and shortlist the most relevant candidates using **Natural Language Processing (NLP)** and **Machine Learning (ML)**.

---

## 🚀 Features

- 📄 **Resume Parsing** – Extracts text from PDF resumes using PyMuPDF.
- 🔍 **Semantic Similarity** – Uses **Sentence-BERT embeddings** to compare resumes with job descriptions.
- 📊 **Ranking & Scoring** – Assigns similarity scores and ranks resumes.
- 📈 **Visualization** – Displays bar charts of resume-job match scores.
- ⚡ **Streamlit Web App** – Interactive, easy-to-use interface.

---

## 🏗️ Tech Stack

- Python 3.8+  
- [Streamlit](https://streamlit.io/) – Web app interface  
- [PyMuPDF](https://pymupdf.readthedocs.io/) – PDF parsing  
- [Sentence-Transformers](https://www.sbert.net/) – Sentence embeddings  
- scikit-learn – Cosine similarity computation  
- Matplotlib – Visualization  

---
## 📂 Project Structure

resume-ranker/
│── app.py # Main Streamlit app
│── requirements.txt # Dependencies
│
├── parser/
│ └── parser.py # PDF text extraction
│
├── utils/
│ ├── ranker.py # Embedding + ranking functions
│ └── visualization.py # Bar chart plotting
│
├── data/
│ ├── resumes/ # Sample resumes (PDF)
│ └── job_description.txt # Sample job description
│
└── results/
└── output.json # Ranked results (optional)

