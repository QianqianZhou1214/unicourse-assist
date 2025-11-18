def split_text(text str, chunk_size=300, overlap=50):
  """
  Splits the input text into chunks of specified size with overlap, for embedding.
  """
  chunks = []
  start = 0

  while start < len(text):
    end = start + chunck_size
    chunk = text[start:end]
    chunks.append(chunk)
    start = end - overlap
  return chunks