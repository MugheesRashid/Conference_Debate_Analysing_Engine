import pandas as pd
import numpy as np

def calculate_influence(df, similarity_matrix, alpha=0.4, beta=0.3, gamma=0.3):
    grouped = df.groupby("delegate").agg({
        "stance_score": "mean",
        "text_length": "count",
    }).reset_index()

    grouped["stance_intensity"] = grouped["stance_score"].abs()

    total_speeches = grouped["text_length"].sum()
    grouped["speech_ratio"] = grouped["text_length"] / total_speeches

    centrality_scores = similarity_matrix.mean(axis=1)
    grouped["centrality"] = centrality_scores

    grouped["influence_score"] = (
        alpha * grouped["stance_intensity"] +
        beta * grouped["speech_ratio"] +
        gamma * grouped["centrality"]
    )

    return grouped.sort_values(by="influence_score", ascending=False)