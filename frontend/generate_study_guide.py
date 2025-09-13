import streamlit as st
from AI.models.model import ask_cag_model

st.header("Generate Study Guide")

selected_test = st.selectbox(
    "Select AP Test:",
    ["AP Chemistry", "AP Biology", "AP Calculus AB", "AP Calculus BC", "AP World History", "AP US History"]
)


selected_unit = st.selectbox("Select unit:", ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5", "Unit 6", "Unit 8", "Unit 9"])

guide_type = st.radio(
    "Select type:",
    ["Guided Notes", "Study Guide"]
)

if st.button("Generate"):
    query = "Based on the units observed, create a " + guide_type + " for " + selected_test + " " + selected_unit
    st.write("AP Test:", selected_test)
    if selected_unit:
        st.write("Unit:", selected_unit)
    st.write("Guide Type:", guide_type)
    answer = ask_cag_model(query)
    st.success("Study guide generated")
    st.write(answer)
