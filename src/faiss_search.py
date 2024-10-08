import faiss
import numpy as np

class FAISSSearch:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)  # Using L2 distance
        self.texts = []

    def add_texts(self, embeddings, texts):
        self.index.add(embeddings)  # Add embeddings to the index
        self.texts.extend(texts)

    def search(self, query_embedding, k=5):
     distances, indices = self.index.search(query_embedding, k)
     # Return a list of tuples containing text and corresponding distance
     return [(self.texts[i], float(distances[0][j])) for j, i in enumerate(indices[0])]

