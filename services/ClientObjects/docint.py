import streamlit as st
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult,DocumentContentFormat
import os 


endpoint = st.secrets.doc.endpoint
key = st.secrets.doc.key



@st.cache_resource
def init_connection():
    return DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key),api_version="2024-11-30")

docClient = init_connection()