import networkx as nx
import matplotlib.pyplot as plt

def draw_network():
    G = nx.Graph()

    # Example network
    G.add_edge("Router", "Laptop")
    G.add_edge("Router", "Mobile")
    G.add_edge("Router", "SmartTV")

    nx.draw(G, with_labels=True, node_color='green')

    plt.savefig("static/network.png")
    plt.close()