import streamlit as st
import pandas as pd

st.write("")
st.write("This page calculates the accuracy of the model by comparing the output file with the ground truth data.")
st.write("")

# Upload CSV files
file1 = st.file_uploader("Upload Model Output data CSV file", type=["csv"])
st.write("")  # Adds space between the lines
file2 = st.file_uploader("Upload Ground truth data CSV file", type=["csv"])
st.write("")  # Adds space between the lines

# Check if both files are uploaded
if file1 is not None and file2 is not None:
    # Read the uploaded files into dataframes
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Ignore 'description' and 'date' columns if they exist in the files
    columns_to_ignore = ['description', 'date']
    df1 = df1.drop(columns=[col for col in columns_to_ignore if col in df1.columns])
    df2 = df2.drop(columns=[col for col in columns_to_ignore if col in df2.columns])

    # Ensure the columns are in the same order
    if list(df1.columns) != list(df2.columns):
        st.write("")  # Adds space between the lines
        st.error("Column mismatch between files. Please ensure both files have the same structure.")
    else:
        # Initialize a dictionary to store column-wise anomalies
        anomaly_summary = {}

        # Variables to calculate overall anomalies
        total_anomalies = 0
        total_values = 0

        # Dataframe to store differences
        differences = pd.DataFrame(columns=["Row", "Column", "File1 Value", "File2 Value"])

        # Compare the data column by column
        for column in df1.columns:
            # Identify rows with differences in the current column
            mismatched_rows = df1[column] != df2[column]

            # Get differences
            diff_rows = df1[mismatched_rows].index
            rows_to_add = []
            for row in diff_rows:
                rows_to_add.append({
                    "Row": row + 1,  # Row index starts from 1 for user-friendly display
                    "Column": column,
                    "File1 Value": df1.at[row, column],
                    "File2 Value": df2.at[row, column]
                })

            # Add new rows to the differences DataFrame
            differences = pd.concat([differences, pd.DataFrame(rows_to_add)], ignore_index=True)

            # Count anomalies for the current column
            column_total_values = len(df1[column])
            column_anomalies = mismatched_rows.sum()
            column_anomaly_percentage = (column_anomalies / column_total_values) * 100

            # Save the result for the column
            anomaly_summary[column] = {
                "Total Values": column_total_values,
                "Anomalies": column_anomalies,
                "Anomaly Percentage": column_anomaly_percentage,
            }

            # Update overall anomalies
            total_anomalies += column_anomalies
            total_values += column_total_values

        # Calculate overall and average anomaly percentages
        overall_anomaly_percentage = (total_anomalies / total_values) * 100
        average_anomaly_percentage = sum(
            stats["Anomaly Percentage"] for stats in anomaly_summary.values()
        ) / len(anomaly_summary)

        # Display column-wise anomaly summary
        st.write("### Column-wise Anomaly Summary:")
        st.write("")  # Adds space between the lines
        for column, stats in anomaly_summary.items():
            st.write(f"**Column:** {column}")
            st.write(f"  - Total Values: {stats['Total Values']}")
            st.write(f"  - Anomalies: {stats['Anomalies']}")
            st.write(f"  - Anomaly Percentage: {stats['Anomaly Percentage']:.2f}%")
            st.write("")  # Adds space between the lines
        # Display overall statistics
        st.write("### Overall Statistics:")
        st.write(f"  - Total Values: {total_values}")
        st.write(f"  - Total Anomalies: {total_anomalies}")
        st.write(f"  - Overall Anomaly Percentage: {overall_anomaly_percentage:.2f}%")
        st.write(f"  - Average Anomaly Percentage Across Columns: {average_anomaly_percentage:.2f}%")
        st.write("")  # Adds space between the lines
        # Display the differences found
        st.write("### Differences Found:")
        st.dataframe(differences)
        st.write("")  # Adds space between the lines
        overall_accuracy = 100 - overall_anomaly_percentage
        st.write("### Accuracy:")
        st.write(f"Overall Accuracy: {overall_accuracy:.2f}%")
        
else:
    st.write("Please upload both CSV files to proceed.")
