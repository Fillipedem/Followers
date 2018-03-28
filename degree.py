"""
Plota número de Graus para cada nó
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

graph = read_graph(file)

degree_sequence = sorted(nx.degree(graph).values(), reverse=True)
dmax = max(degree_sequence)

plt.plot(degree_sequence)
plt.title("Graus em cada Nó")
plt.ylabel("Grau")
plt.xlabel("Nós")

# draw graph in inset
plt.axes([0.45, 0.45, 0.45, 0.45])
plt.axis('off')
plt.show()

