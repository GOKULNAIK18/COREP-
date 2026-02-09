import numpy as np
from embedder import embed

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve_relevant_text(query, documents, top_k=3):
    doc_embeddings = embed(documents)
    query_embedding = embed([query])[0]

    scores = [
        cosine_similarity(query_embedding, doc_emb)
        for doc_emb in doc_embeddings
    ]

    top_indices = np.argsort(scores)[-top_k:][::-1]
    return "\n".join([documents[i] for i in top_indices])
