import streamlit as st



st.title("Welcome to Invoice Auditor")

addbtn=st.button("Add a Contract", type="primary")

if 'list' not in st.session_state:
    list=[]
    st.session_state.list=list

list=st.session_state.list


def on_list_change():

    st.session_state.list=list





@st.dialog("Add todo")
def add():
    # st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Enter todo")
    if st.button("submit"):
       list.append(reason)
       on_list_change()
       st.rerun()

@st.dialog("Edit todo")
def edit(ind):
    # st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Enter todo",value=list[ind])
    if st.button("submit"):
       list[ind]=reason
       on_list_change()
       st.rerun()



def delete(indx):
    # print(list,indx)
    del list[indx]
    on_list_change()
    st.rerun()

if addbtn:
      add()

if list: 
    st.write("Contract list:")
    grid=[]
    for i in range((len(list)//3)+1):
        row=st.columns(3)
        grid.extend(row)

    

    for i in range(len(list)):
        col=grid[i]
        
        with col.container(border=True,height=230):
               
                
                st.subheader(list[i])
                st.write("")
                st.write("")
                st.write("")
                btnclk=st.button('View Invoices',type="primary",key='v'+str(i))
                if btnclk:
                    st.switch_page("todonested.py")
                b,c,d,e=st.columns([1,1,1,1],gap="small")
            
                if b.button(":material/edit:",key=str(i)+'edit'):
                    edit(i)
                if c.button(":material/delete:",key=str(i)+'del'):
                    delete(i)
       
