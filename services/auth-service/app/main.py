from fastapi import FastAPI

app = FastAPI(title="Auth Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {
        "service": "auth-service",
        "version": "v3",
        "description": "Authentication service for the platform - version 3"
    }

