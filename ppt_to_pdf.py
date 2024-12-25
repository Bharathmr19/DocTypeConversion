import streamlit as st
import comtypes.client
import os

def convert_ppt_to_pdf(uploaded_file, output_path="converted_presentation.pdf"):
    # Save the uploaded PowerPoint file temporarily
    with open("temp.pptx", "wb") as temp_file:
        temp_file.write(uploaded_file.read())

    # Initialize the PowerPoint application (COM object)
    powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
    powerpoint.Visible = 1  # Set PowerPoint to visible (optional)

    # Open the PowerPoint presentation
    presentation = powerpoint.Presentations.Open(os.path.abspath("temp.pptx"))
    
    # Save as PDF
    presentation.SaveAs(os.path.abspath(output_path), 32)  # 32 is the constant for PDF format
    presentation.Close()
    powerpoint.Quit()

    # Clean up temporary PowerPoint file
    os.remove("temp.pptx")

    return output_path

# Streamlit App
st.title("Convert PowerPoint to PDF")

# Add unique keys to the components
uploaded_file = st.file_uploader("Upload a PowerPoint file", type="pptx", key="ppt_to_pdf_uploader")

if uploaded_file:
    if st.button("Convert to PDF", key="ppt_to_pdf_button"):
        with st.spinner("Converting..."):
            output_file = convert_ppt_to_pdf(uploaded_file)
        st.success("PowerPoint converted to PDF successfully!")
        with open(output_file, "rb") as file:
            st.download_button(
                label="Download PDF",
                data=file,
                file_name="converted_presentation.pdf",
                mime="application/pdf",
                key="ppt_to_pdf_download_button"
            )
        # Clean up the output file after download
        os.remove(output_file)
