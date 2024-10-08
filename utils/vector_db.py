from faiss_search import FAISSSearch

class VectorDatabase:
    def __init__(self, dimension):
        self.search = FAISSSearch(dimension)

    def add_documents(self, embeddings, texts):
        self.search.add_texts(embeddings, texts)

    def query(self, query_embedding, k=5):
        return self.search.search(query_embedding, k)
