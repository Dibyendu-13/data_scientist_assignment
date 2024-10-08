from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # Load your model here

def create_embeddings(text_list):
    # Ensure text_list is a list of strings
    embeddings = model.encode(text_list, show_progress_bar=True)  # Use the list directly
    return embeddings
