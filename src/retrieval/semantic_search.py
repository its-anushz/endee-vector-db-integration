import os
import requests
from sentence_transformers import SentenceTransformer

ENDEE_ENDPOINT = os.getenv("ENDEE_ENDPOINT", "http://localhost:8080")
INDEX_NAME = "academic_papers"
MODEL_NAME = "all-MiniLM-L6-v2"

def search(query, top_k=3):
    model = SentenceTransformer(MODEL_NAME)
    query_vector = model.encode(query).tolist()

    params = {
        "k": top_k
        # vector will be added once we confirm API format
    }

    response = requests.get(
        f"{ENDEE_ENDPOINT}/api/v1/indexes/{INDEX_NAME}/vectors",
        params=params
    )

    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    query = input("Enter your search query: ")
    results = search(query)

    print("\nSearch Results:\n")
    print(results)
