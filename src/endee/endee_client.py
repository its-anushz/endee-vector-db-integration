def upsert_vector(vector, metadata):
    """
    Insert a vector + metadata into the Endee index.
    """
    payload = {
        "vectors": [
            {
                "vector": vector,
                "metadata": metadata
            }
        ]
    }

    response = requests.post(
        f"{ENDEE_ENDPOINT}/api/v1/indexes/{INDEX_NAME}/vectors",
        json=payload
    )

    response.raise_for_status()
    return response.json()
