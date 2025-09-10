import streamlit as st

col1, col2, col3 = st.columns([1, 2, 1])

col4, col5 = st.columns([1, 1])

with col2:
    st.title("knowt")
    st.subheader("slogan or fact")

with col4:
    st.button("Generate real practice tests with answer keys and explanations.")

with col5:
    st.button("Access study guides")

if st.button("Generate real practice tests with answer keys and explanations."):
    pass

if st.button("Access study guides"):
    pass

st.subheader("Available AP Exams:")

ap_exams = [
    "AP Chemistry"
]

for exam in ap_exams:
    st.button(exam)
