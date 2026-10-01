import os
from dotenv import load_dotenv
import requests
from groq import Groq

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_URL = f"{OLLAMA_BASE_URL}/api/generate"
OLLAMA_MODEL = "llama3.2:1b"

GROQ_MODEL = "openai/gpt-oss-20b"


def _generate_with_ollama(prompt: str) -> str:
    payload = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=payload, timeout=60)
    response.raise_for_status()
    return response.json()["response"]


def _generate_with_groq(prompt: str) -> str:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    completion = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content


def generate_response(prompt: str) -> str:
    """Generate a response using the configured LLM provider (ollama or groq)."""
    provider = os.getenv("LLM_PROVIDER", "ollama")
    if provider == "groq":
        return _generate_with_groq(prompt)
    return _generate_with_ollama(prompt)