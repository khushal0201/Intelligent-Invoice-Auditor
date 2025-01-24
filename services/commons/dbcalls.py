
from JSONdata.contracts import contracts as cdata
from JSONdata.invoices import invoices as idata


print("re rerunning the db calls")

class Contract:

    def get(i=None,limit=100):

        if i is not None: 
            print("here in i")
            return cdata[i]
        
        return cdata[:limit]

    def update(i,obj,limit=100):
        
        cdata[i]=obj
        print("Updated list",cdata)

        return obj


    def delete(i):

        del cdata[i]

    def create(obj):
        
        cdata.append(obj)

        return len(cdata)-1          



class Invoice:


    def get(contractId=None,i=None,limit=100):

        
        if contractId is not None:

            val=list(filter(lambda x:x["contract_id"]==contractId,map(lambda x: {**x[1],"actualInd":x[0]},enumerate(idata))))
            print("contractId",contractId)
            print("Filtered invoices:",val)
            return val
        
        
        if i is not None:
                val=idata[i]
                val["actualInd"]=i
                return val
        
        
        return idata[:limit]

    def update(i,obj,limit=100):
        
        idata[obj["actualInd"]]=obj


        print("Updated idata:",idata)
        return obj


    def delete(i):

        del idata[i]

    def create(obj):
        
        idata.append(obj)

        return len(idata)-1              
