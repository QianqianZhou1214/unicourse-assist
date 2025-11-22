from .search import VectorSearcher
from app.services.llm_client import generate_answer

class RAGPipeline:
    def __init__(self):
        self.searcher = VectorSearcher()
    
    def ask(self, query: str) -> str:
        # 1. Retrieve relevant documents
        docs = self.searcher.search(query, top_k=5)

        # 2. Combine chunks into context
        context = "\n\n".join(docs)

        # 3. Generate answer using LLM
        answer = generate_answer(query, context)

        return answer
    

if __name__ == "__main__":
    pipeline = RAGPipeline()
    question = "What are the courses in first semester of Applied Artificial Intelligence major?"
    answer = pipeline.ask(question)
    print("Question:", question)
    print("Answer:", answer)