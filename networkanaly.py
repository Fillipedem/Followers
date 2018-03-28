"""
Analise de PageRank/Hubs/Authorities
"""
import networkx as nx
import matplotlib.pyplot as plt
from helper import read_graph, read_digraph

# print options
file = r"graphs\clean_graph.txt"
file_auth = r"graphs\auth.txt"
file_hubs = r"graphs\hubs.txt"
file_pr = r"graphs\pagerank.txt"

options = {
    'node_color': 'red',
    'node_size': 5,
    'width': 0.5
}

# read graph
graph = read_digraph(file)

# hubs and authorites
hubs, auth = nx.hits(graph)

# Page Rank
pr = nx.pagerank(graph, alpha=0.95)


# Salvando ranks
# Page Rank
sorted_pr = sorted(pr.keys(), key=lambda x: pr[x], reverse=True)

with open(file_pr, 'w') as f:
    for user in sorted_pr:
        f.write(str(user) + " : " + str(pr[user]) + "\n")

# Hubs
sorted_hubs = sorted(hubs.keys(), key=lambda x: hubs[x], reverse=True)

with open(file_hubs, 'w') as f:
    for user in sorted_hubs:
        f.write(str(user) + " : " + str(hubs[user]) + "\n")

# Auth
sorted_auth = sorted(auth.keys(), key=lambda x: auth[x], reverse=True)

with open(file_auth, 'w') as f:
    for user in sorted_auth:
        f.write(str(user) + " : " + str(auth[user]) + "\n")


# Hubs Print
graph = read_graph(file)
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labes=True, font_weight='bold', **options)
plt.show()

lista = sorted_pr
nx.draw(graph, pos, with_labes=True, font_weight='bold', **options)
nx.draw_networkx_nodes(graph, pos,
                        nodelist=lista[33:35],
                        node_color='b',
                        node_size=10,
                    alpha=0.8)
plt.show()

plt.show()
