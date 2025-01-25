import streamlit as st
import time
from services.commons.docIntelligence import extractContent
from services.commons.gptCall import contractAnalysis
from services.commons.dbcalls import Contract
from services.constants.enums import values,color
from dialogBoxes.rulesDialog import rule_dialog



# Initializing the list via Session cuz no DB

if 'list' not in st.session_state:
    list=[]
    st.session_state.list=list

list=st.session_state.list
contractList=Contract.get()
st.session_state.name=False

# Updating the Session List or DB


# print("rerun")
def on_list_change():
    print("list update",list)
    st.session_state.list=list





def changeFile():
        st.session_state.file=True
        print("File Changed")
    
def changeText():
        st.session_state.name=True
        print("File Changed")


def editContent(i,obj):
    reason = st.text_input("Edit contract",value=obj["name"],on_change=changeText)
    print("e run",i)

    if st.button("Save",disabled= not st.session_state.name):
            obj["name"]=reason
            obj=Contract.update(i,obj)
            st.session_state.name=False



    uploaded_file = st.file_uploader("Choose a Contract file",type=['docx','pdf'],on_change=changeFile)

   

    if uploaded_file is not None and st.session_state.file==True:
        print("file uploaded",uploaded_file)

        with st.status("Processing the Contract...", expanded=True) as status:
            st.write("Uploading the contract")
            data=uploaded_file.getvalue()
            
            st.write("Analysing the Contract")
            content=extractContent(data)

            obj["content"]=content

            st.write("Creating Rule Prompt")
            rules=contractAnalysis(content)
            obj["rules"]=rules


            status.update(
                label="Process complete!", state="complete",expanded=True
            )
            obj["status"]=values.SUCCESS.value

            Contract.update(i,obj)
            st.session_state.file=False
        # st.write(f"Rules:{rules}")
    if st.button("close"):
            st.rerun()



    


# Dialog Box Code

@st.dialog("Add contract")
def add():
    # st.write(f"Why is {item} your favorite?")

    if st.session_state.edit is False:
        reason = st.text_input("Contract Name",on_change=changeText)
        


        if st.button("save",disabled = not st.session_state.name):
            obj={
                "id":89,
                "name":reason,
                "status":values.PENDING.value,
                "content":None,
                "rules":None
            }
            itemVal=Contract.create(obj)
            on_list_change()
            st.session_state.edit=True
            st.session_state.name=False
            st.session_state.edit_item=itemVal
            st.rerun(scope="fragment")

    else:
        obj=Contract.get(i=int(st.session_state.edit_item))
        editContent(int(st.session_state.edit_item),obj)
    
    # processing()
    
    


@st.dialog("Edit contract")
def edit(ind):
    # st.write(f"Why is {item} your favorite?")

    obj=Contract.get(i=ind)
    print("obj:",obj)
    editContent(ind,obj)


def delete(indx):
    # print(list,indx)
    Contract.delete(indx)
    st.rerun()








# Actual UI Code

# Page Title


st.title("Welcome to Invoice Auditor")

# Add A Contact Button 

addbtn=st.button("Add a Contract", type="primary")


if contractList: 
    st.write("Contract list:")
    grid=[]

    # Creating Empty Grid
    for i in range((len(contractList)//3)+1):
        row=st.columns(3)
        grid.extend(row)

    
    # Filling Empty Grids
    for i in range(len(contractList)):
        col=grid[i]
        
        with col.container(border=True):
               
                c1,c2=st.columns([3,1],gap="small")
                c1.subheader(contractList[i]["name"])
                c2.button(color[values(contractList[i]["status"]).name].value,help="Processing "+values(contractList[i]["status"]).name,key=i,type="tertiary")
                st.write("")
                st.write("")
                st.write("")
                btnclk=st.button('View Invoices',type="secondary",key='v'+str(i))
                if btnclk:
                    st.session_state.contractId=i
                    st.switch_page("pages/Invoices.py")
                b,c,d=st.columns([1,1,2],gap="small")
            
                if b.button(":material/edit:",key=str(i)+'edit',type="secondary"):
                    edit(i)
                if c.button(":material/delete:",key=str(i)+'del',type="secondary"):
                    delete(i)
                
                if d.button("Rules",key=str(i)+"rule",type="secondary",disabled=contractList[i]["status"]!=values.SUCCESS.value):
                     
                    rule_dialog(i)

       

if addbtn:
      st.session_state.edit=False
      add()