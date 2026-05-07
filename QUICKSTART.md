# Quick Start Guide

## Setup (One-time)

```bash
# 1. Navigate to project
cd /home/ljdev/ljdevPY/resume-critiquer

# 2. Create .env file with your OpenAI API key
cp .env.example .env

# Open .env and update:
# OPENAI_API_KEY=sk-your-actual-key-here
```

## Run Application

```bash
# 1. Activate virtual environment
source .venv/bin/activate

# 2. Run Streamlit app
uv run streamlit run main.py

# 3. Open browser
# Visit: http://localhost:8501
```

## Usage

1. **Upload Resume** — Choose PDF or TXT file
2. **Enter Job Role** (optional) — e.g., "Senior Python Engineer"
3. **Click "Analyze Resume"** — Watch real-time feedback stream
4. **Review Feedback** — Structured analysis appears instantly

## Common Commands

```bash
# Check Streamlit version
streamlit --version

# Run with different config
uv run streamlit run main.py --logger.level=debug

# Install/update dependencies
uv sync

# Test imports
source .venv/bin/activate && python3 -c "from app.config import settings; print('✅ OK')"
```

## Troubleshooting

### "invalid model ID"
→ Check `OPENAI_MODEL` in `.env` (default: `gpt-4o-mini`)

### "Authentication failed"
→ Verify `OPENAI_API_KEY` in `.env` is valid

### "No module named 'app'"
→ Make sure you activated the virtual environment: `source .venv/bin/activate`

### "PDF text is empty"
→ Ensure PDF contains selectable text (not just images)

## Files Overview

| File | Purpose |
|------|---------|
| `main.py` | Entry point (~50 lines) |
| `app/config.py` | Configuration & validation |
| `app/core/resume_parser.py` | PDF/TXT parsing |
| `app/services/ai_analyzer.py` | OpenAI integration |
| `app/ui/styles.py` | Dark theme CSS |
| `app/ui/components.py` | UI components |
| `README.md` | Full documentation |
| `ARCHITECTURE.md` | Design documentation |

## Documentation

- **README.md** — Full guide with all features
- **ARCHITECTURE.md** — Technical design & patterns
- **IMPLEMENTATION_SUMMARY.md** — What was done
- **.env.example** — Configuration template

---

**Ready to analyze resumes! 🚀**
