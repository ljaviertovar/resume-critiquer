import streamlit as st

import io
import os
from pypdf import PdfReader
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

st.set_page_config(
    page_title="AI Resume Critiquer", page_icon=":note:", layout="centered"
)

st.title("AI Resume Critiquer")
st.markdown(
    "Upload your resume in PDF format, and the AI will provide feedback to help you improve it."
)

upload_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you are applying for")


def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")


analize_button = st.button("Analyze Resume")
if analize_button and upload_file:
    try:
        file_content = extract_text_from_file(upload_file)
        if not file_content.strip():
            st.error("The uploaded file is empty. Please upload a valid resume.")
        else:
            prompt = f"""Please analyze this resume and provide constructive feedback. 
            Focus on the following aspects:
            1. Content clarity and impact
            2. Skills presentation
            3. Experience descriptions
            4. Specific improvements for {job_role if job_role else "general job applications"}
            
            Resume content:
            {file_content}
            
            Please provide your analysis in a clear, structured format with specific recommendations."""

            client = OpenAI(api_key=OPENAI_API_KEY)

            response = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert resume reviewer with years of experience in HR and recruitment.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=1500,
            )
            st.subheader("AI Feedback:")
            st.write(response.choices[0].message.content)
    except Exception as e:
        st.error(f"An error occurred while analyzing the resume: {e}")
elif analize_button:
    st.error("Please upload a resume file before analyzing.")
