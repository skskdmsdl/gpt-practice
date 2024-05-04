import streamlit as st
from langchain.prompts import PromptTemplate
from datetime import datetime

st.set_page_config(
    page_title="FullstackGPT",
    page_icon="🧸",
)

today = datetime.today().strftime("%H:%M:%S")

with st.sidebar:
    st.title("sidebar title")
    st.text_input("extra")

tab_one, tab_two, tab_three = st.tabs(["A", "B", "C"])

with tab_one:
    st.write("a")

with tab_two:
    st.write("b")

with tab_three:
    st.write("c")