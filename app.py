import streamlit as st

st.set_page_config(
    page_title="Intelligent Invoice auditor",
    page_icon="👋",
    initial_sidebar_state="collapsed"
)




pg = st.navigation([st.Page("Todomain.py",title="maintodo"), st.Page("todonested.py",title="nestedtodo")])
pg.run()



