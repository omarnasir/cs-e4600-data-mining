from networkx import write_gpickle, read_gpickle
from networkx import DiGraph, Graph, read_edgelist
import networkx as nx
import igraph

class task_0:
    graph = None
    SCC_largest = None

    def read_graph(self, filename, isdirected):
        print("------------------Reading Graph From Disk--------------------")
        if (isdirected):
            self.graph = read_edgelist(filename,create_using=DiGraph())
        else:
            self.graph = read_edgelist(filename)  
        print("------------------Reading Completed-----------------")
    
    def task_0(self, directed):
        print("------------------Computing SCCs--------------------")
        if(directed):
            self.SCC_largest = max(nx.strongly_connected_component_subgraphs(self.graph), key=len)
        else:
            self.SCC_largest = max(nx.connected_component_subgraphs(self.graph), key=len)
        print("------------------Completed-----------------")
        return nx.info(SCC_largest)

    def lscc_lwcc_generator(self):
        directed = True
        filenames = ['ego-Gplus']
        # filenames = ['wiki-Vote', 'soc-Epinions1', 'soc-Pokec', 'ego-Gplus']
        for file_obj in filenames:
            self.read_graph('D:/Project/data/' + file_obj + '.txt', directed)
            # self.read_graph('C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/data/' + file_obj + '.txt', directed
            #For Cloud
            # self.read_graph('./data/' + file_obj + '.txt', directed)
            info = task_0(self.graph, directed)
            if(directed):
                ext = '_LSCC.txt'
            else:
                ext = '_LWCC.txt'

            write_gpickle(self.SCC_largest,'D:/Project/outputs/'+ file_obj + ext)
            # write_gpickle(self.SCC_largest,'C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/outputs/'+ file_obj + ext)
            #For Cloud
            # write_gpickle(SCC_largest,'./outputs/'+ file_obj + ext)
            print(info)
            print("Iteration finished")

def main():
    obj = task_0()
    obj.lscc_lwcc_generator()

if __name__ == "__main__":
    main()