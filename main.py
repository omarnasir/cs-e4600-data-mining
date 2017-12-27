from networkx import DiGraph, Graph, read_edgelist
from networkx import write_gpickle, read_gpickle
from networkx import all_pairs_shortest_path_length, single_source_shortest_path_length
import task_1 
import numpy as np
import time

def main():
    print("----------Reading Connected Component SubGraph From File")
    wiki_Vote = read_gpickle('D:/Project/outputs/wiki-Vote_LWCC.txt')
    # wiki_Vote = read_gpickle('C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/outputs/wiki-Vote_LSCC.txt')
    # soc_Epinions1 = read_gpickle('D:/Project/outputs/soc-Epinions1_LSCC.txt')
    print("----------Done")
    print("----------Computing Statistics")
    obj = task_1.task_1()
    obj.graph = wiki_Vote
    obj.main()
    # task_1(soc_Epinions1)

if __name__ == "__main__":
    main()