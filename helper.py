import networkx as nx

def read_graph(file):

    graph = nx.Graph()

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

    return graph

def read_digraph(file):

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

    return graph


