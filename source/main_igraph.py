from igraph import *
import numpy as np
import time

import task_1_igraph
import task_2_igraph

filenames = ['ego-Gplus']
# filenames = ['wiki-Vote', 'soc-Epinions1', 'soc-Pokec', 'ego-Gplus']
# ext = [['_LSCC.gz','Strongly Connected Component', True],['_LWCC.gz','Weakly Connected Component', False]]
ext = [['_LWCC.gz','Weakly Connected Component', False]]

def execute_task_1():
    for fileobj in filenames:
        print("######################################################")
        print("\n" + "Reading Subgraph from Disk: " + fileobj + "\n")
        print("######################################################")
        for e in ext:
            print("\n--------- Type: " + e[1] + " ---------")   
            obj = task_1_igraph.task_1()
            obj.graph = Graph.Read_GraphMLz('D:/Project/outputs/' + fileobj + e[0], directed = e[2])
            obj.main()  
            
def execute_task_2_1():
    for i, fileobj in enumerate(filenames):
        print("######################################################")
        print("\n" + "Reading Subgraph from Disk: " + fileobj + "\n")
        print("######################################################")
        for e in ext:
            print("\n--------- Type: " + e[1] + " ---------")
            obj = task_2_igraph.task_2()
            obj.graph = Graph.Read_GraphMLz('D:/Project/outputs/' + fileobj + e[0], directed = e[2])            
            obj.task_2_1()

def execute_task_2_2():
    print("######################################################")
    print("\n" + "Reading Subgraph from Disk: soc-Epinions1 \n")
    print("######################################################")
    for e in ext:
        print("\n--------- Type: " + e[1] + " ---------")
        obj = task_2_igraph.task_2()
        obj.graph = Graph.Read_GraphMLz('D:/Project/outputs/wiki-Vote' + e[0], directed = e[2])            
        obj.task_2_2()

def main():
    # execute_task_1()
    execute_task_2_1()  
    # execute_task_2_2()  

if __name__ == "__main__":
    main()