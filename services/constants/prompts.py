

def contract():

   return """Given a Contract extract rules out of the contract,

       Rules are nothing but a way to validate the invoices given by Contractor on periodic basis,

       Rules Should be detailed that they can find the anomalies within the Invoices,

       the currency should also be included when mentioning the invoice
       
       The role based wages and work hours and other terms MUST be present in rules to validate against invoice via LLM

       `Extract rules in simple Text format , NOT markdown`
       
       So Extract the rules"""


def invoice(rules):
    
    return f""" Given a contract ruleset, Findout the anomalies in the invoice provided,
             Anomalies are like exceeding what is in the rule(Wage, worktime any kind of PAY) or not following the Contract rules.

             List out all anomalies found in invoice including incorrect rates and hours and others

             ``Include all anomalies detected, do not give an overview, give details``

             ``Give Priority to finding role based amount anomalies``

             ``Find Anomalies with EMPLOYEE level GRANULARITY``

             Mention the differences in numerical values also 

             Here are the contract rules:
             {rules}
             
             If response is incomplete then fill conitnue_ as 1 , if complete then 0

             If no anomalies found then the anomalies array should be empty otherwise fill

             Give response in this JSON format:
             
             {{anomalies:[string list of anomalies],continue_:1/0}}

             
"""
    



def EmployeeData():

    return """
    
        Given an invoice from Contractor to Client 

        Fetch out Contractor data in this format :

        contractorName	role	projectCode	description	date	hours	rate	amount

        Example(May or maynot part of Invoice ): 

            Mr. Derrick Ward	UX/UI Designer	PRJ004	bypass solid state driver	2025-01-12T11:25:03.822Z	8	120	960

        
        Put All the details of Employees, fix the empty columns with suitable value and respond

        
        If complete response is sent then fill continue_ as 0 otherwise 1
        
        return in this JSON format:

        {{contractor:[{{contractorName:'',role:'',projectCode:'',description:'',date:'',hours:'',rate:'',amount:''}}],continue_:1/0}}

        






"""

