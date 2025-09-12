import streamlit as st

col1, col2, col3 = st.columns([1, 2, 1])

col4, col5 = st.columns([1, 1])

col6, col7, col8 = st.columns([1, 2, 1])
with col2:
        st.title("AP Momentum")
        st.subheader("Generate Unique Practice Based on Real AP Standards and Problems!")

with col4:
    if st.button("Generate Practice Tests", use_container_width=True):
        st.switch_page("frontend/generate_test.py")

with col5:
    if st.button("Access Study Guides", use_container_width=True):
        st.switch_page("frontend/generate_study_guide.py")

with col7: 
    st.subheader("Available AP Exams:")

    ap_exams = [
        "AP Chemistry",
        "AP Biology",
        "AP Calculus AB",
        "AP Calculus BC",
        "AP World History",
        "AP US History"
    ]

    rows = (len(ap_exams) + 2) // 3
    for i in range(rows):
        cols = st.columns(3)
        for j in range(3):
            index = i * 3 + j
            if index < len(ap_exams):
                cols[j].button(ap_exams[index], use_container_width=True)
