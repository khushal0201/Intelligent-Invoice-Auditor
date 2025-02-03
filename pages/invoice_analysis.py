
import streamlit as st
from services.commons.docIntelligence import extractContent
from services.commons.gptCall import invoiceAnalysis,extractInvoice
from services.commons.dbcalls import Invoice,Contract
from services.constants.enums import values,color
import altair as alt
from millify import millify



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
            def top_kpis():
                st.write("")
                st.write("")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Contractors:", f"🤵 {millify(len(df1['contractorName'].unique()))}", border=True)
                with col2:
                    st.metric("Average Working Hours:", f"⌛ {millify(df1['hours'].mean())}", border=True)
                with col3:
                    st.metric("Total Amount:", f"💲 {millify(df1['amount'].sum())}", border=True)
            
            top_kpis()
            df = df1.groupby('contractorName')[['hours', 'amount']].sum().assign(entries=df1.groupby('contractorName').size())
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

            tabs=st.container(border=True)

            tab1, tab2 = tabs.tabs(["Employee Recevied Amount", "Employee Working Hours Trend"])

            with tab1:
                # Use the Streamlit theme.
                # This is the default. So you can also omit the theme argument.
                st.altair_chart(chart, theme="streamlit", use_container_width=True)
            with tab2:
                # Use the native Altair theme.
                st.altair_chart(chart1, theme="streamlit", use_container_width=True)


            def role_pie_chart():
                
                source=df1.groupby('role')[['amount']].sum().reset_index()


                chart=alt.Chart(source,title="Distribution of amount per Role").mark_arc(innerRadius=50).encode(
                    theta="amount:Q",
                    color="role:N",
                )

                
                st.altair_chart(chart, theme="streamlit", use_container_width=True)

            def top_paid_contractors():


                source=df1.groupby('contractorName')[['amount']].sum().sort_values(by=['amount'], ascending=[False]).head(10).reset_index()

                chart=alt.Chart(source,title="Top 10 paid contractors").mark_bar().encode(
                    x='amount:Q',
                    y=alt.Y('contractorName:N').sort('-x')
                )
                st.altair_chart(chart, theme="streamlit", use_container_width=True)

            # col1,col2=st.columns(2)

            container1=st.container(border=True)
            container2=st.container(border=True)

            with container1:
                role_pie_chart()

            with container2:

                top_paid_contractors()
        else:
            st.header("No Data in invoice")


