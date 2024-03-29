import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_car_info(input_string):
    pattern = r'([\u0590-\u05FF\w]+)-(\w+-\d+)\s+(\d{4})'
    match = re.search(pattern, input_string)
    if match:
        car_name = match.group(1).strip()
        model_number = match.group(2).strip()
        year = match.group(3).strip()
        return car_name, model_number, year
    else:
        return None

def most_similar_text(query, texts):
    # Convert texts to numerical representation (e.g., TF-IDF vectors)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    
    # Convert the query to the same numerical representation
    query_vec = vectorizer.transform([query])
    
    # Calculate cosine similarity between the query and all texts
    similarities = cosine_similarity(X, query_vec)
    
    # Get the index of the most similar text
    most_similar_idx = similarities.argmax()
    
    # Return the most similar text
    return texts[most_similar_idx]