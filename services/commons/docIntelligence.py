from services.ClientObjects.docint import docClient
from markdownify import markdownify as md
from azure.ai.documentintelligence.models import AnalyzeResult,DocumentContentFormat

def markdown(content):
    return md(content, convert=['table','tr','td','th'])


def extractContent(f):

    poller = docClient.begin_analyze_document("prebuilt-layout", body=f,output_content_format=DocumentContentFormat.MARKDOWN)
    invoices: AnalyzeResult = poller.result()
    result=invoices
    datatr = result.content
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(datatr)
    return markdown(result.content)
