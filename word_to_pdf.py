import streamlit as st
import pypandoc
import os

def convert_word_to_pdf(uploaded_file, output_path="converted_document.pdf"):
    # Save the uploaded Word file temporarily
    with open("temp.docx", "wb") as temp_file:
        temp_file.write(uploaded_file.read())
    
    # Convert Word to PDF using pypandoc
    output = pypandoc.convert_file("temp.docx", 'pdf', outputfile=output_path)
    
    # Clean up temporary Word file
    os.remove("temp.docx")

    return output_path

# Streamlit App
st.title("Convert Word to PDF")

# Add unique keys to the components
uploaded_file = st.file_uploader("Upload a Word file", type="docx", key="word_to_pdf_uploader")

if uploaded_file:
    if st.button("Convert to PDF", key="word_to_pdf_button"):
        with st.spinner("Converting..."):
            output_file = convert_word_to_pdf(uploaded_file)
        st.success("Word document converted to PDF successfully!")
        
        # Provide the download button with a unique key
        with open(output_file, "rb") as file:
            st.download_button(
                label="Download PDF",
                data=file,
                file_name="converted_document.pdf",
                mime="application/pdf",
                key="word_to_pdf_download_button"
            )
        
        # Clean up the output file after download
        os.remove(output_file)
