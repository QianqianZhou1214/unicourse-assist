from fastapi import FastAPI
from pydantic import BaseModel
from app.rag.pipeline import RAGPipeline
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RAG Server API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline = RAGPipeline()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    """
    Endpoint to ask questions about courses.
    """
    answer = pipeline.ask(request.question)
    return {"question": request.question, "answer": answer}