import streamlit as st
import fitz  # PyMuPDF
import openpyxl
import os

def convert_pdf_to_excel(uploaded_file, output_path="converted_document.xlsx"):
    # Open the uploaded PDF
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    
    # Create a new Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        
        # Extract text from the PDF page
        text = page.get_text("text")
        
        # Split the text into lines and write it to the Excel sheet
        for line_number, line in enumerate(text.split('\n')):
            sheet.append([line])
    
    # Save the Excel file
    workbook.save(output_path)
    pdf_document.close()

    return output_path

# Streamlit App
st.title("Convert PDF to Excel")

# Add unique keys to the components
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf", key="pdf_to_excel_uploader")

if uploaded_file:
    if st.button("Convert to Excel", key="pdf_to_excel_button"):
        with st.spinner("Converting..."):
            output_file = convert_pdf_to_excel(uploaded_file)
        st.success("PDF converted to Excel successfully!")
        with open(output_file, "rb") as file:
            st.download_button(
                label="Download Excel File",
                data=file,
                file_name="converted_document.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key="pdf_to_excel_download_button"
            )
        # Clean up the output file after download
        os.remove(output_file)
