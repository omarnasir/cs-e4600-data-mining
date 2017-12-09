from networkx import DiGraph
from graph_reader import read_graph
from task_0 import task_0

if __name__ == "__main__":
    isstrong = True
    # filenames = ['Wiki-Vote', 'soc-Epinions1']
    filenames = ['Wiki-Vote', 'soc-Epinions1', 'soc-Pokec', 'ego_Gplus']
    for file_obj in filenames:
        graph = read_graph('./data/' + file_obj + '.txt')
        SCC_largest, num_nodes, num_edges = task_0(graph, isstrong)
        print(num_nodes, num_edges)