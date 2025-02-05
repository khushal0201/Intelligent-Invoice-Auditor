import streamlit as st
from services.commons.dbcalls import Invoice,Contract
from millify import millify
import pandas as pd
import numpy as np




a,b,c=st.columns(3)

with a:
    if st.button("Back",key="secondary"):
        st.switch_page("pages/Contracts.py")
    
contractId=None

if 'contractId1' in st.session_state:
    print("inside")
    contractId=st.session_state.contractId1

# print(" rerun contractId",contractId)

contractList=list(Contract.get())


option = c.selectbox(
    "Select a Contract",
    options=range(len(contractList)),
    index=contractId,
    format_func=lambda x: contractList.__getitem__(x)["name"],
    placeholder="Select Contract",
    label_visibility="collapsed"
)

if option is None:
    st.header("Select a Contract to check accuracy")

else:
    invoiceId=None

    if 'invoiceId' in st.session_state:
        print("inside")
        invoiceId=st.session_state.invoiceId

    invList=Invoice.get(contractId=option)

    option1 = c.selectbox(
        "Select a Invoice",
        options=range(len(invList)),
        index=invoiceId,
        format_func=lambda x: invList.__getitem__(x)["name"],
        placeholder="Select invoice",
        label_visibility="collapsed"
    )
    if option1 is None:
        st.header("Select an invoice to check accuracy")

    else:

        st.header("Accuracy Checker", divider="red")

        accurate_data = st.file_uploader(
            "Choose a CSV file having Accurate Data", accept_multiple_files=False,type=['csv']
        )

        print("accurate data value:",accurate_data)
        if accurate_data is not None:

            with st.spinner('Loading the Dashboard ...'):


                def top_kpis(expected_DF,actual_DF):

                    expected_total_hours = expected_DF["hours"].sum()  # example expected value for total hours
                    actual_total_hours = actual_DF["hours"].sum()    # example actual value for total hours

                    expected_total_records = len(expected_DF)    # example expected value for total rate
                    actual_total_records = len(actual_DF)    # example actual value for total rate

                    expected_total_amount = expected_DF["amount"].sum()  # example expected value for total amount
                    actual_total_amount = actual_DF["amount"].sum()   # example actual value for total amount

                    # Calculate accuracy for each metric
                    accuracy_hours = 1 - abs(expected_total_hours - actual_total_hours) / expected_total_hours
                    accuracy_records = 1 - abs(expected_total_records - actual_total_records) / expected_total_records
                    accuracy_amount = 1 - abs(expected_total_amount - actual_total_amount) / expected_total_amount
                    st.write("")
                    st.write("")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Total Records Accuracy:", f"📃 {accuracy_records*100:.2f} %", border=True)
                    with col2:
                        st.metric("Total Working Hours Accuracy:", f"⌛ {accuracy_hours*100:.2f}%", border=True)
                    with col3:
                        st.metric("Total Amount Accuracy:", f"💲 {accuracy_amount*100:.2f}%", border=True)
            
                

                

                



                def comparisionDF(expected_data, output_data):

                    # Fill NaN in numeric columns with 0 to ensure proper summation
                    numeric_cols = ['hours', 'rate', 'amount']
                    expected_filled = expected_data.copy()
                    expected_filled[numeric_cols] = expected_filled[numeric_cols].fillna(0)
                    output_filled = output_data.copy()
                    output_filled[numeric_cols] = output_filled[numeric_cols].fillna(0)

                    # Aggregate data by contractorName, summing numeric columns
                    expected_agg = expected_filled.groupby('contractorName', as_index=False).agg({
                        'hours': 'sum',
                        'rate': 'sum',
                        'amount': 'sum'
                    })
                    output_agg = output_filled.groupby('contractorName', as_index=False).agg({
                        'hours': 'sum',
                        'rate': 'sum',
                        'amount': 'sum'
                    })

                    # Merge aggregated data to identify discrepancies
                    merged = expected_agg.merge(
                        output_agg,
                        on='contractorName',
                        how='outer',
                        suffixes=('_expected', '_output'),
                        indicator=True
                    )

                    # Initialize error tracking columns
                    merged['Errors'] = ''
                    merged['Visual_Cue'] = ''

                    # Identify contractors missing in output or expected
                    missing_in_output = merged['_merge'] == 'left_only'
                    merged.loc[missing_in_output, 'Errors'] = 'MISSING_IN_OUTPUT'
                    merged.loc[missing_in_output, 'Visual_Cue'] = '🔴 Missing in Output'

                    missing_in_expected = merged['_merge'] == 'right_only'
                    merged.loc[missing_in_expected, 'Errors'] = 'MISSING_IN_EXPECTED'
                    merged.loc[missing_in_expected, 'Visual_Cue'] = '🔴 Missing in Expected'

                    # Check for numeric discrepancies where both exist
                    both_mask = merged['_merge'] == 'both'
                    for col in numeric_cols:
                        expected_col = f'{col}_expected'
                        output_col = f'{col}_output'
                        # Use np.isclose to handle floating point precision
                        mismatch = ~np.isclose(merged[expected_col], merged[output_col], atol=1e-3)
                        # Handle cases where one is NaN (after fillna(0), NaNs are 0)
                        merged.loc[both_mask & mismatch, 'Errors'] += f'|{col.upper()}_MISMATCH'
                        merged.loc[both_mask & mismatch, 'Visual_Cue'] += f'🟡 {col} mismatch '

                    # Clean up error columns
                    merged['Errors'] = merged['Errors'].str.strip('|')
                    merged['Visual_Cue'] = merged['Visual_Cue'].str.strip()

                    # Create final comparison DataFrame
                    comparison_df = merged[[
                        'contractorName',
                        'hours_expected', 'rate_expected', 'amount_expected',
                        'hours_output', 'rate_output', 'amount_output',
                        'Errors', 'Visual_Cue'
                    ]]

                    # Function to style the DataFrame
                    def highlight_cells(row):
                        styles = [''] * len(row)
                        
                        # Highlight missing contractors (Updated to a color visible in dark theme)
                        if 'MISSING' in row['Errors']:
                            styles = [
                                'background-color: #FF4D4D' if 'expected' in col or 'output' in col else ''
                                for col in row.index
                            ]
                        
                        # Highlight numeric mismatches (Updated to a color visible in dark theme)
                        else:
                            for col in numeric_cols:
                                expected_col = f'{col}_expected'
                                output_col = f'{col}_output'
                                if expected_col in row and output_col in row:
                                    if not np.isclose(row[expected_col], row[output_col], atol=1e-3):
                                        idx = row.index.get_loc(output_col)
                                        styles[idx] = 'background-color: #5C6BC0'
                        
                        return styles

                    styled_df = comparison_df.style.apply(highlight_cells, axis=1)
                    return styled_df
                # UI code

                st.write("")
                st.write("")
                st.write("")
                ind=invList[option1]["actualInd"]
                output_data=Invoice.get(i=ind)["employeeData"]
                expected_data = pd.read_csv(accurate_data)
                top_kpis(expected_data,output_data)
                comparedData=comparisionDF(expected_data,output_data)
                st.dataframe(comparedData)