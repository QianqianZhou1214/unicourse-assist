import os
from extract import extract_pdf, extract_html
from chunk import chunk_text
from embed import embed_texts
import chromadb

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(THIS_DIR, "..", ".."))
DATA_DIR = os.path.join(ROOT_DIR, "app","data")
VECTOR_DIR = os.path.join(ROOT_DIR, "app", "vector_store")


def ingest_file(path: str, collection):
    """Ingest a single PDF/HTML file into ChromaDB."""
    base_name = os.path.basename(path)

    if path.endswith(".pdf"):
        text = extract_pdf(path)
    elif path.endswith(".html") or path.endswith(".htm"):
        text = extract_html(path)
    else:
        print("Unsupported file:", path)
        return

    # chunking
    chunks = chunk_text(text)

    existing_ids = set(collection.get()["ids"])
    new_chunks = []
    new_ids = []
    for idx, chunk in enumerate(chunks):
        cid = f"{base_name}-{idx}"
        if cid not in existing_ids:
            new_chunks.append(chunk)
            new_ids.append(cid)

    if not new_chunks:
        print(f"⚡ Skipping {base_name}, already ingested.")
        return

    # embedding
    embeddings = embed_texts(new_chunks)

    # insert into ChromaDB
    collection.add(
        documents=new_chunks,
        embeddings=embeddings,
        ids=new_ids
    )
    print(f"[OK] Ingested {base_name}: {len(new_chunks)} new chunks")


def run_ingest(data_dir=DATA_DIR):
 
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
