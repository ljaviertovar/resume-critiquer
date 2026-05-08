"""
Resume Critiquer - Professional AI Resume Analyzer
Main Streamlit application entry point.
"""

import streamlit as st
from app.config import settings
from app.core.resume_parser import ResumeParser
from app.services.ai_analyzer import AIAnalyzer
from app.ui import styles, components


# Page configuration
st.set_page_config(
    page_title="AI Resume Critiquer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Inject theme-aware CSS
styles.inject_css()

# Render header
components.render_header()

# Render upload section
uploaded_file, job_role = components.render_upload_section()

# Main analysis logic
analyze_button = st.button(
    "Analyze Resume",
    type="primary",
    use_container_width=True,
)

if analyze_button:
    if not uploaded_file:
        components.render_error("Upload a PDF or TXT resume before starting the analysis.")
    else:
        status = st.status("Preparing resume analysis...", expanded=True)
        try:
            status.write("Reading the file and extracting text.")

            with st.spinner("Extracting resume text..."):
                resume_text = ResumeParser.parse(uploaded_file)

            status.write("Text extracted successfully.")
            status.write("Connecting to the AI model to generate recommendations.")
            analyzer = AIAnalyzer(settings)

            status.update(label="Generating personalized feedback...", state="running")
            components.render_feedback(analyzer.analyze(resume_text, job_role))
            status.update(label="Analysis complete.", state="complete", expanded=False)

        except ValueError as e:
            status.update(label="The file could not be analyzed.", state="error")
            components.render_error(str(e))
        except Exception as e:
            status.update(label="The analysis was interrupted.", state="error")
            components.render_error(
                f"The analysis could not be completed: {str(e)}\n\n"
                "Make sure your OPENAI_API_KEY is configured correctly in the .env file."
            )
else:
    if not uploaded_file:
        components.render_empty_state()

components.render_footer()
