from dotenv import load_dotenv
import fitz  # PyMuPDF
load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt): # input is the user input, pdf_content is the list of images from the pdf, prompt is the prompt to be used for the model
    model=genai.GenerativeModel('gemini-1.5-flash') # Using the Gemini Pro Vision model
    response=model.generate_content([input,pdf_content[0],prompt])  # Generating content using the model with the input, first page of the pdf, and the prompt
    return response.text # Returning the response text

def input_pdf_setup(uploaded_file): # Function to process the uploaded PDF file and convert it to images
    if uploaded_file is not None: # Check if a file is uploaded
        ## Convert the PDF to image
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        page = doc.load_page(0)  # First page
        pix = page.get_pixmap()

        # Convert to bytes, bytes are required for the model to process the image 
        img_byte_arr = io.BytesIO()  # Create a BytesIO object to hold the image bytes , hold means the image bytes will be stored in this object
        # img_byte_arr is an array of bytes of type BytesIO, specifically used to hold the image bytes in memory
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples) # Create an image from the pixmap samples, this is the image representation of the first page of the PDF
        img.save(img_byte_arr, format='JPEG') # Save the image to the BytesIO object in JPEG format
        img_byte_arr = img_byte_arr.getvalue() # Get the byte value of the image from memory stream

        pdf_parts = [ # Create a list of parts for the PDF, here we are only using the first page as it is the most relevant for the user input
            {
                "mime_type": "image/jpeg", # Specify the MIME type of the image, 
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64 as the model requires base64 encoded data
            }
        ]
        return pdf_parts # Return the list of parts containing the first page of the PDF as an image
    else:
        raise FileNotFoundError("No file uploaded")
    
## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
        
elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_text,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
