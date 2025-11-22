from sentence_transformers import SentenceTransformer

model = SentenceTransformer("multi-qa-mpnet-base-dot-v1")

def embed_texts(texts: list[str], batch_size: int = 32) -> list[list[float]]:
    """
    Generate embeddings for a list of texts in batches.
    Returns list of embeddings (list of floats).
    """
    embeddings = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        batch_embeddings = model.encode(batch, show_progress_bar=False).tolist()
        embeddings.extend(batch_embeddings)
    return embeddings