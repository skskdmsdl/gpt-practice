import time
import streamlit as st

st.title("Document GTP")

with st.chat_message("human"):
    st.write("Hello")

with st.chat_message("ai"):
    st.write("how are you")

with st.status("Embedding file..."):
    time.sleep(3)
    st.write("Getting a file download...")

st.chat_input("Send a message to the ai")