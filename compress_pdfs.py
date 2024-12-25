import streamlit as st
import fitz

def compress_pdf(uploaded_file, output_quality=20):
    input_pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    output_pdf = "compressed_document.pdf"

    for page in input_pdf:
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_images = input_pdf.extract_image(xref)
            image_bytes = base_images["image"]

            from PIL import Image
            from io import BytesIO
            img = Image.open(BytesIO(image_bytes))
            img.save(BytesIO(), format="JPEG", optimize=True, quality=output_quality)

    input_pdf.save(output_pdf)
    return output_pdf

st.title("Compress PDFs")

# Add unique keys to the components
uploaded_file = st.file_uploader("Upload a pdf file", type="pdf", key="compress_pdf_uploader")
quality = st.slider("Select output quality (lower means more compression)", 10, 100, 50, key="compress_pdf_quality_slider")

if uploaded_file:
    if st.button("Compress PDF", key="compress_pdf_button"):
        output_file = compress_pdf(uploaded_file, quality)
        st.success("PDF compressed successfully!")
        with open(output_file, "rb") as file:
            st.download_button(
                label="Download compressed PDF",
                data=file,
                file_name="compressed_document.pdf",
                mime="application/pdf",
                key="compress_pdf_download_button"
            )
