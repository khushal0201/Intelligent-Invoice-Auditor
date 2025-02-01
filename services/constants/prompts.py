

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
        1. Extract data from each HTML table row (<tr>). Each row contains details in table cells (<td>).
        2. Handle missing contractor names:
           - If a row is missing the contractor name, use the name from the previous row in the current batch.
           - Handle Missing Contractor Names: If a contractor's name is missing in a record, and the contractor's name was provided in the previous record, fill the missing contractorName from the previous record. If the first record is missing a name, fill it with N/A or leave it as empty, but ensure consistency for subsequent records.
        3. Each project must be a separate entry. Use 'N/A' for missing text, '0' for missing numbers.

Example:
Given the following random invoice data with missing contractor names and data to be processed, the extraction should look like this:

<tr><td>John Doe</td><td>Senior Developer</td><td>PRJ001</td><td>design scalable system</td><td>11/15/2024</td><td>6</td><td>$140</td><td>$840.00</td></tr>,
<tr><td>PRJ002</td><td>build responsive website</td><td>11/20/2024</td><td>5</td><td>$130</td><td>$650.00</td></tr>,
<tr><td>PRJ003</td><td>optimize database queries</td><td>12/05/2024</td><td>8</td><td>$150</td><td>$1200.00</td></tr>,
<tr><td>PRJ003</td><td>optimize database queries</td></tr>,
<tr><td>12/05/2024</td><td>8</td><td>$150</td><td>$1200.00</td></tr>,
<tr><td>PRJ004</td><td>implement security patch</td><td>12/15/2024</td><td>7</td><td>$155</td><td>$1085.00</td></tr>,
<tr><td></td><td></td><td></td><td>PRJ004 1/6/2025</td><td>7</td><td>$180</td><td>$1260.00</td></tr>,
<tr><td>Jane Smith</td><td>Project Manager</td><td>PRJ003</td><td>organize team meeting</td><td>12/01/2024</td><td>3</td><td>$120</td><td>$360.00</td></tr>

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
    },
    {
      "contractorName": "John Doe",
      "role": "Senior Developer",
      "projectCode": "PRJ004",
      "description": "implement security patch",
      "date": "2025-1-16T00:00:00.000Z",
      "hours": "7",
      "rate": "180",
      "amount": "1260.00"
    }
  ]
}

Additional Notes for Continuing Data Extraction:
The user will provide the last processed record in each subsequent request. Please refer that also for more context and name of the contractor.



"""
