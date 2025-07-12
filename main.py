import spacy
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy model
nlp = spacy.load("en_core_web_md")

# Example job description and resumes
job_desc = """We are looking for a Data Scientist with strong Python, Machine Learning, and NLP skills.
The ideal candidate will have experience with scikit-learn, pandas, and deploying models using Streamlit or Flask."""

resumes = {
    "Alice": """Alice has 2 years of experience as a Data Scientist. She is proficient in Python, pandas,
                and machine learning. She recently worked on deploying NLP models using Streamlit.""",    
    "Bob": """Bob is a software engineer with experience in Java and C++. He has limited knowledge of
              data science and machine learning, but is a fast learner.""",    
    "Charlie": """Charlie has worked with machine learning and NLP projects. He has used spaCy and scikit-learn
                  and is familiar with model deployment using Flask."""
}

# Vectorize and calculate similarity
job_vector = nlp(job_desc).vector
results = {}

for name, text in resumes.items():
    resume_vector = nlp(text).vector
    sim = cosine_similarity([job_vector], [resume_vector])[0][0]
    results[name] = round(sim, 3)

# Sort results by similarity
sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
sorted_results
