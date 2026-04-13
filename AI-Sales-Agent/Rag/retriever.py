from rag.vector_store import VectorStore

store = VectorStore()

def retrieve_context(query: str):
    results = store.search(query)

    if not results:
        return "No relevant products found."

    formatted = []
    for r in results:
        formatted.append(f"{r['name']} - {r['description']}")

    return "\n".join(formatted)
