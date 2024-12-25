import streamlit as st
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(uploaded_file, page_range=None):
    reader = PdfReader(uploaded_file)
    writer = PdfWriter()

    # If page range is specified, extract those pages; otherwise, split all pages
    if page_range:
        start, end = map(int, page_range.split('-'))
        for i in range(start - 1, end):
            writer.add_page(reader.pages[i])
    else:
        for page in reader.pages:
            writer.add_page(page)

    output_path = "split_document.pdf"
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    return output_path

st.title("Split PDFs")

# Add unique keys to the components
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf", key="split_pdf_uploader")
page_range = st.text_input("Enter page range (eg., 1-3) or leave blank to split all pages", key="split_pdf_page_range")

if uploaded_file:
    if st.button("Split PDF", key="split_pdf_button"):
        output_file = split_pdf(uploaded_file, page_range)
        st.success("PDF split successfully!")
        with open(output_file, "rb") as file:
            st.download_button(
                label="Download split PDF",
                data=file,
                file_name="split_document.pdf",
                mime="application/pdf",
                key="split_pdf_download_button"
            )
