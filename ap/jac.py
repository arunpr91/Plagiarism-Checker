def jaccard_similarity(doc1, doc2):
    # Calculate Jaccard Similarity
    intersection = len(doc1.intersection(doc2))
    union = len(doc1.union(doc2))
    similarity = intersection / union
    return similarity
