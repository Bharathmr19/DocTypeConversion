import streamlit as st
from PIL import Image
import os

def convert_jpg_to_pdf(uploaded_files, output_path="converted_document.pdf"):
    # Open the first image to create a PDF
    images = []
    
    for uploaded_file in uploaded_files:
        # Open each JPG file
        img = Image.open(uploaded_file)
        # Convert image to RGB (Pillow uses RGBA by default)
        img = img.convert("RGB")
        images.append(img)

    # Save all images as a single PDF
    images[0].save(output_path, save_all=True, append_images=images[1:])
    
    return output_path

# Streamlit App
st.title("Convert JPG to PDF")

# Add unique keys to the components
uploaded_files = st.file_uploader("Upload JPG files", type="jpg", accept_multiple_files=True, key="jpg_to_pdf_uploader")

if uploaded_files:
    if st.button("Convert to PDF", key="jpg_to_pdf_button"):
        with st.spinner("Converting..."):
            # Convert the JPG images to a single PDF
            output_file = convert_jpg_to_pdf(uploaded_files)
        
        st.success("JPG images converted to PDF successfully!")
        
        # Provide the download button
        with open(output_file, "rb") as file:
            st.download_button(
                label="Download PDF",
                data=file,
                file_name="converted_document.pdf",
                mime="application/pdf",
                key="jpg_to_pdf_download_button"
            )
        
        # Clean up the output file after download
        os.remove(output_file)
