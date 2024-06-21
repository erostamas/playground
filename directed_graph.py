import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

# Add edges (directed)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)
G.add_edge(1, 3)

# Draw the graph
pos = nx.spring_layout(G)  # Position nodes using Fruchterman-Reingold force-directed algorithm
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=14, font_weight='bold', arrowsize=20)

# Draw edge labels
edge_labels = {(1, 2): '1-2', (2, 3): '2-3', (3, 4): '3-4', (4, 1): '4-1', (1, 3): '1-3'}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Show the plot
plt.show()
