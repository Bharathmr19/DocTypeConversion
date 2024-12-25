import streamlit as st
import os
import win32com.client
import pythoncom  # To initialize COM

def convert_excel_to_pdf(uploaded_file, output_path="converted_document.pdf"):
    # Initialize COM
    pythoncom.CoInitialize()

    # Save the uploaded Excel file temporarily
    with open("temp.xlsx", "wb") as temp_file:
        temp_file.write(uploaded_file.read())
    
    # Initialize Excel COM object
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False  # Don't show Excel window

    # Open the Excel file
    workbook = excel.Workbooks.Open(os.path.abspath("temp.xlsx"))

    # Save the Excel file as PDF
    workbook.ExportAsFixedFormat(0, os.path.abspath(output_path))  # 0 is the constant for PDF format
    
    # Close the workbook
    workbook.Close()
    excel.Quit()

    # Clean up temporary Excel file
    os.remove("temp.xlsx")

    # Uninitialize COM
    pythoncom.CoUninitialize()

    return output_path

# Streamlit App
st.title("Convert Excel to PDF")

# Add unique keys to the components
uploaded_file = st.file_uploader("Upload an Excel file", type="xlsx", key="excel_to_pdf_uploader")

if uploaded_file:
    if st.button("Convert to PDF", key="excel_to_pdf_button"):
        with st.spinner("Converting..."):
            output_file = convert_excel_to_pdf(uploaded_file)
        st.success("Excel document converted to PDF successfully!")
        with open(output_file, "rb") as file:
            st.download_button(
                label="Download PDF",
                data=file,
                file_name="converted_document.pdf",
                mime="application/pdf",
                key="excel_to_pdf_download_button"
            )
        # Clean up the output file after download
        os.remove(output_file)
