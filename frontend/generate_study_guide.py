import streamlit as st

st.header("Generate Study Guide")

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

guide_type = st.radio(
    "Select type:",
    ["Guided Notes", "Study Guide"]
)

if st.button("Generate"):
    st.write("AP Test:", selected_test)
    st.write("Test Type:", test_type)
    if selected_unit:
        st.write("Unit:", selected_unit)
    st.write("Guide Type:", guide_type)
    st.success("Study guide generated")
