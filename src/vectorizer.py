import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_tfidf_matrix(df):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df["clean_speech"])
    return tfidf_matrix, vectorizer

def compute_similarity(tfidf_matrix):
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

def delegate_similarity(df):
    grouped = df.groupby("delegate")["clean_speech"].apply(" ".join).reset_index()
    tfidf_matrix, vectorizer = build_tfidf_matrix(grouped)
    similarity_matrix = compute_similarity(tfidf_matrix)
    return grouped["delegate"] , similarity_matrix


if __name__ == "__main__":

    data = {
        "delegate": ["France", "Germany", "France"],
        "clean_speech": [
            "support unity cooperation",
            "reject proposal condemn",
            "encourage partnership dialogue"
        ]
    }

    df = pd.DataFrame(data)

    delegates, sim_matrix = delegate_similarity(df)

    print("Delegates:")
    print(delegates)

    print("\nSimilarity Matrix:")
    print(sim_matrix)