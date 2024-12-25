import streamlit as st
from PyPDF2 import PdfMerger

def merge_pdfs(uploaded_files):
    merger = PdfMerger()
    for pdf in uploaded_files:
        merger.append(pdf)
    output_path = "merged_document.pdf"
    with open(output_path, "wb") as output_file:
        merger.write(output_file)
    return output_path

st.title("Merge PDFs")

# Add unique keys to the components
uploaded_files = st.file_uploader(
    "Upload PDF files", type="pdf", accept_multiple_files=True, key="merges_pdfs_uploader"
)

if uploaded_files:
    if st.button("Merge PDFs", key="merge_pdfs_button"):
        output_file = merge_pdfs(uploaded_files)
        st.success("PDFs merged successfully!")
        with open(output_file, "rb") as file:
            st.download_button(
                label="Download Merged PDF",
                data=file,
                file_name="merged_document.pdf",
                mime="application/pdf",
                key="merge_pdfs_download_button"
            )
