import json
import re
from services.ClientObjects.gptsdk import gptClient,deployment
from services.constants.prompts import contract,invoice,EmployeeData
from pydantic import BaseModel
import pandas as pd

class invoiceCheck(BaseModel):
        anomalies:list[str]
        continue_:int

class contractor(BaseModel):
       contractorName:str
       role:str
       projectCode:str
       description:str
       date:str
       hours:int
       rate:float
       amount:float

class invoiceStructure(BaseModel):

        contractor:list[contractor]
        continue_:int


def GPTCall(prompt,context,content,type="contract"):

        chat_prompt = [
                    {
                        "role": "system",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt
                            }
                        ]
                    }]
                
                    
        

        # Adding the actual content:


        chat_prompt+=[
                {
                        "role":"user",
                        "content":[{
                                "type":"text",
                                "text":content
                        }]
                }
        ]

        # Adding the Context

        context = context if context is not None else ""
        
        if len(context)!=0:

            assistantReply={
                "role":"assistant",
                "content":'last processed record: '+json.dumps(context)
            }


            chat_prompt+=[assistantReply]
            # print("Added")

        # print("prompt val",repr(chat_prompt))
        if type=="contract":
            completion_json = gptClient.chat.completions.create(  
                        model=deployment, 
                        # response_format={ "type": "json_object" },
                        messages=chat_prompt,  
                        max_tokens=15000,  
                        temperature=0.7,  
                        top_p=0.95,  
                        frequency_penalty=0,  
                        presence_penalty=0,  
                        stop=None,  
                        stream=False
                    )
        else:
             completion_json = gptClient.beta.chat.completions.parse(  
                        model=deployment, 
                        response_format=invoiceCheck if type=="invoice" else invoiceStructure,
                        messages=chat_prompt,  
                        max_tokens=15000,  
                        temperature=0.7,  
                        top_p=0.95,  
                        frequency_penalty=0,  
                        presence_penalty=0,  
                        stop=None
                    )  
             

                
                

        return json.loads(completion_json.to_json())['choices'][0]['message']


def contractAnalysis(content):
        
        prompt=contract()

        return GPTCall(prompt,[],content,"contract")['content']
        

def invoiceAnalysis(rules,content):
        

        prompt=invoice(rules)

        val=GPTCall(prompt,[],content,"invoice")
        # print("parsed Value:",val["parsed"])
        parsed=val["parsed"]["anomalies"]

        return parsed


def extractInvoice():
    
    #preprocess
    with open('output.txt', 'r', encoding='utf-8') as file:
    # Read the entire content of the file
        content = file.read()
    
    # print(f"conent {content}")
    data_rows_tr = re.findall(r'<tr.*?>(.*?)</tr>', content, re.DOTALL)
    data_rows_tr = ['<tr>' + tr + '</tr>' for tr in data_rows_tr]
    # print(f"after processing {data_rows_tr}")
    
    results = []
    last_data = None
    batch_size = 10  # We will process 10 rows at a time
    
    # Process the content in batches of 10
    for i in range(0, len(data_rows_tr), batch_size):
        batch = data_rows_tr[i:i+batch_size]
        
        # Join all <tr> tags with a comma between them to form the batch content
        batch_content = ','.join(batch)
        # print(f"total length: {len(data_rows_tr)}")
        # print(f"batch: {batch_content}")
        
        prompt = f"{EmployeeData()}"
        val=GPTCall(prompt,last_data,batch_content,type="extract")
        # print("parsed employee",val)
        print(f"values: {val}")
        employees=val["parsed"]["contractor"]
        last_data=employees[-2:]

        results.extend(employees)
        print("Count of results:", len(results))
        print(i)

    employeeDF=pd.DataFrame(results)
    employeeDF = employeeDF[(employeeDF['hours'] != 0) & (employeeDF['rate'] != 0) & (employeeDF['amount'] != 0)]
    employeeDF = employeeDF.ffill()
    employeeDF = employeeDF.drop_duplicates(subset=['contractorName', 'role','projectCode','hours','rate','amount'])
    print(employeeDF)
    
    
    return employeeDF
