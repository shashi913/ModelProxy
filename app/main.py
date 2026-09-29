from fastapi import FastAPI
from pydantic import BaseModel

from app.llm_client import generate_response

app = FastAPI(title="ModelProxy", version="0.1.0")


class GenerateRequest(BaseModel):
    prompt: str


class GenerateResponse(BaseModel):
    response: str


@app.get("/health")
def health_check():
    """Basic liveness check used by load balancers / orchestrators."""
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "ModelProxy is running"}

@app.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    text = generate_response(request.prompt)
    return GenerateResponse(response=text)