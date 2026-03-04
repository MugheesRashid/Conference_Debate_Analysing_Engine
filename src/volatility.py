import numpy as np

def calculate_volatility(df):
    stance_values = df["stance_score"]

    volatility = np.std(stance_values)
    return volatility
