import duckdb 
import pandas as pd
from io import StringIO

def call_duckdb(query):
    df = pd.read_csv(r'C:\Users\srihari.nadakuditi\Downloads\invoice 5359385.csv')
    print(query)
    res = duckdb.query(query).df()
    if len(res)>1:
        csv_result = res.to_csv(index=False) 
        print("Query executed successfully. CSV result generated.")
    else:
        csv_result = "No results found for the query."
    
    return csv_result
    
  
    

