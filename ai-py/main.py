from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="UniCourse AI Service",
    description="AI service for course navigation, RAG, MCP, and more.",
    version="0.1.0"
)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)

