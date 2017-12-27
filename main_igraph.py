from igraph import *
import task_1_igraph
import numpy as np
import time

def main():
    filenames = ['wiki-Vote', 'soc-Epinions1', 'soc-Pokec', 'ego-Gplus']
    ext = ['_LSCC.txt','_LWCC.txt']
    print("----------Reading Connected Component SubGraph From File")
    wiki_Vote = Graph.Read_Pickle('D:/Project/outputs_igraph/ego-Gplus_LSCC.txt')
    # wiki_Vote = read_gpickle('C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/outputs/wiki-Vote_LSCC.txt')
    # soc_Epinions1 = read_gpickle('D:/Project/outputs_igraph/soc-Epinions1_LSCC.txt')
    print(wiki_Vote.summary())
    # print("----------Done")
    # print("----------Computing Statistics")
    # obj = task_1_igraph.task_1()
    # obj.graph = wiki_Vote
    # obj.main()
    # task_1(soc_Epinions1)

if __name__ == "__main__":
    main()