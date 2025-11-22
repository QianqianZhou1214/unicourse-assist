import chromadb
import os
from app.ingest.embed import embed_texts

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(THIS_DIR, "..", ".."))
VECTOR_DIR = os.path.join(ROOT_DIR, "app", "vector_store")

class VectorSearcher:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=VECTOR_DIR)
        self.collection = self.client.get_or_create_collection(
            name="courses",
            metadata={"hnsw:space": "cosine"}
        )
    
    def search(self, query: str, top_k: int = 5):
        query_embedding = embed_texts([query])[0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        documents = results['documents'][0]

        return documents