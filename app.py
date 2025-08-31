from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
import os

app = FastAPI()

# Read secret that will be injected via GitHub Actions -> HF Space Secrets
MY_API_KEY = os.getenv("MY_API_KEY")

@app.get("/")
def root():
    return FileResponse("index.html")

@app.get("/hello")
def hello(name: str = "World"):
    if not MY_API_KEY:
        return JSONResponse({"error": "API key not set in Space Secrets"}, status_code=500)
    return {"message": f"Hello {name}! ✅ Secure backend is working with a secret injected from GitHub."}
