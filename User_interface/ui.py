import streamlit as st
import requests

st.title("LLM-Based Grading System")

problem = st.text_area("Problem")
reference = st.text_area("Reference Solution")
rubric = st.text_area("Rubric")
student_code = st.text_area("Student Code")

if st.button("Grade"):
    payload = {
        "problem": problem,
        "reference_solution": reference,
        "rubric": rubric,
        "student_code": student_code
    }
    res = requests.post("http://localhost:8000/grade", json=payload)
    st.json(res.json())
