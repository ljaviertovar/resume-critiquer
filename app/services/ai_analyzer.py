"""AI-powered resume analysis using OpenAI API with streaming."""

from typing import Generator
from openai import OpenAI
from app.config import Settings


class AIAnalyzer:
    """Analyzes resumes using OpenAI API with streaming support."""

    def __init__(self, settings: Settings):
        """
        Initialize AIAnalyzer with configuration.

        Args:
            settings: Application settings containing OpenAI credentials
        """
        self.settings = settings
        self.client = OpenAI(api_key=settings.openai_api_key)

    def analyze(self, resume_text: str, job_role: str = "") -> Generator[str, None, None]:
        """
        Analyze resume and yield AI feedback chunks in real-time.

        Args:
            resume_text: The extracted resume text
            job_role: Target job role for tailored analysis (optional)

        Yields:
            Text chunks as they arrive from OpenAI
        """
        prompt = self._build_prompt(resume_text, job_role)

        with self.client.chat.completions.create(
            model=self.settings.openai_model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert resume reviewer with 20+ years of experience in HR, recruitment, and ATS systems. "
                    "Provide constructive, specific, actionable feedback in English using a clear structured format.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=self.settings.temperature,
            max_tokens=self.settings.max_tokens,
            stream=True,
        ) as response:
            for chunk in response:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content

    @staticmethod
    def _build_prompt(resume_text: str, job_role: str) -> str:
        """Build the analysis prompt with structured output format."""
        job_context = (
            f"\nSpecific focus: optimize the resume for a {job_role} role."
            if job_role
            else "\nGeneral focus: optimize the resume for better visibility in the job market."
        )

        return f"""Analyze the following resume and provide comprehensive, actionable feedback using this exact structure:

## Overall Score
Rate the resume quality from 0 to 10 and include a brief explanation.

## Strengths
List 3 to 5 key strengths as bullet points.

## Areas for Improvement
List 3 to 5 specific points that need work.

## Recommendations
Provide 5 concrete, actionable recommendations to improve the resume.{job_context}

## ATS Optimization
- Missing or underrepresented keywords
- Possible formatting issues for ATS systems
- Suggested content to add

---

RESUME TO ANALYZE:
{resume_text}"""
