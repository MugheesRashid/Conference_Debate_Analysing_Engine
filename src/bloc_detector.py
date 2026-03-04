# bloc_detector.py

import numpy as np
from sklearn.cluster import AgglomerativeClustering

def detect_blocs(delegates, similarity_matrix, num_blocs=2):
    """
    Automatically groups delegates into blocs
    based on speech similarity.
    """

    # Convert similarity to distance
    # Clustering works on distance (low = close)
    distance_matrix = 1 - similarity_matrix

    # Create clustering model
    model = AgglomerativeClustering(
        n_clusters=num_blocs,
        metric="precomputed",
        linkage="average"
    )

    # Fit model
    labels = model.fit_predict(distance_matrix)

    # Organize delegates into blocs
    blocs = {}

    for delegate, label in zip(delegates, labels):
        if label not in blocs:
            blocs[label] = []
        blocs[label].append(delegate)

    return blocs