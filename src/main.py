from loader import load_data
from preprocess import preprocess_dataframe
from features import add_features
from vectorizer import delegate_similarity
from influence import calculate_influence
from volatility import calculate_volatility
from report import generate_report
from alliance import plot_alliance_network
from bloc_detector import detect_blocs

import pandas as pd

def main():
    
    data = load_data("./data/sample_session.csv")

    df = pd.DataFrame(data)

    df = preprocess_dataframe(df)

    df = add_features(df)

    delegates, similarity_matrix = delegate_similarity(df)

    blocs = detect_blocs(delegates, similarity_matrix, num_blocs=2)
    
    influence_table = calculate_influence(df, similarity_matrix)

    volatility = calculate_volatility(df)

    generate_report(df, delegates, similarity_matrix, influence_table, volatility, blocs)
    
    plot_alliance_network(delegates, similarity_matrix)

if __name__ == "__main__":
    main()