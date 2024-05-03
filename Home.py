import streamlit as st
from langchain.prompts import PromptTemplate
from datetime import datetime

st.set_page_config(
    page_title="FullstackGPT",
    page_icon="🧸",
)

today = datetime.today().strftime("%H:%M:%S")

st.title(today)

st.title("Hello world!")

st.subheader("Welcome to Streamlit")

st.markdown(
    """
    #### I Love it
    """
)

st.write("hello")

st.write([1, 2, 3, 4, 5])

st.write({"x": 1})

st.write(PromptTemplate)

st.selectbox("Choose your model", ("GPT-3", "GPT-4"))

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