import igraph
import numpy as np
import time
import random

class task_2:
    graph = None
    filenames = ['soc-Pokec']
    # filenames = ['wiki-Vote', 'soc-Epinions1', 'soc-Pokec', 'ego-Gplus']
    LSCC_vsizes = [1300, 32223, 1304537, 69501]
    LWCC_vsizes = [7066, 75877, 1632803, 107614]

    num_samples = 100
    

    ### Sample random pairs algorithm implementation
    def random_pairs(self):
        v_x = []
        v_y = []
        distances = []

        # Generate a list of random vertices indexes as origins x
        random.seed(2017)
        v_x = random.sample(range(self.LSCC_vsizes[0]-1), k=self.num_samples)
        random.shuffle(v_x)

        # Generate a list of random vertices indexes as destinations y
        random.seed(2018)        
        v_y = random.sample(range(self.LSCC_vsizes[0]-1), k=self.num_samples)
        random.shuffle(v_y)

        distances = igraph.shortest_paths(v_x, v_y)

        return distances
    
        




def main():
    obj = task_2()
    print(obj.random_pairs())

if __name__ == "__main__":
    main()