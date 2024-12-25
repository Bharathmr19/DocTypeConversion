import streamlit as st
from pdf2docx import Converter
import os

def convert_pdf_to_word(uploaded_file, output_path="converted_document.docx"):
    with open("temp.pdf", "wb") as temp_file:
        temp_file.write(uploaded_file.read())
    
    converter = Converter("temp.pdf")
    converter.convert(output_path, start=0, end=None)
    converter.close()
    
    os.remove("temp.pdf")
    return output_path


st.title("Convert PDF to Word")

# Add unique keys to the components
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf", key="pdf_to_word_uploader")

if uploaded_file:
    if st.button("Convert to Word", key="pdf_to_word_button"):
        with st.spinner("Converting..."):
            output_file = convert_pdf_to_word(uploaded_file)
        st.success("PDF converted to Word successfully!")
        with open(output_file, "rb") as file:
            st.download_button(
                label="Download Word Document",
                data=file,
                file_name="converted_document.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                key="pdf_to_word_download_button"
            )
        # Clean up the converted file after download
        os.remove(output_file)
