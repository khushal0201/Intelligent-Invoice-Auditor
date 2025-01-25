

import json
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


        if len(context)!=0:

            assistantReply={
                "role":"assistant",
                "content":'last processed record: '+json.dumps(context)
            }


            chat_prompt+=[assistantReply]
            print("Added")

        print("prompt val",repr(chat_prompt))
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
        print("parsed Value:",val["parsed"])
        parsed=val["parsed"]["anomalies"]

        return parsed



def extractInvoice(content):
    cont=1
    count=0
    results=[]
    lastData=[]
    while cont==1:
       
        prompt=EmployeeData()

        val=GPTCall(prompt,lastData,content,type="extract")
        print("parsed employee",val)

        employees=val["parsed"]["contractor"]
        cont=int(val["parsed"]["continue_"])
        lastData=employees[-2:]
        print("lastData",lastData)
        results.extend(employees)
        print("continue val:",cont)

        count+=1

    employeeDF=pd.DataFrame(results)
    print(employeeDF)
    return employeeDF

       



