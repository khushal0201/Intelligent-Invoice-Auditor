from openai import AzureOpenAI  
import streamlit as st

subkey=st.secrets.gpt.key
endpoint = st.secrets.gpt.endpoint
deployment = st.secrets.gpt.deployment
subscription_key = subkey  



@st.cache_resource
def init_connection():
    return AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=subscription_key,  
    api_version="2024-10-21",  
    )

gptClient = init_connection()