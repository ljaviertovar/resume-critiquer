# 🚀 AI Resume Critiquer

A professional, production-ready AI-powered resume analyzer built with **Streamlit** and **OpenAI**.

## Features

✨ **Intelligent Resume Analysis**
- AI-powered feedback using GPT-4o-mini (configurable model)
- Real-time streaming responses for instant feedback
- Structured analysis covering strengths, improvements, and ATS optimization

🎨 **Professional UI**
- Dark theme inspired by GitHub's design
- Elegant gradient headers and smooth interactions
- Responsive layout optimized for all devices

🔒 **Production-Ready**
- Environment variable validation with pydantic-settings
- Proper error handling and user-friendly messages
- Modular architecture for easy maintenance and extension
- Support for PDF and TXT resume formats

🎯 **Customizable**
- Target job role for tailored recommendations
- Configurable AI parameters (temperature, max_tokens, model)
- Extensible component system for UI customization

---

## Quick Start

### Prerequisites
- Python 3.12+
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository**
   ```bash
   cd resume-critiquer
   ```

2. **Create a `.env` file** from the template
   ```bash
   cp .env.example .env
   ```

3. **Add your OpenAI API key** to `.env`
   ```env
   OPENAI_API_KEY=sk-your-key-here
   OPENAI_MODEL=gpt-4o-mini
   ```

4. **Install dependencies** (using uv)
   ```bash
   uv sync
   ```

5. **Run the application**
   ```bash
   source .venv/bin/activate
   uv run streamlit run main.py
   ```

   The app will open at `http://localhost:8501`

---

## Configuration

### Environment Variables

All settings are loaded from `.env`:

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | *(required)* | Your OpenAI API key |
| `OPENAI_MODEL` | `gpt-4o-mini` | Model to use (e.g., `gpt-4o`, `gpt-4-turbo`) |
| `MAX_TOKENS` | `1500` | Maximum response length |
| `TEMPERATURE` | `0.7` | Creativity level (0-1) |

### Available Models

- `gpt-4o-mini` — Fast, affordable (recommended)
- `gpt-4o` — More capable, higher cost
- `gpt-4-turbo` — Balance of speed and capability

---

## Project Structure

```
resume-critiquer/
├── app/                          # Application package
│   ├── __init__.py              # Package initialization
│   ├── config.py                # Pydantic settings for environment vars
│   ├── core/
│   │   ├── __init__.py
│   │   └── resume_parser.py     # PDF/TXT parsing logic
│   ├── services/
│   │   ├── __init__.py
│   │   └── ai_analyzer.py       # OpenAI integration with streaming
│   └── ui/
│       ├── __init__.py
│       ├── styles.py            # Dark theme CSS
│       └── components.py        # Reusable UI components
├── main.py                       # Entry point (clean & concise)
├── pyproject.toml               # Project metadata & dependencies
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

---

## Usage

### Basic Workflow

1. **Upload** a resume (PDF or TXT format)
2. **(Optional)** Enter your target job role for tailored feedback
3. **Click** "Analyze Resume"
4. **View** real-time AI feedback streaming in the interface

### Example Job Roles

- Senior Software Engineer
- Product Manager
- Data Scientist
- Full-Stack Developer
- DevOps Engineer

---

## Architecture

### Modular Design

- **`app/config.py`** — Centralized configuration with validation
- **`app/core/resume_parser.py`** — Resume extraction logic (PDF, TXT)
- **`app/services/ai_analyzer.py`** — OpenAI API integration with streaming
- **`app/ui/styles.py`** — Professional dark theme CSS
- **`app/ui/components.py`** — Reusable UI building blocks
- **`main.py`** — Clean Streamlit entry point (~50 lines)

### Key Features

✅ **Separation of Concerns** — Each module has a single responsibility  
✅ **Error Handling** — Graceful error messages for users  
✅ **Streaming** — Real-time response display (no waiting)  
✅ **Type Hints** — Full Python type annotations  
✅ **Validation** — Environment variables validated at startup  

---

## Performance

- **Fast startup** — Config validation happens once
- **Streaming responses** — No waiting for full completion
- **Efficient parsing** — Direct PDF/TXT extraction
- **Optimized UI** — Minimal CSS for fast rendering

---

## Troubleshooting

### "invalid model ID" Error
→ Check `OPENAI_MODEL` in `.env` is a valid model name

### "Authentication failed" Error
→ Verify `OPENAI_API_KEY` is set correctly in `.env`

### PDF not extracting text
→ Ensure the PDF contains selectable text (not image-based)

### Slow responses
→ Try using `gpt-4o-mini` for faster responses (cheaper too!)

---

## Development

### Adding Custom Prompts

Edit the prompt in `app/services/ai_analyzer.py`:

```python
def _build_prompt(resume_text: str, job_role: str) -> str:
    # Customize the analysis structure here
    return f"""Your custom prompt..."""
```

### Extending UI Components

Add new components to `app/ui/components.py`:

```python
def render_custom_section():
    st.subheader("Your Section")
    # Component logic here
```

### Adding New Capabilities

1. Create a new module in `app/services/`
2. Import it in `main.py`
3. Use in the main logic

---

## Best Practices Applied

- ✅ **Type Safety** — Full Python typing throughout
- ✅ **Configuration Management** — Environment variables with validation
- ✅ **Error Handling** — Specific exception handling
- ✅ **Code Organization** — Modular architecture
- ✅ **Documentation** — Docstrings and comments
- ✅ **Security** — No hardcoded secrets
- ✅ **Performance** — Streaming for better UX
- ✅ **Accessibility** — Clear error messages

---

## License

MIT License - Feel free to use and modify!

---

## Support

For issues or questions:
1. Check the `.env` file is correctly configured
2. Verify your OpenAI API key is valid
3. Ensure all dependencies are installed: `uv sync`
4. Check Streamlit version: `streamlit --version` (should be ≥1.57.0)

---

**Built with ❤️ using Streamlit & OpenAI**
