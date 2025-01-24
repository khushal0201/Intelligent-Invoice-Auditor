print("re running the cdata")

contracts=[{
        "id":1,
        "name":"contract 1",
        "status":0,
        "content":"Some contract content",
        "rules":""
    },
    {
        "id":2,
        "name":"contract 4",
        "status":1,
        "content":"Some contract content",
        "rules":"""
Rules extracted from the contract:\n\n1. **Contractor Rate Validation**:\n   - Verify that the invoice matches the agreed-upon rates for the contractor type and experience level:\n     - Senior Software Architect: $1,200/day, $180/hour for overtime.\n     - Full Stack Developer: $900/day, $135/hour for overtime.\n     - DevOps Engineer: $950/day, $142/hour for overtime.\n     - Data Scientist: $1,000/day, $150/hour for overtime.\n     - UX/UI Designer: $800/day, $120/hour for overtime.\n     - Quality Assurance Engineer: $750/day, $112/hour for overtime.\n     - Business Analyst: $850/day, $127/hour for overtime.\n     - Project Manager: $1,100/day, $165/hour for overtime.\n     - Security Engineer: $1,050/day, $157/hour for overtime.\n     - Technical Writer: $700/day, $105/hour for overtime.\n\n2. **Rate Adjustments**:\n   - Ensure that annual rate increases do not exceed 5% unless specifically justified by market conditions and mutually agreed in writing.\n\n3. **Invoice Submission Requirements**:\n   - Invoices must be submitted within 5 business days of month-end.\n   - Invoices must include:\n     - Contractor's legal name and address.\n     - Invoice number and date.\n     - Valid Purchase Order number.\n     - Detailed timesheet.\n     - Applicable tax identification numbers.\n     - Banking information for payment processing.\n   - All invoices must be in USD.\n\n4. **Timesheet Validation**:\n   - Timesheet entries must include:\n     - Project code and name.\n     - Detailed work description.\n     - Hours worked in minimum 0.5-hour increments.\n     - Project manager approval signature.\n     - Date of service.\n     - Location of service (on-site or remote).\n\n5. **Payment Terms**:\n   - Payment must be made within 30 days of receipt of a valid invoice.\n   - Client can dispute charges within 15 days of invoice receipt. Disputed charges should not delay payment of undisputed amounts.\n\n6. **Working Hours and Overtime Rules**:\n   - Standard working day: 8 hours (9:00 AM - 5:00 PM local time).\n   - Standard working week: Monday through Friday.\n   - Lunch break: 1 hour (non-billable).\n   - Overtime rates apply to hours worked beyond 8 hours per day.\n   - Maximum billable hours per day: 12 hours.\n   - Weekend work must be pre-approved in writing by the Project Manager.\n   - Holiday work must be pre-approved and is subject to 1.5x the standard rate.\n\n7. **Expense Reimbursement Validation**:\n   - All expenses must be pre-approved in writing.\n   - Expenses over $500 must have senior management approval.\n   - Mileage reimbursement: $0.65 per mile.\n   - Per diem rates: $75/day for approved travel.\n   - Air travel: Economy class for domestic flights, Business class for international flights exceeding 6 hours.\n   - Accommodation reimbursement:\n     - Up to $250/night for major metropolitan areas.\n     - Up to $180/night for other locations.\n   - Original receipts required for all expenses.\n   - Expense reports must be submitted within 30 days.\n\n8. **Overtime and Holiday Work Rules**:\n   - Overtime must be billed only for hours exceeding 8 hours per day.\n   - Weekend and holiday work must be pre-approved in writing.\n   - Holiday work billed at 1.5x the standard rate.\n\n9. **Invoice Format Check**:\n   - Ensure the invoice has the correct formatting and includes all required details as specified under Invoice Submission Requirements.\n\n10. **Approval for Weekend and Holiday Work**:\n    - Verify written approval from the Project Manager for weekend or holiday work billed.\n\n11. **Dispute Handling**:\n    - Ensure disputes are raised within 15 days of invoice receipt and verify that undisputed portions are paid on time.\n\n12. **Currency Validation**:\n    - All amounts in the invoice must be in USD.\n\n13. **Maximum Billable Hours Per Day**:\n    - Ensure that billable hours per day do not exceed 12 hours.\n\n14. **Pre-Approval for Expenses**:\n    - Verify written pre-approval for all expenses, especially those exceeding $500 or involving travel.\n\n15. **Documentation of Travel Expenses**:\n    - Validate that travel expenses include original receipts and adhere to the specified reimbursement limits for mileage, per diem, air travel, and accommodation.\n\n16. **Annual Rate Review**:\n    - Confirm that any rate changes are mutually agreed upon in writing and do not exceed the specified limits unless justified.\n\nBy following these rules, invoices can be validated for accuracy, compliance, and anomalies.
"""        
  },
    {
        "id":1,
        "name":"contract 0",
        "status":0,
        "content":"Some contract content",
        "rules":""
    },
    {
        "id":6,
        "name":"contract 34",
        "status":1,
        "content":"Some contract content",
        "rules":" some rules"
    },
    {
        "id":7,
        "name":"contract 190",
        "status":0,
        "content":"Some contract content",
        "rules":""
    }
]
