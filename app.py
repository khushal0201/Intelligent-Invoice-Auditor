import streamlit as st

st.set_page_config(
    page_title="first app",
    page_icon="👋",
    initial_sidebar_state="collapsed"
)




pg = st.navigation([st.Page("Todomain.py",title="maintodo"), st.Page("todonested.py",title="nestedtodo")])
pg.run()



