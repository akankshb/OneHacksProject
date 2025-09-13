import streamlit as st
import sys
from pathlib import Path

from AI.models.model import ask_cag_model

st.header("Generate Practice Test")

selected_test = st.selectbox(
    "Select AP Test:",
    ["AP Chemistry", "AP Biology", "AP Calculus AB", "AP Calculus BC", "AP World History", "AP US History"]
)

test_type = st.selectbox(
    "MCQ or Free Response?",
    ["MCQ", "FRQ"]
)

selected_unit = None
selected_unit = st.selectbox("Select unit:", ["Unit 1", "Unit 2", "Unit 3"])
num_questions = st.slider("Number of questions:", min_value=1, max_value=15, value=5)

if st.button("Generate Test"):
    st.write("AP Test:", selected_test)
    st.write("Test Type:", test_type)
    if selected_unit:
        st.write("Unit:", selected_unit)
    st.write("Number of questions:", num_questions)
    query = "Based on the units you observe, create a " + test_type + " practice test on " + selected_unit + " with " + str(num_questions) + " questions"
    st.write(query)
    answer = ask_cag_model("query")
    st.success("Test generated")
    st.write(answer)
