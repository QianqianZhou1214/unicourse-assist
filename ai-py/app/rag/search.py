import chromadb

class VectorSearcher:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="../vector_store")
        self.collection = self.client.get_or_create_collection(
            name="courses:",
            metadata={"hnsw:space": "cosine"}
        )
    
    def search(self, query: str, top_k: int = 5):
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )
        
        documents = results['documents'][0]

        return documents