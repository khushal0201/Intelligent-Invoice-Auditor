import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(
    layout= "wide",
    page_title="Intelligent Invoice auditor app",
    page_icon="👋",
    initial_sidebar_state="collapsed"
)

nav = get_nav_from_toml(
    ".streamlit/pages.toml"
)

# st.logo("logo.webp")
st.logo("logo.webp", size="large",)

# ContractPage=st.Page("pages/Contracts.py",title="Contract",icon="📄")

# InvoicePage=st.Page("pages//Invoices.py",title="Invoice",icon="📃")

# pg = st.navigation([st.Page("Todomain.py",title="maintodo"), st.Page("todonested.py",title="nestedtodo")])
pg = st.navigation(nav)
add_page_title(pg)
pg.run()
# pg = st.navigation([ContractPage,InvoicePage])

# st.sidebar.header("App")
