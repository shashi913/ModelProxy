from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_generate_endpoint():
    fake_response = "Hello there!"
    with patch("app.main.generate_response", return_value=fake_response):
        response = client.post("/generate", json={"prompt": "Say hi"})
    assert response.status_code == 200
    assert response.json() == {"response": "Hello there!"}

def test_generate_with_groq_provider(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "groq")
    fake_response = "Hi from Groq!"
    with patch("app.llm_client._generate_with_groq", return_value=fake_response):
        from app.llm_client import generate_response
        result = generate_response("Say hi")
    assert result == "Hi from Groq!"