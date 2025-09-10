import streamlit as st

st.title("knowt")
st.subheader("slogan or fact")


with col1:
    st.button("Generate real practice tests with answer keys and explanations.")
with col2:
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

with col2:
