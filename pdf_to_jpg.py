import streamlit as st
from pdf2image import convert_from_path
import os
import tempfile
import zipfile

def convert_pdf_to_jpg(uploaded_file, output_folder="converted_images"):
    # Create a folder for saving images if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save the uploaded PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
        tmp_pdf.write(uploaded_file.read())
        tmp_pdf_path = tmp_pdf.name

    # Convert the PDF to images (one per page)
    images = convert_from_path(tmp_pdf_path, 300)  # 300 DPI for better quality

    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i + 1}.jpg")
        image.save(image_path, 'JPEG')
        image_paths.append(image_path)

    # Clean up the temporary PDF file
    os.remove(tmp_pdf_path)

    return image_paths

# Streamlit App
st.title("Convert PDF to JPG")

# Add unique keys to the components
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf", key="pdf_to_jpg_uploader")

if uploaded_file:
    if st.button("Convert to JPG", key="pdf_to_jpg_button"):
        with st.spinner("Converting..."):
            # Convert the PDF to JPG images
            image_paths = convert_pdf_to_jpg(uploaded_file)

        st.success("PDF converted to JPG successfully!")

        # Create a ZIP file containing all JPG images for download
        zip_path = "converted_images.zip"
        with zipfile.ZipFile(zip_path, "w") as zipf:
            for image_path in image_paths:
                zipf.write(image_path, os.path.basename(image_path))
                os.remove(image_path)  # Remove the image file after adding it to the zip

        # Provide the download button
        with open(zip_path, "rb") as zip_file:
            st.download_button(
                label="Download ZIP of JPG images",
                data=zip_file,
                file_name="converted_images.zip",
                mime="application/zip",
                key="pdf_to_jpg_download_button"
            )

        # Clean up the zip file after download
        os.remove(zip_path)
