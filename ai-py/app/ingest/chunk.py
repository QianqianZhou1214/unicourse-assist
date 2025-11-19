def chunk_text(text: str, chunk_size=400, overlap=100):
    """
    Chunks the input text into smaller pieces with specified size and overlap for embedding.
    """

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks
  