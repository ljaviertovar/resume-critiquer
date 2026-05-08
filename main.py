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

# Inject dark theme CSS
styles.inject_css()

# Render header
components.render_header()

# Render upload section
uploaded_file, job_role = components.render_upload_section()

# Main analysis logic
analyze_button = st.button(
    "Analizar CV",
    type="primary",
    use_container_width=True,
)

if analyze_button:
    if not uploaded_file:
        components.render_error("Sube un archivo PDF o TXT antes de iniciar el análisis.")
    else:
        status = st.status("Preparando el análisis del CV...", expanded=True)
        try:
            status.write("Leyendo el archivo y extrayendo el texto.")

            with st.spinner("Extrayendo el texto del CV..."):
                resume_text = ResumeParser.parse(uploaded_file)

            status.write("Texto extraído correctamente.")
            status.write("Conectando con el modelo de IA para generar recomendaciones.")
            analyzer = AIAnalyzer(settings)

            status.update(label="Generando feedback personalizado...", state="running")
            components.render_feedback(analyzer.analyze(resume_text, job_role))
            status.update(label="Análisis completado.", state="complete", expanded=False)

        except ValueError as e:
            status.update(label="No se pudo analizar el archivo.", state="error")
            components.render_error(str(e))
        except Exception as e:
            status.update(label="El análisis se interrumpió.", state="error")
            components.render_error(
                f"No se pudo completar el análisis: {str(e)}\n\n"
                "Revisa que tu OPENAI_API_KEY esté configurada correctamente en el archivo .env."
            )
else:
    if not uploaded_file:
        components.render_empty_state()
