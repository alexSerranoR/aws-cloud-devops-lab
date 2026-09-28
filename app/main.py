from fastapi import FastAPI

app = FastAPI(
    title="AWS Cloud DevOps Lab",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "AWS Cloud DevOps Lab API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "cloud-devops-api",
        "version": "0.1.0"
    }

@app.get("/info")
def info():
    return {
        "project": "AWS Cloud DevOps Lab",
        "environment": "local",
        "version": "0.1.0"
    }