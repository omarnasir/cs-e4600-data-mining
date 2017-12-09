import networkx as nx
from networkx import DiGraph
import numpy as np

def largest_scc(SCC_list):
    #Find the largest SCC
    return max(SCC_list, key=len)

def size_SCC(SCC_largest, g):
    num_nodes = len(SCC_largest)
    num_edges = 0
    for node in SCC_largest:
        for edge in g.adj[node]:
            if edge in SCC_largest:
                num_edges += 1
    return num_nodes, num_edges

def task_0(graph, strong):
    if(strong):
        SCC_list = nx.strongly_connected_components(graph)
    else:
        SCC_list = nx.weakly_connected_components(graph)
    SCC_largest = largest_scc(SCC_list)
    num_nodes, num_edges = size_SCC(SCC_largest, graph)
    return SCC_largest, num_nodes, num_edges