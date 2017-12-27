from igraph import *

class task_0:
    graph = None
    SCC_largest = None

    def read_graph(self, filename, isdirected):
        print("------------------Reading Graph From Disk--------------------")
        self.graph = Graph.Read_Ncol(filename, directed=isdirected)  
        print("------------------Reading Completed-----------------")
    
    def task_0(self, directed):
        print("------------------Computing SCCs--------------------")
        if(directed):
            self.SCC_largest = max(self.graph.components(mode="STRONG"), key=len)            
        else:
            self.SCC_largest = max(self.graph.components(mode="WEAK"), key=len)
        self.SCC_largest = self.graph.subgraph(self.SCC_largest)
        print("------------------Completed-----------------")
        return self.SCC_largest.summary()

    def lscc_lwcc_generator(self):
        directed = False
        filenames = ['soc-Pokec']
        # filenames = ['wiki-Vote', 'soc-Epinions1', 'soc-Pokec', 'ego-Gplus']
        for file_obj in filenames:
            ### Local computing
            self.read_graph('D:/Project/data/' + file_obj + '.txt', directed)
            # self.read_graph('C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/data/' + file_obj + '.txt', directed
            ### For Aalto Notebooks
            # self.read_graph('./data/' + file_obj + '.txt', directed)
            info = self.task_0(directed)
            if(directed):
                ext = '_LSCC.txt'
            else:
                ext = '_LWCC.txt'
            print("------------------Graph Summary--------------------")
            print("Graph Name: " + file_obj)
            print("Edges/Vertices: " + info)
            print("------------------Writing LCCs to Disk--------------------")
            ### Local computing
            self.SCC_largest.write_graphmlz(f='D:/Project/outputs_igraph/'+ file_obj + ext)
            # self.SCC_largest.write_graphmlz(f='C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/outputs/'+ file_obj + ext)
            ### For Aalto Notebooks
            # self.SCC_largest.write_graphmlz(f='./outputs/'+ file_obj + ext)
            print("------------------Completed-----------------")
            print("Iteration finished")

def main():
    obj = task_0()
    obj.lscc_lwcc_generator()

if __name__ == "__main__":
    main()