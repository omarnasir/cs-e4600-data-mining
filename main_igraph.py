from igraph import *
import task_1_igraph
import numpy as np
import time

def main():
    filenames = ['wiki-Vote']
    # filenames = ['wiki-Vote', 'soc-Epinions1', 'soc-Pokec', 'ego-Gplus']
    # ext = [['_LWCC.txt','Weakly Connected Component']]
    ext = [['_LSCC.txt','Strongly Connected Component'],['_LWCC.txt','Weakly Connected Component']]
    for fileobj in filenames:
        print("######################################################")
        print("\n" + "Reading Subgraph from Disk: " + fileobj + "\n")
        print("######################################################")
        for e in ext:
            print("\n--------- Type: " + e[1] + " ---------")   
            obj = task_1_igraph.task_1()
            obj.graph = Graph.Read_GraphMLz('D:/Project/outputs_igraph/' + fileobj + e[0])
            # wiki_Vote = read_gpickle('C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/outputs/wiki-Vote_LSCC.txt')
            obj.main()  
            
if __name__ == "__main__":
    main()