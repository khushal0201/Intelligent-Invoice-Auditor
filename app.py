import streamlit as st

st.set_page_config(
    page_title="Intelligent Invoice auditor app",
    page_icon="👋",
    initial_sidebar_state="collapsed"
)



ContractPage=st.Page("pages/Contracts.py",title="Contract",icon="📄")

InvoicePage=st.Page("pages//Invoices.py",title="Invoice",icon="📃")

# pg = st.navigation([st.Page("Todomain.py",title="maintodo"), st.Page("todonested.py",title="nestedtodo")])

pg = st.navigation([ContractPage,InvoicePage])
pg.run()



# st.sidebar.header("App")


