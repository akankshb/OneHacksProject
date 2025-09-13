import streamlit as st
import sys
from pathlib import Path

from AI.models.model import ask_cag_model

st.header("Generate Practice Test")

selected_test = st.selectbox(
    "Select AP Test:",
    ["AP Chemistry", "AP Biology", "AP Calculus AB", "AP Calculus BC", "AP World History", "AP US History"]
)


selected_unit = None
selected_unit = st.selectbox("Select unit:", ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5", "Unit 6", "Unit 8", "Unit 9"])
if st.button("Generate Test"):
    st.write("AP Test:", selected_test)
    if selected_unit:
        st.write("Unit:", selected_unit)
    query = "Based on the units you observe, create a practice test on " + selected_unit + " for " + selected_test
    # st.write(query)
    answer = ask_cag_model(query)
    st.success("Test generated")
    st.write(answer)
