"""Resume parsing functionality for PDF and TXT files."""

import io
from pypdf import PdfReader


class ResumeParser:
    """Handles extraction of text from resume files (PDF and TXT)."""

    @staticmethod
    def parse(uploaded_file) -> str:
        """
        Parse uploaded resume file and extract text.

        Args:
            uploaded_file: Streamlit UploadedFile object (PDF or TXT)

        Returns:
            Extracted text from the resume

        Raises:
            ValueError: If file is empty or unsupported format
            Exception: If PDF reading fails
        """
        if uploaded_file.type == "application/pdf":
            text = ResumeParser._from_pdf(uploaded_file)
        elif uploaded_file.type == "text/plain":
            text = ResumeParser._from_txt(uploaded_file)
        else:
            raise ValueError(f"Unsupported file type: {uploaded_file.type}")

        if not text.strip():
            raise ValueError("The uploaded file is empty. Please upload a valid resume.")

        return text

    @staticmethod
    def _from_pdf(file_obj) -> str:
        """Extract text from PDF file."""
        try:
            reader = PdfReader(io.BytesIO(file_obj.read()))
            text = ""
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
            return text
        except Exception as e:
            raise Exception(f"Failed to read PDF: {str(e)}")

    @staticmethod
    def _from_txt(file_obj) -> str:
        """Extract text from TXT file."""
        try:
            return file_obj.read().decode("utf-8")
        except UnicodeDecodeError:
            raise Exception("Failed to decode TXT file. Please ensure it's UTF-8 encoded.")
