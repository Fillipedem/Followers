import networkx as nx
import matplotlib.pyplot as plt

# print options
options = {
    'node_color': 'red',
    'node_size': 3,
    'width': 1
}

graph = nx.DiGraph()


with open("search.txt", 'r') as f:

    count = 0
    for line in f:
        count += 1

        lista = line.split(";")

        u = lista[0]

        if u not in graph.node:
            graph.add_node(u)

        for v in lista[1:]:
            if v not in graph.node:
                graph.add_node(v)

            graph.add_edge(u, v)
            print(u, v)

    print(count)

print(graph.graph)

#graph.add_nodes_from([1, 2, 3, 4, 5])

#graph.add_edges_from([(1, 2), (3, 4), (5, 3), (5, 2)])

nx.draw(graph, with_labes=True, font_weight='bold', **options)
plt.show()
