import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

DATA_DIR = "data"
INDEX_DIR = "embeddings"
INDEX_PATH = os.path.join(INDEX_DIR, "index.faiss")

def load_documents():
    docs = []
    for file in os.listdir(DATA_DIR):
        if file.endswith(".txt"):
            with open(os.path.join(DATA_DIR, file), "r") as f:
                text = f.read()
                # simple chunking by paragraph
                chunks = [c.strip() for c in text.split("\n\n") if c.strip()]
                docs.extend(chunks)
    return docs

def build_faiss_index(documents):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(documents, show_progress_bar=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    os.makedirs(INDEX_DIR, exist_ok=True)
    faiss.write_index(index, INDEX_PATH)

    return documents

if __name__ == "__main__":
    docs = load_documents()
    build_faiss_index(docs)
    print(f"FAISS index created at {INDEX_PATH}")
