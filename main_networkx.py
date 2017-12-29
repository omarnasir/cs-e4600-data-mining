from networkx import DiGraph, Graph, read_edgelist
from networkx import write_gpickle, read_graphml
from networkx import all_pairs_shortest_path_length, single_source_shortest_path_length
import task_1_networkx 
import numpy as np
import time

def main():
    filenames = ['wiki-Vote']
    # filenames = ['wiki-Vote', 'soc-Epinions1', 'soc-Pokec', 'ego-Gplus']
    # ext = [['_LWCC.txt.gz','Weakly Connected Component']]
    ext = [['_LSCC.txt.gz','Strongly Connected Component'],['_LWCC.txt.gz','Weakly Connected Component']]
    for fileobj in filenames:
        print("######################################################")
        print("\n" + "Reading Subgraph from Disk: " + fileobj + "\n")
        print("######################################################")
        for e in ext:
            print("\n--------- Type: " + e[1] + " ---------")   
            obj = task_1_networkx.task_1()
            obj.graph = read_graphml('D:/Project/outputs/' + fileobj + e[0])
            # wiki_Vote = read_gpickle('C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/outputs/wiki-Vote_LSCC.txt')
            obj.main()  

if __name__ == "__main__":
    main()