import streamlit as st


if st.button("Back",key="secondary"):
    st.switch_page("Todomain.py")

st.title("Welcome to Invoices")
addbtn=st.button("Add an Invoice", type="primary")


list=[]

# print("Out rerun")

@st.dialog("Add Invoice")
def add():
    # st.write(f"Why is {item} your favorite?")
    # print("re run check ")
    reason = st.text_input("Enter Invoice")
    # print("second",reason)
    if st.button("submit"):
    #    print("after submit")
       list.append(reason)
       st.rerun()

if addbtn:
      add()

