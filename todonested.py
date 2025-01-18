import streamlit as st


if st.button("Back",key="secondary"):
    st.switch_page("Todomain.py")

st.title("Welcome to Invoices")
addbtn=st.button("Add an Invoice", type="primary")