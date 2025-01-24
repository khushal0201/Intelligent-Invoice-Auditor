from services.ClientObjects.docint import docClient
from markdownify import markdownify as md
from azure.ai.documentintelligence.models import AnalyzeResult,DocumentContentFormat


def markdown(content):
    return md(content, convert=['table','tr','td','th'])


def extractContent(f):

    poller = docClient.begin_analyze_document("prebuilt-layout", body=f,output_content_format=DocumentContentFormat.MARKDOWN)
    invoices: AnalyzeResult = poller.result()
    result=invoices
    return markdown(result.content)
