import streamlit as st
import time
from services.commons.docIntelligence import extractContent
from services.commons.gptCall import invoiceAnalysis,extractInvoice
from services.commons.dbcalls import Invoice,Contract
from services.constants.enums import values,color



a,b,c=st.columns(3)

with a:
    if st.button("Back",key="secondary"):
        st.switch_page("pages/Contracts.py")

contractId=None

if 'contractId' in st.session_state:
    print("inside")
    contractId=st.session_state.contractId

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

# print("Selected option:",option)



if option is None:
    st.header("Select a Contract to view Invoices")

else:

    
    # Session list
    invList=Invoice.get(contractId=option)

    def changeFile():
        st.session_state.file=True
        # print("File Changed")

    def editContent(ind,obj):
        reason = st.text_input("Edit contract",value=obj["name"])
        if st.button("Save"):
            obj["name"]=reason
            obj=Invoice.update(ind,obj)
        
        

        uploaded_file = st.file_uploader("Choose a Contract file",type=['docx','pdf'],on_change=changeFile)
        
    

        if uploaded_file is not None and st.session_state.file:
            # print("file uploaded",uploaded_file)

            rule=Contract.get(i=obj["contract_id"])["rules"]
            # print("The Rule:",rule)
            with st.status("Uploading Invoice content...", expanded=False) as status:
                st.write("Uploading the Invoice")
                data=uploaded_file.getvalue()


                status.update(
                    label="Extracting invoice content", state="running",expanded=False
                )
                st.write("Extracting invoice content")
                content=extractContent(data)
                obj["content"]=content

                status.update(
                    label="Extracting Employee Data", state="running",expanded=False
                )
                st.write("Extracting Employee Data")
                
                obj["employeeData"]=extractInvoice()


                status.update(
                    label="Analysing the invoice", state="running",expanded=False
                )
                st.write("Analysing the invoice")

                anomalies=invoiceAnalysis(rule,content)
                obj["anomalies"]=anomalies


                status.update(
                    label="Process complete!", state="complete",expanded=False
                )
                obj["status"]=values.SUCCESS
                # print("Before updating")
                Invoice.update(i=ind,obj=obj)
                st.session_state.file=False
            
        if st.button("Close"):
            st.rerun()

        



    
    # Updating the session list

    def on_list_change():
        st.session_state.invlist=list

    # Adding the invoice

    @st.dialog("Add Invoice")
    def add():
       
        if st.session_state.edit is False:
            reason = st.text_input("Invoice Name")
            


            if st.button("save"):
                obj={
                "id":89,
                "name":reason,
                "status":values.PENDING.value,
                "content":None,
                "contract_id":option,
                "anomalies":[],
                "employeeData":None
            }
                ind=Invoice.create(obj)
                on_list_change()
                st.session_state.edit=True
                st.session_state.edit_item=ind
                st.rerun(scope="fragment")
        else:
            # print("Inside else")
            obj=Invoice.get(i=st.session_state.edit_item)
            editContent(st.session_state.edit_item,obj)
        
    def downloadData(i):
        df=Invoice.get(i=i)["employeeData"]
        csv=df.to_csv(index=False).encode('utf-8')
        invoiceName=str(Invoice.get(i=i)["name"])+'.csv'

                # Different ways to use the API
        b,c=st.columns([1,3],gap="large")
        c.download_button('Download Invoice Data', csv,invoiceName, 'text/csv',icon=":material/download:",use_container_width=True)
    
    @st.dialog("Results")
    def results(ind):
        anomalies=Invoice.get(i=ind)["anomalies"]

        downloadData(ind)
        
        st.write("Anomalies found:")
        for i in anomalies:
            container = st.container(border=True)
            container.write(i)
        



    def delete(indx):
        # print(list,indx)
        Invoice.delete(i=indx)
        st.rerun()


    # Editing the Invoice 

    st.header(f"Invoices")
    addbtn=st.button("Add an Invoice", type="primary",disabled=Contract.get(i=option)["status"]!=values.SUCCESS.value)

    if invList: 
        grid=[]

        # Creating Empty Grid
        for i in range((len(invList)//3)+1):
            row=st.columns(3)
            grid.extend(row)

        
        # Filling Empty Grids
        for i in range(len(invList)):
            col=grid[i]
            
            with col.container(border=True,height=None):
                
                    c1,c2=st.columns([3,1],gap="small")
                    c1.subheader(invList[i]["name"])
                    c2.button(color[values(invList[i]["status"]).name].value,help="Processing "+values(invList[i]["status"]).name,key=i,type="tertiary")
                    st.write("")
                    st.write("")
                    st.write("")
                    
                    b,c=st.columns([3,1],gap="small")
                
                    if b.button('View/Edit',type="secondary",key='v'+str(i),use_container_width=True):
                            # print("editing")
                            st.session_state.edit_item=invList[i]["actualInd"]
                            st.session_state.edit=True
                            add()
                    if c.button(":material/delete:",key=str(i)+'del'):
                        delete(invList[i]["actualInd"])
                    
                    if st.button("Results",key="an"+str(i),disabled=invList[i]["status"]!=values.SUCCESS):
                        results(invList[i]["actualInd"])

    if addbtn:
        st.session_state.edit=False
        add()