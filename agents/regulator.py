from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Load regulation documents
def load_regulations():

    with open("rag/regulations.txt", "r") as f:
        docs = f.read().split("\n\n")

    return docs


# Build vector index
def build_index(docs):

    embeddings = model.encode(docs)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return index, embeddings


# Retrieve relevant regulation
def retrieve_regulation(query):

    docs = load_regulations()
    index, embeddings = build_index(docs)

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), k=1)

    return docs[indices[0][0]]


def run_regulator(investigation_results):

    enriched_results = []

    for item in investigation_results:

        investigation_text = item["investigation"]

        regulation = retrieve_regulation(investigation_text)

        enriched_results.append({
            "transaction": item["transaction"],
            "investigation": investigation_text,
            "regulation": regulation
        })

    return enriched_results