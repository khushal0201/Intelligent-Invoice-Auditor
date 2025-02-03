from pydantic import BaseModel
from services.ClientObjects.gptsdk import gptClient,deployment
import streamlit as st
from services.constants.prompts import ChatPrompt,summary_generator_prompt,contractPrompt
from pydantic import BaseModel


class invoiceChat(BaseModel):
    needs_query: bool
    out_of_context_text:str
    query:str

def gptCall(messages,stream=True):

    system=ChatPrompt()
        
    msgs=[{
        "role":"system",
        "content":system
    }]

    msgs.extend([
            {"role": m["role"], "content": m["content"]}
            for m in messages
    ])

    print("msgs",msgs)

    stream = gptClient.beta.chat.completions.parse(
                model=deployment,
                messages=msgs,
                max_tokens=5000,
                response_format=invoiceChat,
                temperature=0.7,  
                top_p=0.95,  
                frequency_penalty=0,  
                presence_penalty=0,
                stop=None
            )
    
    print("parsed:",stream.choices[0].message.parsed.out_of_context_text)
    return stream.choices[0].message.parsed


def appendUser(content):
    st.session_state.messages.append({"role": "user", "content": content})


def appendAssistant(content):
    st.session_state.messages.append({"role": "assistant", "content": content})


def summaryCall(query,data):

    system=summary_generator_prompt(query,data)
        
    msgs=[{
        "role":"system",
        "content":system
    }]



    stream = gptClient.chat.completions.create(
                model=deployment,
                messages=msgs,
                max_tokens=5000,
                temperature=0.7,  
                top_p=0.95,  
                frequency_penalty=0,  
                presence_penalty=0,
                stop=None
            )
    
    print("parsed:",stream.choices[0].message.content)
    return stream.choices[0].message.content


def contractCall(messages,contract,stream=True):

    system=contractPrompt(contract)
        
    msgs=[{
        "role":"system",
        "content":system
    }]

    msgs.extend([
            {"role": m["role"], "content": m["content"]}
            for m in messages
    ])

    print("msgs",msgs)

    stream = gptClient.chat.completions.create(
                model=deployment,
                messages=msgs,
                max_tokens=5000,
                temperature=0.7,  
                top_p=0.95,  
                frequency_penalty=0,  
                presence_penalty=0,
                stop=None
            )
    
    print("parsed:",stream.choices[0].message.content)
    return stream.choices[0].message.content
