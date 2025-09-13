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
    "Full course or specific unit?",
    ["Full Course", "Specific Unit"]
)

selected_unit = None
if test_type == "Specific Unit":
    selected_unit = st.selectbox("Select unit:", ["Unit 1", "Unit 2", "Unit 3"])

num_questions = st.slider("Number of questions:", min_value=1, max_value=50, value=10)

if st.button("Generate Test"):
    st.write("AP Test:", selected_test)
    st.write("Test Type:", test_type)
    if selected_unit:
        st.write("Unit:", selected_unit)
    st.write("Number of questions:", num_questions)
    st.success("Test generated")
    answer = ask_cag_model("Hello World")
    st.write(answer)
