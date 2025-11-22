from search import VectorSearcher
from services.llm_client import generate_answer

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