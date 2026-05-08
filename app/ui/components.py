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
                Upload your resume as a PDF or TXT file and get clear, actionable
                feedback tailored to the role you want to land.
            </p>
            <div class="feature-grid" aria-label="Review focus areas">
                <span>Clarity and impact</span>
                <span>Experience and achievements</span>
                <span>Relevant skills</span>
                <span>ATS optimization</span>
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
                <h2>Prepare the analysis</h2>
                <p>The resume file is required. Adding a target role helps personalize the recommendations.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.55, 1], gap="large")

    with col1:
        st.markdown("#### Resume")
        uploaded_file = st.file_uploader(
            "Upload a PDF or TXT file",
            type=["pdf", "txt"],
            help="Supported formats: PDF and TXT. Maximum size: 200 MB.",
            label_visibility="visible",
        )
        if uploaded_file:
            st.caption(
                f"File ready: {uploaded_file.name} "
                f"({uploaded_file.size / 1024:.1f} KB)"
            )
        else:
            st.caption("Your resume is parsed locally before the analysis starts.")

    with col2:
        st.markdown("#### Target role")
        job_role = st.text_input(
            "Job title or seniority",
            placeholder="e.g., Senior Python Engineer",
            help="Leave this blank for a general resume review.",
        )
        st.caption("Optional, but recommended for more precise feedback.")

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
                <h2>AI Feedback</h2>
                <p>Structured review with strengths, improvements, and next steps.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    feedback_container = st.container()

    with feedback_container:
        st.caption("Generating the response in real time. You can start reading while the analysis continues.")
        focus_result_heading()
        st.write_stream(generator)

    st.success("Analysis complete. You can now review the recommendations and improve your resume.")


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
                <h3>Your analysis will appear here after you upload a resume.</h3>
                <p>
                    You will get an overall score, key strengths, improvement areas,
                    concrete recommendations, and ATS optimization tips.
                </p>
            </div>
            <ol>
                <li>Upload your PDF or TXT file.</li>
                <li>Add a target role if you want tailored feedback.</li>
                <li>Click Analyze Resume.</li>
            </ol>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    """Render the page footer."""
    st.markdown(
        """
        <footer class="app-footer">
            <p>Developed by <a href="https://www.ljaviertovar.dev/" target="_blank" rel="noreferrer">L Javier Tovar</a></p>
        </footer>
        """,
        unsafe_allow_html=True,
    )


def render_loading_state() -> None:
    """Render a loading state with animation."""
    with st.spinner("Analyzing your resume..."):
        st.write("")
