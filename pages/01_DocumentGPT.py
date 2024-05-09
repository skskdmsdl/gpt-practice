import time
import streamlit as st

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="🦠"
)

st.title("Document GTP")

messages = []

def send_message(message, role):
    with st.chat_message(role):
        st.write(message)
        messages.append({"message":message, "role":role})
    st.write(messages)

message = st.chat_input("Send a message to the ai")

if message:
    send_message(message, "human")
    time.sleep(2)
    send_message(f"You said: {message}", "ai")