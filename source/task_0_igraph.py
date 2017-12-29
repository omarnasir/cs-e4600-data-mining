from igraph import *

class task_0:
    graph = None
    scc_largest = None
    
    def task_0(self, directed):
        print("------------------Computing SCCs--------------------")
        if(directed):
            self.scc_largest = max(self.graph.components(mode="STRONG"), key=len)            
        else:
            self.scc_largest = max(self.graph.components(mode="WEAK"), key=len)
        # Extract the subgraph for the largest connected component
        self.scc_largest = self.graph.subgraph(self.scc_largest)
        print("------------------Completed-----------------")
        return self.scc_largest.summary()

    def lscc_lwcc_generator(self):
        directed = False # Set to True/False for directed/undirected graphs
        filenames = ['wiki-Vote', 'soc-Epinions1', 'soc-Pokec', 'ego-Gplus']
        
        for file_obj in filenames:
            print("------------------Reading Graph From Disk--------------------")
            self.graph = Graph.Read_Ncol('./data/' + file_obj + '.txt', directed=directed)
            print("------------------Reading Completed-----------------")

            # Compute Connected components
            info = self.task_0(directed)
            
            if(directed):
                ext = '_LSCC.gz'
            else:
                ext = '_LWCC.gz'
            
            print("------------------Graph Summary--------------------")
            print("Graph Name: " + file_obj)
            print("Edges/Vertices: " + info.split("-- ")[1])
            
            print("------------------Writing LCCs to Disk--------------------")
            self.scc_largest.write_graphmlz(f='./outputs/'+ file_obj + ext)
            print("------------------Completed-----------------")

def main():
    obj = task_0()
    obj.lscc_lwcc_generator()

if __name__ == "__main__":
    main()