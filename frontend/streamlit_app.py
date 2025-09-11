import streamlit as st

home_page = st.Page("homepage.py", title="Home")
test_page = st.Page("generate_test.py", title="Practice Tests")
study_page = st.Page("/generate_study_guide.py", title="Study Guides")

pg = st.navigation([st.Page("home_page"), st.Page("test_page"), st.Page("study_page")])

pg.run()
