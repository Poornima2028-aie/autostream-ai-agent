def get_embedding(text: str):
    """
    Mock embedding function (for learning purpose)
    In real project: use OpenAI / SentenceTransformers
    """
    return [len(text), sum(ord(c) for c in text) % 1000]
