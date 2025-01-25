from services.commons.dbcalls import Contract
import streamlit as st


@st.dialog("Contract Rules")
def rule_dialog(contract_id):
    
    
    rules=Contract.get(contract_id)["rules"]

    st.write(rules)
    