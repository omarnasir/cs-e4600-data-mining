from networkx import DiGraph
from networkx import Graph

def read_graph(filename):
    G = DiGraph()
    with open(filename) as f:
        for line in f:
            tokens = line.split()
            if tokens[0] not in G.nodes():
                G.add_node(int(tokens[0]))
            G.add_edge(int(tokens[0]),int(tokens[1]))
    return G
