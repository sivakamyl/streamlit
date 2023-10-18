import streamlit as st
import time

if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.spinner():
        time.sleep(0.4)
        with st.chat_message("user"):
            st.markdown(prompt)

response = f"Echo: {prompt}"
#can give avatar, st.image
with st.chat_message("assistant", avatar="🤖"):
    st.markdown(response)
