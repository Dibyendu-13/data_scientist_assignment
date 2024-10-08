def rerank_results(search_results, keyword_results):
    # Convert the results to tuples to make them hashable
    search_results_tuples = [(text, float(distance)) for text, distance in search_results]
    keyword_results_tuples = [(text, 0) for text in keyword_results]  # Assuming distance is 0 for keyword results

    # Merge and remove duplicates by converting to a set
    combined_results = list(set(search_results_tuples) | set(keyword_results_tuples))
    

    combined_results.sort(key=lambda x: x[1])  # Sort by distance if you have distances

    return combined_results
