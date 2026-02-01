import json
from src.endee.endee_client import upsert_vector, create_index_if_not_exists
from src.endee.endee_client import upsert_vector
from sentence_transformers import SentenceTransformer # type: ignore
from src.endee.endee_client import upsert_vector

DATA_PATH = "data/documents.json"
MODEL_NAME = "all-MiniLM-L6-v2"

def load_documents(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    print("Loading embedding model...")
    model = SentenceTransformer(MODEL_NAME)

    print("Loading documents...")
    documents = load_documents(DATA_PATH)

    print(f"Found {len(documents)} documents")

    for idx, doc in enumerate(documents):
        text = doc["text"]

        print(f"Embedding document {idx + 1}...")
        embedding = model.encode(text).tolist()

        metadata = {
            "paper_id": doc["paper_id"],
            "paper_title": doc["paper_title"],
            "section": doc["section"],
            "text": text
        }

        upsert_vector(embedding, metadata)

    print("Ingestion completed successfully.")

if __name__ == "__main__":
    main()
