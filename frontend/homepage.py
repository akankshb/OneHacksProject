import streamlit as st

col1, col2, col3 = st.columns([1, 2, 1])

col4, col5 = st.columns([1, 1])

col6, col7, col8 = st.columns([1, 1, 1])

with col6:
    st.button("Home")

with col7:
    st.button("Practice Tests")

with col8:
    st.button("Study Guides")

with col2:
    st.title("App Name")
    st.subheader("slogan")

with col4:
    st.button("Generate Practice Tests")

with col5:
    st.button("Access Study Guides")

with col2: 
    st.subheader("Available AP Exams:")

ap_exams = [
    "AP Chemistry"
]

for exam in ap_exams:
    st.button(exam)
