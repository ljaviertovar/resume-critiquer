"""CSS styling for a polished Streamlit dark interface."""

import streamlit as st

DARK_THEME_CSS = """
<style>
    :root {
        --bg-primary: #080b12;
        --bg-secondary: #101620;
        --bg-tertiary: #17202c;
        --bg-muted: #202938;
        --border: #2b3444;
        --border-strong: #3b4658;
        --text-primary: #f5f7fb;
        --text-secondary: #a9b4c3;
        --text-muted: #7e8a9b;
        --accent: #60a5fa;
        --accent-strong: #38bdf8;
        --accent-soft: rgba(96, 165, 250, 0.14);
        --accent-danger: #fb7185;
        --accent-success: #34d399;
        --shadow: 0 18px 60px rgba(0, 0, 0, 0.35);
    }

    html, body, .stApp, .main {
        background-color: var(--bg-primary);
        color: var(--text-primary);
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Helvetica Neue", sans-serif;
    }

    .block-container {
        max-width: 1080px;
        padding: 2.75rem 2rem 4rem;
    }

    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary);
        font-weight: 600;
        letter-spacing: 0;
    }

    p, li, label, .stMarkdown, .stCaption {
        color: var(--text-secondary);
    }

    .app-hero {
        padding: 1.75rem 0 2.25rem;
        border-bottom: 1px solid var(--border);
    }

    .hero-kicker {
        color: var(--accent-strong);
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0;
        margin-bottom: 0.75rem;
        text-transform: uppercase;
    }

    .app-hero h1 {
        color: var(--text-primary);
        font-size: clamp(2.4rem, 6vw, 4.7rem);
        line-height: 0.95;
        margin: 0 0 1rem;
    }

    .app-hero p {
        color: var(--text-secondary);
        font-size: 1.08rem;
        line-height: 1.65;
        max-width: 720px;
        margin: 0;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.75rem;
        margin-top: 1.65rem;
    }

    .feature-grid span {
        background: var(--bg-secondary);
        border: 1px solid var(--border);
        border-radius: 8px;
        color: var(--text-primary);
        font-size: 0.9rem;
        font-weight: 600;
        padding: 0.82rem 0.9rem;
    }

    .section-heading {
        align-items: flex-start;
        display: flex;
        gap: 1rem;
        margin: 2.25rem 0 1.15rem;
    }

    .section-heading > span {
        align-items: center;
        background: var(--accent-soft);
        border: 1px solid rgba(96, 165, 250, 0.35);
        border-radius: 999px;
        color: var(--accent-strong);
        display: inline-flex;
        flex: 0 0 auto;
        font-size: 0.82rem;
        font-weight: 800;
        height: 2.25rem;
        justify-content: center;
        width: 2.25rem;
    }

    .section-heading h2 {
        font-size: 1.55rem;
        line-height: 1.2;
        margin: 0;
    }

    .section-heading p {
        margin: 0.28rem 0 0;
        max-width: 620px;
    }

    [data-testid="column"] {
        min-width: 0;
    }

    [data-testid="stHorizontalBlock"] {
        align-items: stretch;
        gap: 1.25rem;
    }

    [data-testid="stHorizontalBlock"] > [data-testid="column"] {
        background-color: var(--bg-secondary);
        border: 1px solid var(--border);
        border-radius: 8px;
        box-shadow: var(--shadow);
        display: flex;
        flex-direction: column;
        min-height: 12.25rem;
        padding: 1.1rem;
    }

    [data-testid="stHorizontalBlock"] > [data-testid="column"] [data-testid="stVerticalBlock"] {
        gap: 0.55rem;
    }

    [data-testid="stHorizontalBlock"] > [data-testid="column"] h4 {
        font-size: 1.08rem;
        margin: 0 0 0.2rem;
    }

    [data-testid="stFileUploader"], [data-testid="stTextInput"] {
        background: transparent;
        border: 0;
        padding: 0;
        box-shadow: none;
    }

    [data-testid="fileUploadDropzone"] {
        background-color: var(--bg-tertiary);
        border: 1px dashed var(--border-strong);
        border-radius: 8px;
        min-height: 4.75rem;
        padding: 1rem !important;
    }

    [data-testid="fileUploadDropzone"]:hover {
        background-color: var(--bg-muted);
        border-color: var(--accent-strong);
    }

    [data-testid="fileUploadDropzone"] button {
        border-radius: 8px;
        min-height: 2.5rem;
    }

    [data-testid="stFileUploader"] small,
    [data-testid="stFileUploader"] [data-testid="stMarkdownContainer"] p {
        color: var(--text-secondary);
    }

    .stButton > button {
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-strong) 100%);
        color: #06111f;
        border: none;
        border-radius: 8px;
        font-weight: 700;
        min-height: 3rem;
        padding: 0.75rem 1.1rem;
        cursor: pointer;
        transition: all 0.2s ease;
        box-shadow: 0 12px 30px rgba(56, 189, 248, 0.18);
    }

    div[data-testid="stButton"] {
        margin-top: 1rem;
    }

    .stButton > button:hover {
        box-shadow: 0 16px 38px rgba(56, 189, 248, 0.28);
        transform: translateY(-1px);
    }

    .stButton > button:active {
        transform: translateY(0);
    }

    .stTextInput > div > div > input {
        background-color: var(--bg-tertiary);
        color: var(--text-primary);
        border: 1px solid var(--border);
        border-radius: 8px;
        min-height: 2.75rem;
        padding: 0.7rem 0.85rem;
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--accent);
        outline: none;
        box-shadow: 0 0 0 3px var(--accent-soft);
    }

    .stAlert {
        border-radius: 8px;
    }

    .stSuccess {
        background-color: rgba(52, 211, 153, 0.1);
        border: 1px solid rgba(52, 211, 153, 0.45);
    }

    .stError {
        background-color: rgba(251, 113, 133, 0.1);
        border: 1px solid rgba(251, 113, 133, 0.45);
    }

    .stInfo {
        background-color: var(--accent-soft);
        border: 1px solid rgba(96, 165, 250, 0.35);
    }

    .empty-state {
        align-items: start;
        background: var(--bg-secondary);
        border: 1px solid var(--border);
        border-radius: 8px;
        display: grid;
        gap: 1.5rem;
        grid-template-columns: minmax(0, 1.3fr) minmax(220px, 0.7fr);
        margin-top: 1.35rem;
        padding: 1.35rem;
    }

    .empty-state h3 {
        font-size: 1.25rem;
        margin: 0.45rem 0 0.45rem;
    }

    .empty-state p, .empty-state li {
        line-height: 1.6;
    }

    .empty-state ol {
        margin: 0;
        padding-left: 1.2rem;
    }

    .empty-icon {
        color: var(--accent-strong);
        font-size: 0.82rem;
        font-weight: 800;
        letter-spacing: 0;
        text-transform: uppercase;
    }

    .stProgress > div > div > div {
        background: linear-gradient(90deg, var(--accent) 0%, var(--accent-strong) 100%);
    }

    .feedback-heading {
        border-top: 1px solid var(--border);
        margin-top: 2rem;
        padding-top: 1.85rem;
        scroll-margin-top: 1rem;
    }

    [data-testid="stStatusWidget"] {
        background-color: var(--bg-secondary);
        border: 1px solid var(--border);
        border-radius: 8px;
        margin-top: 1rem;
    }

    [data-testid="stStatusWidget"] p {
        color: var(--text-secondary);
    }

    .stMarkdown a, a {
        color: var(--accent);
        text-decoration: none;
    }

    .stMarkdown a:hover {
        text-decoration: underline;
    }

    /* Code blocks */
    pre {
        background-color: var(--bg-tertiary);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 1em;
    }

    code {
        color: var(--accent);
    }

    hr {
        border-color: var(--border);
    }

    [data-testid="metric-container"] {
        background-color: var(--bg-tertiary);
        border: 1px solid var(--border);
        border-radius: 8px;
    }

    [data-testid="stSidebar"] {
        background-color: var(--bg-secondary);
        border-right: 1px solid var(--border);
    }

    header [data-testid="stToolbar"] {
        color: var(--text-primary);
    }

    @media (max-width: 900px) {
        .block-container {
            padding: 2rem 1.2rem 3rem;
        }

        [data-testid="stHorizontalBlock"] {
            gap: 1rem;
        }

        [data-testid="stHorizontalBlock"] > [data-testid="column"] {
            min-height: 0;
        }

        .feature-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
    }

    @media (max-width: 640px) {
        .block-container {
            padding: 1.25rem 1rem 2.5rem;
        }

        .app-hero {
            padding-top: 1.25rem;
        }

        .app-hero h1 {
            font-size: 2.45rem;
            line-height: 1;
        }

        .app-hero p {
            font-size: 1rem;
        }

        .feature-grid {
            grid-template-columns: 1fr;
        }

        .section-heading {
            gap: 0.75rem;
            margin-top: 1.6rem;
        }

        .section-heading h2 {
            font-size: 1.3rem;
        }

        [data-testid="stHorizontalBlock"] > [data-testid="column"] {
            padding: 0.9rem;
        }

        .empty-state {
            grid-template-columns: 1fr;
            padding: 1rem;
        }
    }
</style>
"""


def inject_css() -> None:
    """Inject the dark theme CSS into the Streamlit app."""
    st.markdown(DARK_THEME_CSS, unsafe_allow_html=True)
