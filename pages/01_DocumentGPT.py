import time
import streamlit as st

st.title("Document GTP")

with st.chat_message("human"):
    st.write("Hello")

with st.chat_message("ai"):
    st.write("how are you")

st.chat_input("Send a message to the ai")

with st.status("Embedding file...", expanded=True) as status:
    time.sleep(2)
    st.write("Getting the file")
    time.sleep(2)
    st.write("Embedding the file")
    time.sleep(2)
    st.write("Caching the file")
    status.update(label="Error", status="error")
