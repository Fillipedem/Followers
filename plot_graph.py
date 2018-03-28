"""
Plotar Grafo Direcionado e Não Direcionado
"""
import networkx as nx
import matplotlib.pyplot as plt
from helper import read_graph, read_digraph

# print options
file = "graphs\clean_graph.txt"

options = {
    'node_color': 'red',
    'node_size': 5,
    'width': 0.5
}

# read graph
graph = read_graph()

# plot
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labes=True, font_weight='bold', **options)
plt.show()
