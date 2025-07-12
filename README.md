# AI-Powered Resume Screening App

Resume_Screening_App/
├── app.py
├── matcher.py
├── main.py                    ← (optional, CLI version)
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── jobDescription.txt
│   └── resumes/
│       ├── alice.txt
│       ├── bob.txt
│       └── charlie.txt


## 📌 Features

- Match resumes to a job description using `spaCy`
- Cosine similarity-based scoring
- Streamlit web interface
- Text-only input – lightweight and fast
- BERT-compatible upgrade option

# Install
pip install -r requirements.txt
python -m spacy download en_core_web_md

Tech Stack
Python
Streamlit
spaCy (en_core_web_md)
scikit-learn
Cosine Similarity

# Future Enhancements
Integrate Sentence-BERT for improved accuracy
Upload PDF/Docx resumes
Feedback-based ranking
Save matches to a database

## Made by Suraj Sitoula – MCA Student | Aspiring Data Analyst
Connect on LinkedIn if you found this helpful!

