import duckdb 
import pandas as pd
from io import StringIO
from services.commons.dbcalls import Invoice

def call_duckdb(query,index):
    df = Invoice.get(i=index)["employeeData"]
    print(df.head(5))
    print(query)
    res = duckdb.query(query).df()
    print(res)
    if len(res)>=1:
        csv_result = res.to_csv(index=False) 
        print("Query executed successfully. CSV result generated.")
    else:
        csv_result = "No results found for the query."
    
    return csv_result
    
  
    

