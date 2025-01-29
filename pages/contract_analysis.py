
import streamlit as st
import time
from services.commons.docIntelligence import extractContent
from services.commons.gptCall import invoiceAnalysis,extractInvoice
from services.commons.dbcalls import Invoice,Contract
from services.constants.enums import values,color
import pandas as pd



a,b,c=st.columns(3)

with a:
    if st.button("Back",key="secondary"):
        st.switch_page("pages/Contracts.py")
    
contractId=None

if 'contractId1' in st.session_state:
    print("inside")
    contractId=st.session_state.contractId1


# print(" rerun contractId",contractId)

contractList=list(Contract.get())


option = c.selectbox(
    "Select a Contract",
    options=range(len(contractList)),
    index=contractId,
    format_func=lambda x: contractList.__getitem__(x)["name"],
    placeholder="Select Contract",
    label_visibility="collapsed"
)

if option is None:
    st.header("Select a Contract to view Invoices")

else:
    invList=Invoice.get(contractId=option)
    df = pd.DataFrame(columns=['Invoice', 'Anomalies'])
    print(len(invList))
    for j in range(0,len(invList)):
        df1=Invoice.get(i=j)
        print(df1)
        df.loc[len(df)]=[df1['name'],len(df1['anomalies'])]
    st.dataframe(df, width=800)
    st.bar_chart(df,x="Invoice",y="Anomalies")


