import streamlit as st
import os
import win32com.client
import pythoncom
import tempfile

def convert_powerpoint_to_pdf(uploaded_file, output_path="converted_document.pdf"):
    # Initialize COM
    pythoncom.CoInitialize()

    # Save the uploaded PowerPoint file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pptx") as tmp_pptx:
        tmp_pptx.write(uploaded_file.read())
        tmp_pptx_path = tmp_pptx.name

    # Initialize PowerPoint COM object
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    # Do not hide the PowerPoint window
    powerpoint.Visible = True  # Make PowerPoint visible during the process

    # Open the PowerPoint presentation
    presentation = powerpoint.Presentations.Open(tmp_pptx_path)

    # Save the presentation as PDF
    presentation.SaveAs(output_path, 32)  # 32 is the constant for PDF format

    # Close the presentation and quit PowerPoint
    presentation.Close()
    powerpoint.Quit()

    # Clean up the temporary PowerPoint file
    os.remove(tmp_pptx_path)

    # Uninitialize COM
    pythoncom.CoUninitialize()

    return output_path

# Streamlit App
st.title("Convert PowerPoint to PDF")

uploaded_file = st.file_uploader("Upload a PowerPoint presentation", type="pptx")

if uploaded_file:
    if st.button("Convert to PDF"):
        with st.spinner("Converting..."):
            # Convert the PowerPoint presentation to PDF
            output_file = convert_powerpoint_to_pdf(uploaded_file)

        st.success("PowerPoint presentation converted to PDF successfully!")
        
        # Provide the download button
        with open(output_file, "rb") as file:
            st.download_button(
                label="Download PDF",
                data=file,
                file_name="converted_document.pdf",
                mime="application/pdf"
            )
        
        # Clean up the output file after download
        os.remove(output_file)
