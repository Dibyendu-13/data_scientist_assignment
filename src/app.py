# src/app.py
import numpy as np
from src.text_extraction import extract_text
from src.embedding import create_embeddings
from src.faiss_search import FAISSSearch
from src.keyword_search import keyword_search
from src.llm_answer import generate_answer
from src.rerank import rerank_results

def main():
    # Load and extract text from PDFs
    pdf_file = 'sample_pdfs/en/Blue_Ocean_Strategy,_Expanded_Edition_How_to_Create_Uncontested-2.pdf'
    text_data = extract_text(pdf_file)

    # Generate embeddings for the extracted text
    embeddings = create_embeddings(text_data)

    # Check the shape of the embeddings
    if embeddings.ndim == 1:
        embeddings = embeddings[np.newaxis, :]  # Ensure it's 2D

    # Instantiate the FAISSSearch class
    dimension = embeddings.shape[1]  # Assuming embeddings are 2D (num_samples, dimension)
    faiss_search = FAISSSearch(dimension)
    faiss_search.add_texts(embeddings, text_data)

    # Perform a query
    query = "What is the content of the PDF?"
    query_embedding = create_embeddings([query])  # Generate embedding for the query

    # Ensure the query_embedding is 2D
    if query_embedding.ndim == 1:
        query_embedding = query_embedding[np.newaxis, :]  # Ensure it's 2D

    # Perform FAISS search
    search_results = faiss_search.search(query_embedding, k=5)

    # Perform keyword-based search
    keyword_results = keyword_search(query, text_data)

    # Combine and rerank the results
    results = rerank_results(search_results, keyword_results)

    # Extract only the text parts from the results
    results_text = [text for text, _ in results]  # Assuming results is a list of tuples (text, distance)

    # Generate an answer using Cohere LLM based on the reranked results
    query = "What are the main points discussed in the PDF regarding deep learning?"
    context = "The document discusses various aspects of deep learning, including data distribution types and command prompts in programming."
    answer = generate_answer(query, context)  # Pass the improved context
    print("Answer:", answer)
    

if __name__ == '__main__':
    main()
