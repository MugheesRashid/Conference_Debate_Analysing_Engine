# visualization.py (optional)
import networkx as nx
import matplotlib.pyplot as plt

def plot_alliance_network(delegates, similarity_matrix, threshold=0.7):
    G = nx.Graph()

    # Add nodes
    for d in delegates:
        G.add_node(d)

    # Add edges based on similarity
    for i in range(len(delegates)):
        for j in range(i+1, len(delegates)):
            if similarity_matrix[i][j] > threshold:
                G.add_edge(delegates[i], delegates[j], weight=similarity_matrix[i][j])

    # Draw network
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={k: f"{v:.2f}" for k, v in labels.items()})
    plt.title("Delegate Alliance Network")
    plt.show()
