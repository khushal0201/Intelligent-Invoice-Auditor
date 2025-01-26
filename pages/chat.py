import streamlit as st
import numpy as np

with st.chat_message("user"):
    st.write("Hello")
    st.line_chart(np.random.randn(30, 3))


prompt = st.chat_input("Choose a Contract or Invoice to Get Started")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")