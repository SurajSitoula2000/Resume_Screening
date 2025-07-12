import streamlit as st
from matcher import get_resume_scores

st.title("📄 Resume Screening & Matching System")
st.markdown("Match resumes against a job description using NLP.")

if st.button("Run Matcher"):
    scores = get_resume_scores('C:\Users\SURAJ\OneDrive\Desktop\Resume_Builder\jobDescription.txt', "Resume_Builder")
    st.subheader("Match Scores:")
    for name, score in scores:
        st.write(f"**{name}** → Score: {score}")
        