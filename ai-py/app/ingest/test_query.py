from embed import embed_texts
import os
import chromadb

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(THIS_DIR, "..", ".."))
DATA_DIR = os.path.join(ROOT_DIR, "app","data")
VECTOR_DIR = os.path.join(ROOT_DIR, "app", "vector_store")

chroma = chromadb.PersistentClient(path=VECTOR_DIR)
coll = chroma.get_or_create_collection("courses")

query_text = "what is theoretical computer science?"

# generating HuggingFace embedding
query_embedding = embed_texts([query_text])[0]

# query
results = coll.query(
    query_embeddings=[query_embedding],
    n_results=5
)

print(results)