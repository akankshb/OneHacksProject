import streamlit as st

home_page = st.Page("frontend/homepage.py", title="Home")
test_page = st.Page("frontend/generate_test.py", title="Practice Tests")
study_page = st.Page("frontend/generate_study_guide.py", title="Study Guides")

pg = st.navigation([home_page, test_page, study_page], position="top")

pg.run()
