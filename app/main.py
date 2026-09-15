from fastapi import FastAPI

app = FastAPI(title="ModelProxy", version="0.1.0")

@app.get("/health")
def health_check():
    """Basic liveness check used by load balancers / orchestrators."""
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "ModelProxy is running"}