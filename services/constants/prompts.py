

def contract():


#         return """

# Please analyze the provided contract and extract the rules related to the following categories:

# Time-Related Violations:

# Maximum daily work hours allowed (e.g., 12-hour limit).
# Valid time increments for logging work (e.g., 0.5-hour increments).
# Restrictions on weekend work.
# Work on public holidays and any restrictions related to it.
# Rate-Related Violations:

# Rules regarding the correct rates for roles (e.g., Senior Software Architect with 10+ years should be $1,200/day, $180/hour).
# Guidelines for role assignments and restrictions on unauthorized assignments.
# Rate card mismatches and what constitutes a valid rate for a specific role.
# Compliance Violations:

# Requirements for project codes and whether they need to be specified.
# Necessity of approval signatures and who must approve.
# Rules regarding valid project assignments.
# Role-Based Rules:

# Extract rules for each role mentioned in the contract (e.g., Senior Software Architect with 10+ years should be compensated at $1,200/day or $180/hour).
# Include rules related to years of experience, specific rates tied to roles, and any additional role-based qualifications or requirements.
# Ensure that the role's corresponding rates, experience levels, and any other restrictions related to the role are clearly summarized.
# Please provide a clear summary of each rule under the appropriate category, ensuring that role-based rules (including compensation, experience, and other relevant criteria) are always extracted.
# """

    return """

Please extract and list the following precise rules from the contract, ensuring the rate card is included for all roles:

Time-Related Violations:

Maximum daily work hours: (e.g., 12 hours).
Time increments for logging work: (e.g., 0.5 hours).
Weekend work restrictions: (e.g., no work without approval).
Public holiday work: (e.g., additional compensation required).

Rate-Related Violations:

Correct rates for roles: (e.g., Senior Software Architect with 10+ years: $1,200/day or $180/hour).
Role assignments: (e.g., unauthorized assignments are not allowed).
Rate card mismatches: (e.g., exceeding agreed rate is a violation).
Include the full rate card for each role and the specific rates outlined in the contract.

Compliance Violations:

Project code requirement: (e.g., must specify project code for all tasks).
Approval signatures: (e.g., project manager approval needed).
Project assignment validity: (e.g., must be assigned to correct project code).

Role-Based Rules:

Compensation per role: (e.g., Senior Software Architect: $1,200/day or $180/hour).
Experience requirement: (e.g., 10+ years for Senior Software Architect).
Additional qualifications: (e.g., Certification required for Scrum Master).
Include the rate card detailing compensation for all roles.


"""

def invoice(rules):
    
#     return f""" Given a contract ruleset, Findout the anomalies in the invoice provided,
#              Anomalies are like exceeding what is in the rule(Wage, worktime any kind of PAY) or not following the Contract rules.

#              List out all anomalies found in invoice including incorrect rates and hours and others

#              ``Include all anomalies detected, do not give an overview, give details``

#              ``Give Priority to finding role based amount anomalies``

#              ``Find Anomalies with EMPLOYEE level GRANULARITY``

#              Mention the differences in numerical values also 

#              Here are the contract rules:
#              {rules}
             
#              If response is incomplete then fill conitnue_ as 1 , if complete then 0

#              If no anomalies found then the anomalies array should be empty otherwise fill

#              Give response in this JSON format:
             
#              {{anomalies:[string list of anomalies],continue_:1/0}}

             
# """
    
        return f"""
.Given the contract ruleset (provided dynamically in the system), prioritize and identify any anomalies in the provided invoice (provided in the user prompt). Focus on detecting violations in the following order of priority:

1. **Exceeded Daily Hours** (Highest Priority):
   - Flag any invoice where a day's hours exceed the **daily hours limit** as specified in the contract ruleset.
   - Example: If the contract specifies a **maximum of 12 hours per day**, and John Smith logged 14 hours in one day, it should be flagged as a violation.
    **Do not flag** entries individually based on their **per-entry hours** if the total hours for that day are below the limit. Instead, check the **total hours for the same day across all entries for that employee**.
    
2. **Rate Mismatch** (Second Priority):
   - Flag invoices with an **incorrect rate** for the role (e.g., a rate that doesn’t match the contract rate for the specified role as provided in the contract ruleset).
   - Example: If the contract rate for a **Security Engineer** is $142/hour, and Sarah Johnson is billed at $150/hour, it should be flagged as a violation.

3. **Time-Related Violations** (Third Priority):
   - **Invalid time increments**: Hours must be logged in **0.5-hour increments**. Flag any entry that doesn’t follow this rule.
     - Example: "Alex Turner's time is logged in 0.3-hour increments (Contract requires 0.5-hour increments)."
   - **Unauthorized weekend work**: Flag work on weekends unless **pre-approval** is documented.
     - Example: "Emily Davis worked on a Sunday without documented pre-approval."
   - **Work on public holidays**: Flag work logged on public holidays unless **pre-approval** is documented.
     - Example: "Michael Chen worked on a public holiday without pre-approval."

4. **Compliance Violations** (Lowest Priority):
   - **Missing project code**: Flag if the project code is missing or incorrect.
     - Example: "Michael Chen's entry is missing a required project code."
   - **Missing approval signatures**: Flag if approval signatures are absent.
     - Example: "John Smith's timesheet is missing approval signatures."
   - **Invalid project assignments**: Flag if the project assigned is not part of the contract.
     - Example: "Sarah Johnson's time is logged under an unapproved project."

### Contract Ruleset (Dynamic Input):
 {rules}

**Role-Based Violations:**
- For each role (e.g., **Security Engineer, DevOps Engineer, etc.**), refer to the **contract ruleset** to check for any **rate violations**. The role-based rate for each job title must be **correctly applied** based on the contract.

### User Prompt (Invoice Data):
- The invoice data will be provided in the **user prompt** and should be processed according to the contract ruleset.

### Output Requirements:
- **Only report valid anomalies** based on the provided ruleset. Do **not generate false anomalies** (such as formatting errors or irrelevant issues that are not part of the contract rules).
- The anomalies must be reported in **priority order** as follows:
  1. **Exceeded daily hours** (must come first).
  2. **Rate mismatch** (must come second).
  3. **Time-related violations** (third priority).
  4. **Compliance violations** (last priority).
  
- For each anomaly, provide numerical discrepancies where applicable (e.g., actual vs. expected rates, hours, amounts).
- If **all anomalies** have been reported, set `"continue_"` to **0**.
- If more anomalies **remain to be reported** in subsequent API calls, set `"continue_"` to **1**.

### Output Format:
{{
    "anomalies": ["list of detected anomalies"],
    "continue_": 1 or 0
}}
        """



def EmployeeData():

#     return """
    
#         Given an invoice from Contractor to Client 

#         Fetch out Contractor data in this format :

#         contractorName	role	projectCode	description	date	hours	rate	amount

#         Example(May or maynot part of Invoice ): 

#             Mr. Derrick Ward	UX/UI Designer	PRJ004	bypass solid state driver	2025-01-12T11:25:03.822Z	8	120	960

        
#         Put All the details of Employees, fix the empty columns with suitable value and respond

        

        
#         If complete response is sent then fill continue_ as 0 otherwise 1
        
#         return in this JSON format:

#         {{contractor:[{{contractorName:'',role:'',projectCode:'',description:'',date:'',hours:'',rate:'',amount:''}}],continue_:1/0}}

        






# """

    return """
        Given an invoice from Contractor to Client, extract the contractor's details in the following format:

contractorName, role, projectCode, description, date, hours, rate, amount

Instructions:
Extract All the Contractor Details: For each contractor listed in the invoice, extract the details such as name, role, project code, description, date, hours, rate, and amount.

Handle Missing Contractor Names: If a contractor's name is missing in a record, and the contractor's name was provided in the previous record, fill the missing contractorName from the previous record. If the first record is missing a name, fill it with N/A or leave it as empty, but ensure consistency for subsequent records.

Multiple Projects for Same Contractor: If a contractor has multiple projects listed under their name, ensure that all records are extracted, and each project gets its own entry with the contractor's name. All columns should be filled with appropriate values. If any value is missing or incomplete, replace it with suitable values (e.g., N/A, 0, null if applicable).

Final Record Status (continue_ field):

Set continue_ to 1 if there are more contractor records to be extracted (i.e., there is still missing data or additional contractor records that need to be processed).
Set continue_ to 0 when all contractor records have been fully extracted and no more data is missing or left to process.
Example:
Given the following random invoice data with missing contractor names and data to be processed, the extraction should look like this:

John Doe Senior Developer PRJ001
design scalable system 11/15/2024 6 $140 $840.00
PRJ002
build responsive website 11/20/2024 5 $130 $650.00
PRJ003
optimize database queries 12/05/2024 8 $150 $1200.00
PRJ004
implement security patch 12/15/2024 7 $155 $1085.00
PRJ002
create API documentation 1/10/2025 7 $160 $1120.00
Jane Smith Project Manager PRJ003
organize team meeting 12/01/2024 3 $120 $360.00
PRJ002
prepare project proposal 12/12/2024 6 $125 $750.00


Here’s how the extracted data should look with the proper handling of continue_ and missing contractor names:

{
  "contractor": [
    {
      "contractorName": "John Doe",
      "role": "Senior Developer",
      "projectCode": "PRJ001",
      "description": "design scalable system",
      "date": "2024-11-15T00:00:00.000Z",
      "hours": "6",
      "rate": "140",
      "amount": "840.00"
    },
    {
      "contractorName": "John Doe",
      "role": "Senior Developer",
      "projectCode": "PRJ002",
      "description": "build responsive website",
      "date": "2024-11-20T00:00:00.000Z",
      "hours": "5",
      "rate": "130",
      "amount": "650.00"
    },
    {
      "contractorName": "John Doe",
      "role": "Senior Developer",
      "projectCode": "PRJ003",
      "description": "optimize database queries",
      "date": "2024-12-05T00:00:00.000Z",
      "hours": "8",
      "rate": "150",
      "amount": "1200.00"
    },
    {
      "contractorName": "John Doe",
      "role": "Senior Developer",
      "projectCode": "PRJ004",
      "description": "implement security patch",
      "date": "2024-12-15T00:00:00.000Z",
      "hours": "7",
      "rate": "155",
      "amount": "1085.00"
    }
  ],
  "continue_": 1
}

Explanation:
Partial Data Extraction: Only the records for John Doe up to PRJ004 are provided. The records for Jane Smith are missing in this response, so this is an incomplete data extraction.

continue_: 1: Since there are more contractor records (for Jane Smith), the response is incomplete, and the continue_ is set to 1, indicating that the data extraction is not yet finished and that more data will follow in subsequent API calls.


Second API Call (to complete the extraction):
In the subsequent API call, the remaining records for Jane Smith would be returned to complete the data extraction.

{
  "contractor": [
    {
      "contractorName": "Jane Smith",
      "role": "Project Manager",
      "projectCode": "PRJ003",
      "description": "organize team meeting",
      "date": "2024-12-01T00:00:00.000Z",
      "hours": "3",
      "rate": "120",
      "amount": "360.00"
    },
    {
      "contractorName": "Jane Smith",
      "role": "Project Manager",
      "projectCode": "PRJ002",
      "description": "prepare project proposal",
      "date": "2024-12-12T00:00:00.000Z",
      "hours": "6",
      "rate": "125",
      "amount": "750.00"
    }
  ],
  "continue_": 0
}
Final Result:
continue_: 0: The continue_ value is set to 0 in the second API call because all contractor data has now been extracted, and there are no more records left to process.
Summary:
continue_: 1 should only be used when the data extraction is incomplete, meaning more data will come in the next API call (i.e., the extraction has been partial).
continue_: 0 indicates that all contractor data has been fully extracted, and no more records are expected.

Additional Notes for Continuing Data Extraction:
When more data is expected, do not repeat records that have already been extracted. Only return the data after the last processed record.
The user will provide the last processed record in each subsequent request. Please continue the extraction based on that provided record. If all records are extracted, return continue_ = 0.

"""
