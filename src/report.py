# report.py

import pandas as pd
import numpy as np

def generate_report(df, delegates, similarity_matrix, influence_table, volatility_score, blocs):
    """
    Generates a structured session summary report.
    """

    print("\n================ Debate Intelligence Engine Report ================\n")

    num_delegates = df["delegate"].nunique()
    num_speeches = len(df)
    print(f"Total Delegates: {num_delegates}")
    print(f"Total Speeches: {num_speeches}")
    print(f"Debate Volatility Index: {volatility_score:.4f}\n")

    print("Top Influential Delegates:")
    print(influence_table[["delegate", "influence_score"]].head(5))
    print("\n")

    print("Probable Alliances (Similarity > 0.7):")
    delegate_names = list(delegates)
    alliances_found = False

    for i in range(len(delegate_names)):
        for j in range(i+1, len(delegate_names)):
            if similarity_matrix[i][j] > 0.7:
                print(f"- {delegate_names[i]} ↔ {delegate_names[j]} (Similarity: {similarity_matrix[i][j]:.2f})")
                alliances_found = True

    if not alliances_found:
        print("No strong alliances detected.\n")


    print("\nDetected Blocs:")
    for bloc_id, members in blocs.items():
        print(f"Bloc {bloc_id + 1}: {', '.join(members)}")


    avg_cooperation = df["Coorporative_Index"].mean()
    avg_assertiveness = df["Assertive_Index"].mean()
    avg_stance = df["stance_score"].mean()
    print(f"Average Cooperation Index: {avg_cooperation:.4f}")
    print(f"Average Assertiveness Index: {avg_assertiveness:.4f}")
    print(f"Average Stance Score: {avg_stance:.4f}\n")

    print("==================================================================\n")
