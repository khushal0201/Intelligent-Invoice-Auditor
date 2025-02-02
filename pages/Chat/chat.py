from pages.Chat.apiCallHandler import gptCall,appendUser,appendAssistant,summaryCall,contractCall
from pages.Chat.customCSS import cssLoad
from DuckDb.duckdb import call_duckdb
from services.commons.dbcalls import Invoice,Contract
import streamlit as st
import json
import time
# st.title("hey")


def removeMsgs():
    st.session_state.messages=[]

def stream_string(text: str, chunk_size: int = 1):
    """Split a string into chunks to simulate streaming."""
    for i in range(0, len(text), chunk_size):
        yield text[i : i + chunk_size]
        # Optional: Add a small delay to mimic real streaming
        time.sleep(0.001)

a,b,c=st.columns(3)

cssLoad()
contractId=None

with a:
    if st.button("Back",key="secondary"):
        st.switch_page("pages/Contracts.py")

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
    label_visibility="collapsed",
    on_change=removeMsgs
)

if option is None:
    st.subheader("Select a Contract to chat")

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
        label_visibility="collapsed",
        on_change=removeMsgs
    )
    if "messages" not in st.session_state:
            st.session_state.messages = []
            
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):  
            st.markdown(message["content"])
    
    

    if option1 is None:

        # HANDLING The CONTRACT CHAT

        def assistantCall():
            contractData=Contract.get(i=option)["rules"]
            response = contractCall(st.session_state.messages[-5:],contract=contractData,stream=True)
            
            return response



        if len(st.session_state.messages)==0:
            with st.chat_message("assistant"):
                response=assistantCall()
                st.write_stream(stream_string(response))
                appendAssistant(response)

        if prompt := st.chat_input("Chat Normally or ask regarding Contract, or Select an Invoice"):
            # st.session_state.messages.append({"role": "user", "content": prompt})
            appendUser(prompt)
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                
                response=assistantCall()  
                st.write(response) 


            appendAssistant(response)

        

        

    else:

        # Handling the INVOICE CHAT
        # df=Invoice.get(i=)["employeeData"]
        ind=invList[option1]["actualInd"]


        def assistantCall():
            parsed_response = gptCall(st.session_state.messages[-5:],stream=True)
            chat=parsed_response.out_of_context_text
            query=parsed_response.query
            needs_query=parsed_response.needs_query
            return chat,query,needs_query



        if len(st.session_state.messages)==0:
            with st.chat_message("assistant"):
                chat,query,needs_query=assistantCall()
                st.write_stream(stream_string(chat))
                appendAssistant(chat)



        if prompt := st.chat_input("Chat Normally or ask queries regarding Invoice"):
            # st.session_state.messages.append({"role": "user", "content": prompt})
            appendUser(prompt)
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                
                chat,query,needs_query=assistantCall()
                
                try:
                            
                    if needs_query:
                        query_res = call_duckdb(query,index=ind)
                        
                        # make the other llm call here 
                        user_query=prompt
                        response=summaryCall(prompt,query_res)
                    else:
                        response=chat
                    
                    st.write_stream(stream_string(response))


                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                except KeyError as e:
                    print(f"Missing expected key in the response: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

            appendAssistant(response)