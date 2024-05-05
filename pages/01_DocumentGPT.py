import streamlit as st

st.title("Document GTP")

with st.chat_message("human"):
    st.write("Hello")

with st.chat_message("ai"):
    st.write("how are you")

st.chat_input("Send a message to the ai")