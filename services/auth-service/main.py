@app.get("/info")
def info():
    return {
        "service": "auth-service",
        "version": "v2",
        "description": "Authentication service for the platform - version 2"
    }
