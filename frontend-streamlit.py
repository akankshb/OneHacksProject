import streamlit as st
from pathlib import Path
import sys

# # Add your backend path so we can import query_bot
# sys.path.append(str(Path(__file__).parent.parent / "backend" / "app" / "services"))

# Add AI/models to sys.path
sys.path.append(str(Path(__file__).parent / "AI" / "models"))

# from generation import query_bot  # import your function

from model import ask_cag_model  # import your function

st.title("AP momentum Bot 🤖")

# Text input
user_query = st.text_input("Ask a question about AB subjects:")

# Button to submit
if st.button("Submit"):
    if user_query.strip() == "":
        st.warning("Please enter a question first!")
    else:
        with st.spinner("Fetching answer..."):
            try:
                answer = ask_cag_model(user_query)  # call your backend function
                st.markdown(f"**Answer:** {answer}")
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
