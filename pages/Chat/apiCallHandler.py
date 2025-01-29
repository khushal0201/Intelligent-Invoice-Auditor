from pydantic import BaseModel
from services.ClientObjects.gptsdk import gptClient,deployment
import streamlit as st
from services.constants.prompts import ChatPrompt


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

    stream = gptClient.chat.completions.create(
                model=deployment,
                messages=msgs,
                max_tokens=5000,
                temperature=0.7,  
                top_p=0.95,  
                frequency_penalty=0,  
                presence_penalty=0,
                stop=None,  
                stream=stream
            )
    
    return stream


def appendUser(content):
    st.session_state.messages.append({"role": "user", "content": content})


def appendAssistant(content):
    st.session_state.messages.append({"role": "assistant", "content": content})

