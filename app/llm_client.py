import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "llama3.2:1b"

def generate_response(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """send a prompt to the local Ollama server and return the generated text."""
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=60)
    response.raise_for_status()
    data = response.json()
    return data["response"]