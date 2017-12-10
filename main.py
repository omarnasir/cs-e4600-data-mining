from networkx import write_gpickle, read_gpickle
from networkx import all_pairs_shortest_path_length, single_source_shortest_path_length
from graph_reader import read_graph
from task_0 import task_0
import task_1 
import numpy as np
import time

# def lscc_lwcc_generator():
#     directed = False
#     filenames = ['ego-Gplus']
#     # filenames = ['wiki-Vote', 'soc-Epinions1', 'soc-Pokec', 'ego-Gplus']
#     for file_obj in filenames:
#         # graph = read_graph('D:/Project/data/' + file_obj + '.txt', directed)
#         graph = read_graph('C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/data/' + file_obj + '.txt', directed
#         #For Cloud
#         # graph = read_graph('./data/' + file_obj + '.txt', directed)
#         SCC_largest, info = task_0(graph, directed)
#         if(directed):
#             ext = '_LSCC.txt'
#         else:
#             ext = '_LWCC.txt'

#         # write_gpickle(SCC_largest,'D:/Project/outputs/'+ file_obj + ext)
#         write_gpickle(SCC_largest,'C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/outputs/'+ file_obj + ext)
#         #For Cloud
#         # write_gpickle(SCC_largest,'./outputs/'+ file_obj + ext)
#         print(info)
#         print("Iteration finished")

def main():
    print("----------Reading Connected Component SubGraph")
    # wiki_Vote = read_gpickle('D:/Project/outputs/wiki-Vote_LWCC.txt')
    wiki_Vote = read_gpickle('C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/outputs/wiki-Vote_LSCC.txt')
    # soc_Epinions1 = read_gpickle('D:/Project/outputs/soc-Epinions1_LSCC.txt')
    print("----------Done")
    print("----------Computing Statistics")
    obj = task_1.task_1()
    obj.graph = wiki_Vote
    obj.main()
    # task_1(soc_Epinions1)

if __name__ == "__main__":
    main()