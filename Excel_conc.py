import streamlit as st
import pandas as pd
from os.path import splitext

# Create a file uploader widget
uploaded_files = st.file_uploader("Choose Excel and CSV files", type=["xls", "xlsx", "csv"], accept_multiple_files=True)

if uploaded_files is not None:
    # Create an empty list to store the dataframes
    df_list = []

     # Use a for loop to read in each file
    for file in uploaded_files:
        # Split the file name and extension
        _, file_extension = splitext(file.name)

        # Check the file extension
        if file_extension in [".xls", ".xlsx"]:
            # Read the Excel file into a dataframe
            df = pd.read_excel(file)
        elif file_extension == ".csv":
            # Read the CSV file into a dataframe
            df = pd.read_csv(file)
            
        # Append the dataframe to the list
        df_list.append(df)

    # Concatenate all of the dataframes into a single dataframe
    df_final = pd.concat(df_list)

    # Create an ExcelWriter object
    with pd.ExcelWriter('concatenated_data.xlsx', engine='openpyxl') as writer:
        # Save the final dataframe to a new Excel file
        df_final.to_excel(writer, index=False)
        
       
        
    # Display a success message
    st.success("Data concatenation complete!")
