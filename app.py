import streamlit as st
from compress_pdfs import compress_pdf
from excel_to_pdf import convert_excel_to_pdf
from jpg_to_pdf import convert_jpg_to_pdf
from merge_pdfs import merge_pdfs
from pdf_to_excel import convert_pdf_to_excel
from pdf_to_jpg import convert_pdf_to_jpg
from pdf_to_ppt import convert_pdf_to_ppt
from pdf_to_word import convert_pdf_to_word
from ppt_to_pdf import convert_ppt_to_pdf
from split_pdfs import split_pdf
from word_to_pdf import convert_word_to_pdf

# Streamlit App Title
st.title("Multi-Function PDF and File Converter")

# Sidebar for navigation
st.sidebar.title("Select a Functionality")
option = st.sidebar.selectbox(
    "Choose a functionality:",
    [
        "Merge PDFs",
        "Split PDFs",
        "Compress PDFs",
        "Convert PDF to Excel",
        "Convert PDF to JPG",
        "Convert PDF to PowerPoint",
        "Convert PDF to Word",
        "Convert PowerPoint to PDF",
        "Convert Excel to PDF",
        "Convert Word to PDF",
        "Convert JPG to PDF"
    ]
)

# Conditional rendering based on the selected functionality
if option == "Merge PDFs":
    st.header("Merge PDFs")
    uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True, key="merges_pdfs_uploader")
    if uploaded_files:
        if st.button("Merge PDFs"):
            merged_pdf = merge_pdfs(uploaded_files)
            st.download_button("Download Merged PDF", merged_pdf, file_name="merged_document.pdf", mime="application/pdf")

elif option == "Split PDFs":
    st.header("Split PDFs")
    uploaded_pdf = st.file_uploader("Upload a PDF to Split", type="pdf", key="split_pdfs_uploader")
    if uploaded_pdf:
        if st.button("Split PDF"):
            split_pdf(uploaded_pdf)  # Call your split PDF function here

elif option == "Compress PDFs":
    st.header("Compress PDFs")
    uploaded_pdf = st.file_uploader("Upload PDF to Compress", type="pdf", key="compress_pdfs_uploader")
    if uploaded_pdf:
        if st.button("Compress PDF"):
            compressed_pdf = compress_pdf(uploaded_pdf)
            st.download_button("Download Compressed PDF", compressed_pdf, file_name="compressed_document.pdf", mime="application/pdf")

elif option == "Convert PDF to Excel":
    st.header("Convert PDF to Excel")
    uploaded_pdf = st.file_uploader("Upload PDF to Convert to Excel", type="pdf", key="pdf_to_excel_uploader")
    if uploaded_pdf:
        if st.button("Convert to Excel"):
            converted_excel = convert_pdf_to_excel(uploaded_pdf)
            st.download_button("Download Excel", converted_excel, file_name="converted_document.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

elif option == "Convert PDF to JPG":
    st.header("Convert PDF to JPG")
    uploaded_pdf = st.file_uploader("Upload PDF to Convert to JPG", type="pdf", key="pdf_to_jpg_uploader")
    if uploaded_pdf:
        if st.button("Convert to JPG"):
            jpg_files = convert_pdf_to_jpg(uploaded_pdf)
            for jpg_file in jpg_files:
                st.image(jpg_file)

elif option == "Convert PDF to PowerPoint":
    st.header("Convert PDF to PowerPoint")
    uploaded_pdf = st.file_uploader("Upload PDF to Convert to PowerPoint", type="pdf", key="pdf_to_ppt_uploader")
    if uploaded_pdf:
        if st.button("Convert to PowerPoint"):
            ppt_file = convert_pdf_to_ppt(uploaded_pdf)
            st.download_button("Download PowerPoint", ppt_file, file_name="converted_ppt.pptx", mime="application/vnd.openxmlformats-officedocument.presentationml.presentation")

elif option == "Convert PDF to Word":
    st.header("Convert PDF to Word")
    uploaded_pdf = st.file_uploader("Upload PDF to Convert to Word", type="pdf", key="pdf_to_word_uploader")
    if uploaded_pdf:
        if st.button("Convert to Word"):
            word_file = convert_pdf_to_word(uploaded_pdf)
            st.download_button("Download Word", word_file, file_name="converted_document.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

elif option == "Convert PowerPoint to PDF":
    st.header("Convert PowerPoint to PDF")
    uploaded_pptx = st.file_uploader("Upload PowerPoint to Convert to PDF", type="pptx", key="ppt_to_pdf_uploader")
    if uploaded_pptx:
        if st.button("Convert to PDF"):
            ppt_to_pdf_file = convert_ppt_to_pdf(uploaded_pptx)
            st.download_button("Download PDF", ppt_to_pdf_file, file_name="converted_ppt.pdf", mime="application/pdf")

elif option == "Convert Excel to PDF":
    st.header("Convert Excel to PDF")
    uploaded_excel = st.file_uploader("Upload Excel to Convert to PDF", type="xlsx", key="excel_to_pdf_uploader")
    if uploaded_excel:
        if st.button("Convert to PDF"):
            excel_to_pdf_file = convert_excel_to_pdf(uploaded_excel)
            st.download_button("Download PDF", excel_to_pdf_file, file_name="converted_excel.pdf", mime="application/pdf")

elif option == "Convert Word to PDF":
    st.header("Convert Word to PDF")
    uploaded_word = st.file_uploader("Upload Word to Convert to PDF", type="docx", key="word_to_pdf_uploader")
    if uploaded_word:
        if st.button("Convert to PDF"):
            word_to_pdf_file = convert_word_to_pdf(uploaded_word)
            st.download_button("Download PDF", word_to_pdf_file, file_name="converted_word.pdf", mime="application/pdf")

elif option == "Convert JPG to PDF":
    st.header("Convert JPG to PDF")
    uploaded_jpg = st.file_uploader("Upload JPG to Convert to PDF", type="jpg", key="jpg_to_pdf_uploader")
    if uploaded_jpg:
        if st.button("Convert to PDF"):
            jpg_to_pdf_file = convert_jpg_to_pdf(uploaded_jpg)
            st.download_button("Download PDF", jpg_to_pdf_file, file_name="converted_image.pdf", mime="application/pdf")

# Add a line and footer text at the bottom of the sidebar
st.sidebar.markdown("---")  # This adds a horizontal line
st.sidebar.markdown("Made by Bharath Gowda M R")
