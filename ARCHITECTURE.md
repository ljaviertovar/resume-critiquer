# Architecture Documentation

## Overview

Resume Critiquer follows a **layered architecture** with clear separation of concerns:

```
┌─────────────────────────────────────┐
│      main.py (Entry Point)          │  Streamlit UI orchestration
├─────────────────────────────────────┤
│         UI Layer                    │  
│  (components.py, styles.py)         │  User interface & styling
├─────────────────────────────────────┤
│      Services Layer                 │
│   (ai_analyzer.py)                  │  Business logic & integrations
├─────────────────────────────────────┤
│      Core Layer                     │
│   (resume_parser.py)                │  Domain-specific logic
├─────────────────────────────────────┤
│   Infrastructure Layer              │
│      (config.py)                    │  Configuration & dependencies
└─────────────────────────────────────┘
```

---

## Detailed Structure

### 1. **Entry Point** (`main.py`)

**Responsibility:** Orchestrate the entire application flow

**What it does:**
- Configure Streamlit page settings
- Apply CSS styling
- Render UI components
- Handle user interactions
- Delegate to service layer
- Display results or errors

**Why this matters:**
- Keeps main.py clean and readable (~50 lines)
- All logic is delegated to appropriate modules
- Easy to understand the application flow

---

### 2. **Configuration Layer** (`app/config.py`)

**Responsibility:** Manage application settings and environment variables

**Technology:** Pydantic Settings

**What it does:**
- Validates environment variables at startup
- Provides type-safe configuration
- Raises `ValidationError` if required variables are missing
- Offers default values for optional settings

**Example:**
```python
settings = Settings()  # Fails early if OPENAI_API_KEY is missing
```

**Benefits:**
- Fail-fast approach (errors at startup, not runtime)
- Type-safe configuration access
- Single source of truth for settings

---

### 3. **Core Layer** (`app/core/`)

**Responsibility:** Domain-specific business logic

#### `resume_parser.py`
- Extracts text from uploaded files (PDF or TXT)
- Handles format-specific parsing
- Validates extracted content
- Raises meaningful exceptions

**Design Pattern:** Static methods for stateless operations

```python
text = ResumeParser.parse(uploaded_file)  # Simple, pure function
```

---

### 4. **Services Layer** (`app/services/`)

**Responsibility:** External integrations and business processes

#### `ai_analyzer.py`
- Integrates with OpenAI API
- Implements streaming for real-time responses
- Builds structured prompts
- Handles AI-specific logic

**Design Pattern:** Dependency injection (receives `Settings`)

```python
analyzer = AIAnalyzer(settings)
response_stream = analyzer.analyze(text, job_role)
```

**Why streaming?**
- Better UX: responses appear instantly
- Better UX: users see progress
- More cost-effective: can stop early if needed
- Production-standard pattern

---

### 5. **UI Layer** (`app/ui/`)

**Responsibility:** User interface and styling

#### `styles.py`
- CSS styling for dark theme
- Professional, GitHub-inspired design
- Consistent color palette
- Responsive styling

#### `components.py`
- Reusable Streamlit components
- Render header, upload section, feedback, errors
- Empty state handling
- Clean separation of UI concerns

**Design Pattern:** Component-based architecture

```python
components.render_header()  # Reusable, testable
components.render_feedback(stream)  # Composable
```

---

## Data Flow

```
User Action (Upload File)
        ↓
     main.py
        ↓
  UI Component
  (render_upload_section)
        ↓
   ResumeParser.parse()
     (core layer)
        ↓
   Extract Text
        ↓
  AIAnalyzer.analyze()
   (services layer)
        ↓
  OpenAI API Call
  (with streaming)
        ↓
  Yield Response Chunks
        ↓
   render_feedback()
   (UI component)
        ↓
   Display to User
```

---

## Error Handling

**Multi-level error handling:**

```
Level 1: Config Validation
├─ Missing OPENAI_API_KEY → ValidationError at startup

Level 2: File Processing
├─ Invalid file type → ValueError in ResumeParser
├─ Empty file → ValueError in ResumeParser
└─ Decoding error → Exception with helpful message

Level 3: API Integration
├─ Auth failure → Exception from OpenAI client
├─ Rate limiting → Exception from OpenAI client
└─ Model not found → Exception from OpenAI client

Level 4: User Feedback
└─ render_error() → User-friendly message
```

---

## Extension Points

### Adding New Resume Formats

```python
# In app/core/resume_parser.py
@staticmethod
def _from_docx(file_obj) -> str:
    # Add DOCX support
    ...

# Update parse() method to handle DOCX
```

### Adding New AI Features

```python
# Create app/services/resume_scorer.py
class ResumeScorerService:
    def __init__(self, settings):
        self.client = OpenAI(api_key=settings.openai_api_key)
    
    def score(self, text: str) -> int:
        # Score logic
        ...

# Use in main.py
```

### Customizing UI

```python
# In app/ui/components.py
def render_custom_section():
    st.markdown("...", unsafe_allow_html=True)
    # Custom UI logic
```

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | ≥1.57.0 | Web UI framework |
| openai | ≥2.36.0 | OpenAI API client |
| pypdf | ≥6.10.2 | PDF parsing |
| python-dotenv | ≥1.2.2 | Environment variables |
| pydantic-settings | ≥2.0.0 | Configuration validation |

---

## Performance Considerations

### Current Optimizations

1. **Lazy Loading** — Settings validated once at startup
2. **Streaming** — No buffering of full response
3. **Minimal CSS** — Inline CSS for fast rendering
4. **Efficient Parsing** — Direct PDF text extraction
5. **No State** — Stateless components for horizontal scaling

### Future Optimizations

- Cache parsed resumes (optional)
- Implement response rate limiting
- Add response caching for identical resumes
- Optimize CSS delivery

---

## Testing Strategy

### Unit Testing (Recommended)

```python
# tests/test_resume_parser.py
def test_parse_pdf():
    mock_file = Mock()
    result = ResumeParser.parse(mock_file)
    assert len(result) > 0

# tests/test_ai_analyzer.py
def test_analyze_returns_generator():
    settings = Settings(...)
    analyzer = AIAnalyzer(settings)
    gen = analyzer.analyze("Resume text", "Job role")
    assert isinstance(gen, Generator)
```

### Integration Testing

```python
# tests/test_integration.py
def test_full_flow():
    # Upload file → Parse → Analyze → Display
    ...
```

---

## Security

### Current Measures

✅ Environment variables in `.env` (not committed)  
✅ No hardcoded secrets  
✅ Input validation in ResumeParser  
✅ Exception handling prevents stack traces  

### Recommendations

- Don't expose OPENAI_API_KEY in browser
- Implement rate limiting for API calls
- Validate file sizes before processing
- Sanitize file content if displayed to users

---

## Deployment

### Local Development

```bash
uv run streamlit run main.py
```

### Production Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Connect to Streamlit Cloud
3. Set environment variables in cloud dashboard
4. Deploy!

### Docker Deployment

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install uv && uv sync
CMD ["streamlit", "run", "main.py"]
```

---

## Maintenance

### Adding New Features

1. Create a new module in appropriate layer
2. Update imports in dependent modules
3. Add docstrings and type hints
4. Test integration with main.py
5. Update README.md if needed

### Monitoring

- OpenAI API costs (track in settings)
- Error rates (log failures)
- User feedback (feature requests)

---

## Summary

Resume Critiquer is built on:
- **Clean Architecture** — Layered approach with clear boundaries
- **Dependency Injection** — Services receive dependencies
- **Single Responsibility** — Each module has one reason to change
- **Type Safety** — Full Python type annotations
- **Error Handling** — Multiple levels of error handling
- **Extensibility** — Easy to add features

This makes it **production-ready, maintainable, and scalable**.
