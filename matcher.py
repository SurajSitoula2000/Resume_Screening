import os
import numpy as np
import spacy
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load('en_core_web_md')


def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_resume_scores(jd_path, Resume_Builder):
    jd_text = load_text(jd_path)
    jd_vector = nlp(jd_text).vector

    results = []
    for fname in os.listdir(Resume_Builder):
        if fname.endswith('.txt'):
            res_text = load_text(os.path.join(Resume_Builder, fname))
            res_vector = nlp(res_text).vector
            score = cosine_similarity([jd_vector], [res_vector])[0][0]
            results.append((fname.replace(".txt", ""), round(score, 3)))

    return sorted(results, key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    jd_text = load_text("C:\Users\SURAJ\OneDrive\Desktop\Resume_Builder\jobDescription.txt")
    scores = get_resume_scores(jd_text, "Resume_Builder")
    print("\nTop Resume Matches:\n")
    for name, score in scores:
        print(f"{name} → Score: {score}")
