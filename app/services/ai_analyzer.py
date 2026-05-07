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
                    "content": "Eres una persona experta en revisión de CVs con más de 20 años de experiencia en HR, reclutamiento y sistemas ATS. "
                    "Entrega feedback constructivo, específico y accionable en español, usando un formato estructurado y fácil de leer.",
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
            f"\nEnfoque específico: optimiza el CV para el puesto de {job_role}."
            if job_role
            else "\nEnfoque general: optimiza el CV para mayor visibilidad en el mercado laboral."
        )

        return f"""Analiza el siguiente CV y entrega feedback completo y accionable con esta estructura exacta:

## Puntuación general
Califica la calidad del CV de 0 a 10 e incluye una explicación breve.

## Fortalezas
Lista de 3 a 5 fortalezas principales en viñetas.

## Áreas de mejora
Lista de 3 a 5 puntos específicos que necesitan trabajo.

## Recomendaciones
Entrega 5 recomendaciones concretas y accionables para mejorar el CV.{job_context}

## Optimización ATS
- Keywords faltantes o poco visibles
- Posibles problemas de formato para sistemas ATS
- Contenido sugerido para agregar

---

CV A ANALIZAR:
{resume_text}"""
