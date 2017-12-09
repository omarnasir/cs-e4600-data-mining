import networkx as nx
from networkx import DiGraph
import numpy as np

def task_0(graph, directed):
    if(directed):
        SCC_largest = max(nx.strongly_connected_component_subgraphs(graph), key=len)
    else:
        SCC_largest = max(nx.connected_component_subgraphs(graph), key=len)
    return SCC_largest, nx.info(SCC_largest)