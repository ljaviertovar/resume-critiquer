"""Reusable UI components for Streamlit interface."""

from typing import Generator, Optional, Tuple, Any
import streamlit as st
import streamlit.components.v1 as st_components


def render_header() -> None:
    """Render the application header and value proposition."""
    st.markdown(
        """
        <section class="app-hero">
            <div class="hero-kicker">Resume review powered by AI</div>
            <h1>AI Resume Critiquer</h1>
            <p>
                Sube tu CV en PDF o TXT y recibe una revisión clara, accionable y
                orientada al rol que quieres conseguir.
            </p>
            <div class="feature-grid" aria-label="Puntos evaluados">
                <span>Claridad e impacto</span>
                <span>Experiencia y logros</span>
                <span>Skills relevantes</span>
                <span>Optimización ATS</span>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_upload_section() -> Tuple[Optional[Any], str]:
    """
    Render the file upload and job role input sections.

    Returns:
        Tuple of (uploaded_file, job_role)
    """
    st.markdown(
        """
        <div class="section-heading">
            <span>01</span>
            <div>
                <h2>Prepara el análisis</h2>
                <p>El archivo es obligatorio. El rol objetivo ayuda a personalizar las recomendaciones.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.55, 1], gap="large")

    with col1:
        st.markdown("#### CV")
        uploaded_file = st.file_uploader(
            "Sube un archivo PDF o TXT",
            type=["pdf", "txt"],
            help="Formatos soportados: PDF y TXT. Tamaño máximo: 200 MB.",
            label_visibility="visible",
        )
        if uploaded_file:
            st.caption(
                f"Archivo listo: {uploaded_file.name} "
                f"({uploaded_file.size / 1024:.1f} KB)"
            )
        else:
            st.caption("Tu CV se procesa localmente antes de enviarse al análisis.")

    with col2:
        st.markdown("#### Rol objetivo")
        job_role = st.text_input(
            "Puesto o seniority",
            placeholder="Ej. Senior Python Engineer",
            help="Déjalo vacío si quieres una revisión general.",
        )
        st.caption("Opcional, pero recomendado para obtener feedback más preciso.")

    return uploaded_file, job_role.strip()


def render_feedback(generator: Generator[str, None, None]) -> None:
    """
    Render AI feedback with real-time streaming.

    Args:
        generator: Generator yielding text chunks from AI
    """
    st.markdown(
        """
        <div id="analysis-result" class="section-heading feedback-heading">
            <span>02</span>
            <div>
                <h2>Feedback de IA</h2>
                <p>Revisión estructurada con fortalezas, mejoras y próximos pasos.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    feedback_container = st.container()

    with feedback_container:
        st.caption("Generando la respuesta en tiempo real. Puedes empezar a leer mientras continúa el análisis.")
        focus_result_heading()
        st.write_stream(generator)

    st.success("Análisis completado. Ya puedes revisar las recomendaciones y ajustar tu CV.")


def focus_result_heading() -> None:
    """Focus the analysis heading when streaming starts."""
    st_components.html(
        """
        <script>
            const doc = window.parent.document;
            const targetId = "analysis-result";
            let attempts = 0;

            function getScrollParents(node) {
                const parents = [window.parent, doc.scrollingElement, doc.documentElement, doc.body];
                let current = node ? node.parentElement : null;

                while (current) {
                    const styles = window.parent.getComputedStyle(current);
                    const overflowY = styles.overflowY;
                    const canScroll = current.scrollHeight > current.clientHeight + 4;

                    if (canScroll && ["auto", "scroll", "overlay", "hidden"].includes(overflowY)) {
                        parents.push(current);
                    }

                    current = current.parentElement;
                }

                return [...new Set(parents.filter(Boolean))];
            }

            function scrollParentToTarget(parent, target) {
                const offset = 6;

                if (parent === window.parent) {
                    const top = target.getBoundingClientRect().top + window.parent.scrollY - offset;
                    window.parent.scrollTo({ top: Math.max(top, 0), behavior: "smooth" });
                    return;
                }

                const parentRect = parent.getBoundingClientRect
                    ? parent.getBoundingClientRect()
                    : { top: 0 };
                const top = target.getBoundingClientRect().top
                    - parentRect.top
                    + parent.scrollTop
                    - offset;

                parent.scrollTo({ top: Math.max(top, 0), behavior: "smooth" });
            }

            function focusResult(behavior = "smooth") {
                const target = doc.getElementById(targetId);
                if (target) {
                    getScrollParents(target).forEach((parent) => scrollParentToTarget(parent, target));
                    return;
                }

                attempts += 1;
                if (attempts < 18) {
                    window.setTimeout(focusResult, 90);
                }
            }

            window.requestAnimationFrame(focusResult);
            [80, 180, 320, 520, 800, 1200].forEach((delay) => {
                window.setTimeout(focusResult, delay);
            });
        </script>
        """,
        height=0,
    )


def render_error(message: str) -> None:
    """
    Render an error message with styling.

    Args:
        message: Error message to display
    """
    st.error(message)


def render_empty_state() -> None:
    """Render an empty state placeholder when no file is uploaded."""
    st.markdown(
        """
        <section class="empty-state">
            <div>
                <span class="empty-icon">Ready</span>
                <h3>Cuando subas tu CV, aparecerá aquí el análisis.</h3>
                <p>
                    Te mostraré una puntuación general, fortalezas, áreas de mejora,
                    recomendaciones concretas y ajustes para ATS.
                </p>
            </div>
            <ol>
                <li>Sube tu archivo PDF o TXT.</li>
                <li>Agrega el rol objetivo si quieres feedback personalizado.</li>
                <li>Presiona Analizar CV.</li>
            </ol>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_loading_state() -> None:
    """Render a loading state with animation."""
    with st.spinner("Analizando tu CV..."):
        st.write("")
