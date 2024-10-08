from sklearn.feature_extraction.text import TfidfVectorizer

def keyword_search(query, text_data):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text_data])
    
    query_vector = vectorizer.transform([query])
    scores = (tfidf_matrix * query_vector.T).toarray()
    
    # Get top matching sentences
    top_indices = scores.argsort()[0][::-1][:5]
    return [text_data.splitlines()[i] for i in top_indices]
