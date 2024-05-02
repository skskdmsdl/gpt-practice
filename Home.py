import streamlit as st
from langchain.prompts import PromptTemplate
from datetime import datetime

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

st.sidebar.title("sidebar title")

