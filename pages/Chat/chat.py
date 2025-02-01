from pages.Chat.apiCallHandler import gptCall,appendUser,appendAssistant
from pages.Chat.customCSS import cssLoad
from DuckDb.duckdb import call_duckdb
import streamlit as st
import json
# st.title("hey")

def firstAssistantCall():
    value=gptCall(st.session_state.messages,stream=True)
    response=st.write_stream(value)
    appendAssistant(response)


cssLoad()

if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):  
        st.markdown(message["content"])

if len(st.session_state.messages)==0:
    with st.chat_message("assistant"):
        firstAssistantCall()



if prompt := st.chat_input("Chat Normally or Select Invoice / Contract to get more details"):
    # st.session_state.messages.append({"role": "user", "content": prompt})
    appendUser(prompt)
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        
        session_msgs=st.session_state.messages
        stream = gptCall(session_msgs[-5:],stream=True)
        response = st.write_stream(stream)
        try:
            response = response.lstrip('```json').rstrip('```')
            
            
            r = json.loads(response)
            
           
            if r['needs_query']:
                query_res = call_duckdb(r['query'])
                print(query_res)
                # make the other llm call here 
            else:
                print(r['out_of_context_text'])

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except KeyError as e:
            print(f"Missing expected key in the response: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

            
    appendAssistant(response)