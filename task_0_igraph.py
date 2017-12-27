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
        directed = False # Set to True for directed graphs
        filenames = ['wiki-Vote', 'soc-Epinions1', 'soc-Pokec', 'ego-Gplus']
        
        for file_obj in filenames:
            print("------------------Reading Graph From Disk--------------------")
            ### Local computing
            self.graph = Graph.Read_Ncol('D:/Project/data/' + file_obj + '.txt', directed=directed) 
            # self.graph = Graph.Read_Ncol('C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/data/' + file_obj + '.txt',directed=directed)
            ### For Aalto Notebooks
            # self.graph = Graph.Read_Ncol('./data/' + file_obj + '.txt', directed=directed)
            print("------------------Reading Completed-----------------")
            info = self.task_0(directed)
            if(directed):
                ext = '_LSCC.txt'
            else:
                ext = '_LWCC.txt'
            print("------------------Graph Summary--------------------")
            print("Graph Name: " + file_obj)
            print("Edges/Vertices: " + info.split("-- ")[1])
            print("------------------Writing LCCs to Disk--------------------")
            ### Local computing
            self.scc_largest.write_graphmlz(f='D:/Project/outputs_igraph/'+ file_obj + ext)
            # self.scc_largest.write_graphmlz(f='C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/outputs/'+ file_obj + ext)
            ### For Aalto Notebooks
            # self.scc_largest.write_graphmlz(f='./outputs/'+ file_obj + ext)
            print("------------------Completed-----------------")
            print("Iteration finished")

def main():
    obj = task_0()
    obj.lscc_lwcc_generator()

if __name__ == "__main__":
    main()