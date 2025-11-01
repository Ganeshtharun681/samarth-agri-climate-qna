import streamlit as st
from samarth_core import answer_query

st.set_page_config(page_title="Project Samarth ", layout="centered")

st.title("Project Samarth")
st.caption("Intelligent Q&A over Indian Government Data (Rainfall + Crop Production)")

query = st.text_input("Ask a question (e.g., 'Compare rainfall between 2020 and 2024', or 'Show top 5 states by production'):")

if query:
    answer, source = answer_query(query)
    st.markdown(f"**Answer:** {answer}")
    st.caption(f"{source}")
