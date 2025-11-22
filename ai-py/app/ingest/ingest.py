import os
from extract import extract_pdf, extract_html
from chunk import chunk_text
from embed import embed_texts
import chromadb

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

ROOT_DIR = os.path.abspath(os.path.join(THIS_DIR, "..", ".."))
DATA_DIR = os.path.join(ROOT_DIR, "app","data")
VECTOR_DIR = os.path.join(ROOT_DIR, "app", "vector_store")
os.makedirs(VECTOR_DIR, exist_ok=True)

print("ROOT_DIR =", ROOT_DIR)
print("DATA_DIR =", DATA_DIR)
print("VECTOR_DIR =", VECTOR_DIR)


def ingest_file(path: str, collection):
    """
    Selects the appropriate extractor based on file type.
    """
    if path.endswith('.pdf'):
        text = extract_pdf(path)
    elif path.endswith('.html') or path.endswith('.htm'):
        text = extract_html(path)
    else:
        print(f"Unsupported file type: {path}")
        return
    
    #chunking
    chunks = chunk_text(text)

    #embedding
    embeddings = embed_texts(chunks)

    #storing in vector db
    ids = [f"{os.path.basename(path)}-{i}" for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )

    print(f"[OK] Ingested {path} with {len(chunks)} chunks.")


def run_ingest(data_dir=DATA_DIR):
    print("Using data directory:", data_dir)
    chroma = chromadb.PersistentClient(path=VECTOR_DIR)

    collection = chroma.get_or_create_collection(
        name="courses",
        metadata={"hnsw:space": "cosine"}
    )

    for file in os.listdir(data_dir):
        path = os.path.join(data_dir, file)
        ingest_file(path, collection)

if __name__ == "__main__":
    run_ingest()