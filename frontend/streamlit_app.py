import streamlit as st

home_page = st.Page("pages/home.py", title="Home")
test_page = st.Page("pages/generate_test.py", title="Practice Tests")
study_page = st.Page("pages/generate_study_guide.py", title="Study Guides")

pg = st.navigation([home_page, test_page, study_page])

st.set_page_config(page_title="AP Study App", page_icon="📚")

pg.run()
