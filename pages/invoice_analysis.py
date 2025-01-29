
import streamlit as st
import time
from services.commons.docIntelligence import extractContent
from services.commons.gptCall import invoiceAnalysis,extractInvoice
from services.commons.dbcalls import Invoice,Contract
from services.constants.enums import values,color
import altair as alt


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
    invoiceId=None

    if 'invoiceId' in st.session_state:
        print("inside")
        invoiceId=st.session_state.invoiceId

    invList=Invoice.get(contractId=option)

    option1 = c.selectbox(
        "Select a Invoice",
        options=range(len(invList)),
        index=invoiceId,
        format_func=lambda x: invList.__getitem__(x)["name"],
        placeholder="Select invoice",
        label_visibility="collapsed"
    )
    if option1 is None:
        st.header("Select an invoice")

    else:
        # df=Invoice.get(i=)["employeeData"]
        ind=invList[option1]["actualInd"]
        df1=Invoice.get(i=ind)["employeeData"]
        if df1 is not None and not df1.empty:
            df = df1.groupby('contractorName')[['hours', 'amount']].sum()
            df = df.reset_index()
            st.write("")
            st.write("")
            st.dataframe(df, width=800)
            #chart 1
            chart = alt.Chart(df).mark_bar().encode(
                x='contractorName',
                y=alt.Y('amount', title='Amount',),
            ).interactive()
            #chart 2
            chart1 = alt.Chart(df).mark_line().encode(
                x='contractorName',
                y=alt.Y('hours', title='Hours'),
            ).interactive()

            tab1, tab2 = st.tabs(["Employee Recevied Amount", "Employee Working Hours Trend"])

            with tab1:
                # Use the Streamlit theme.
                # This is the default. So you can also omit the theme argument.
                st.altair_chart(chart, theme="streamlit", use_container_width=True)
            with tab2:
                # Use the native Altair theme.
                st.altair_chart(chart1, theme="streamlit", use_container_width=True)
        else:
            st.header("No Data in invoice")


