from networkx import DiGraph, Graph, read_edgelist
from networkx import Graph
import numpy as np

def read_graph(filename, isdirected):
    print("------------------Reading Graph--------------------")
    if (isdirected):
        G = read_edgelist(filename,create_using=DiGraph())
    else:
        G = read_edgelist(filename)  
    print("------------------Reading Completed-----------------")
    return G