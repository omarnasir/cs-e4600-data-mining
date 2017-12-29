import networkx as nx
from networkx import DiGraph
import numpy as np

#Explore algorithm from DFS
def explore(g, node, node_neighbours, visited, order, stack):
    stack.append(node)
    visited.add(node)
    for neighbour in node_neighbours:
        if neighbour not in visited:
            visited, order, stack = explore(g, neighbour, g.adj[neighbour], visited, order, stack)
    order.append(node)
    stack.pop()
    return visited, order, stack

# coding: utf-8
def get_reverse_post(digraph):
    #Visited contains nodes in graph we have already visited
    visited = set()
    #Order contains visited nodes in the order you exit them in the exploration
    order = []
    #Direction of exploration, only contains nodes of 1 SCC
    stack = [] 
    #This loop ensures you traverse the whole network
    #Depends on choice of first node, whether it gives a tree or a forest
    for node in digraph.nodes():
        if node not in visited:
            visited, order, stack = explore(digraph, node, digraph.adj[node], visited, order, stack)
    #Reverse order of visited nodes, based on post values
    return list(reversed(order))

def get_sccs(digraph, rev_post):
    #Visited contains nodes in graph we have already visited
    visited = set()
    #Order contains visited nodes in the order you exit them in the exploration
    order = []
    #Direction of exploration, only contains nodes of 1 SCC
    stack = [] 

    SCC_list = []
    #This loop ensures you traverse the whole network
    #Depends on choice of first node, whether it gives a tree or a forest
    for node in rev_post:
        if node not in visited:
            visited, order, stack = explore(digraph, node, digraph.adj[node], visited, order, stack)
            #Append nodes from 1 SCC to SCC_list
            #Clear order array to find set of nodes in next SCC
            SCC_list.append(order)
            order = []

    #Reverse order of visited nodes, based on post values
    return SCC_list

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

# def main():
    #------------Testing Purposes--------------
    # graph = nx.DiGraph({4: [2,3], 2: [1], 1: [4], 3 :[0], 0:[]})
    #Run DFS on Graph and extract list of visited nodes in reverse order of how we pop the stack
    # rev_post = get_reverse_post(graph)
    #Reverse the graph in memory without creating a copy
    # g_reverse = graph.reverse(copy=True)
    # SCC_list = get_sccs(g_reverse,rev_post)
    # SCC_largest = largest_scc(SCC_list)
    # num_nodes, num_edges = size_SCC(SCC_largest, graph)
    # print(SCC_largest, num_nodes, num_edges)

# if __name__=="__main__":
#     main()