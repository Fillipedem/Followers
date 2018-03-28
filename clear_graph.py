import networkx as nx
import matplotlib.pyplot as plt

# print options
file = "graphs/search.txt"
file_graph = "graphs/clean_graph.txt"

options = {
    'node_color': 'red',
    'node_size': 3,
    'width': 1
}

graph = nx.DiGraph()

with open(file, 'r') as f:

    count = 0
    for line in f:
        count += 1

        lista = line[:-1].split(";")

        u = lista[0]

        if u not in graph.node:
            graph.add_node(u)

        for v in lista[1:]:
            if v not in graph.node:
                graph.add_node(v)

            graph.add_edge(u, v)



# limpando grafo
nodes = graph.node
d_in = graph.in_degree(graph)
d_out = graph.out_degree(graph)

for n in graph.nodes():
    if d_out[n] == 0 or d_in == 0:
        graph.remove_node(n)

# writing results
with open(file_graph, 'w') as f:

    for user in graph.node:
        f.write(str(user))

        for edges in graph.edges(user):
            f.write(";" + str(edges[1]))

        f.write('\n')
