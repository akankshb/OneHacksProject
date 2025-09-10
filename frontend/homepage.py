import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "Home"

col1, col2, col3 = st.columns([1, 2, 1])

col4, col5 = st.columns([1, 1])

col6, col7, col8 = st.columns([1, 1, 1])

with col6:
    if st.button("Home", use_container_width=True):
        st.session_state.page = "Home"

with col7:
    if st.button("Practice Tests", use_container_width=True):
        st.session_state.page = "Practice Tests"

with col8:
    if st.button("Study Guides", use_container_width=True):
        st.session_state.page = "Study Guides"

if st.session_state.page == "Home":
    with col2:
        st.title("App Name", use_container_width=True)
        st.subheader("slogan", use_container_width=True)

    with col4:
        if st.button("Generate Practice Tests", use_container_width=True):
            st.session_state.page = "Practice Tests"

    with col5:
        if st.button("Access Study Guides", use_container_width=True):
            st.session_state.page = "Study Guides"

    with col2: 
        st.subheader("Available AP Exams:", use_container_width=True)

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

elif st.session_state.page == "Practice Tests":
    with col2:
        st.header("Practice Tests")
        st.write("Placeholder for practice test generation page.")

elif st.session_state.page == "Study Guides":
    with col2:
        st.header("Study Guides")
        st.write("Placeholder for study guide page.")
