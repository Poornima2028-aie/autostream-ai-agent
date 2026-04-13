import json

class VectorStore:
    def __init__(self, file_path="data/product_catalog.json"):
        with open(file_path, "r") as f:
            self.data = json.load(f)

    def search(self, query):
        results = []

        for item in self.data["products"]:
            if query.lower() in item["name"].lower():
                results.append(item)

        return results[:3]  # top 3 results
