from igraph import *
import numpy as np
import time
import random
import pandas as pd

class task_2:
    graph = None
    nodes = []
    filenames = ['wiki-Vote']
    # filenames = ['wiki-Vote', 'soc-Epinions1', 'soc-Pokec', 'ego-Gplus']
    LSCC_vsizes = [1300, 32223, 1304537, 69501]
    LWCC_vsizes = [7066, 75877, 1632803, 107614]

    num_samples = 100
    num_iterations = 2

    ### Sample random pairs algorithm implementation
    def random_pairs(self, iteration):
        v_x = []
        v_y = []
        distances = []

        # Generate a list of random vertices indexes as origins x
        random.seed(2017 + 300*iteration)
        v_x = random.sample(range(self.LSCC_vsizes[0]-1), k=self.num_samples)
        random.shuffle(v_x)

        # Generate a list of random vertices indexes as destinations y
        random.seed(2018 + 100*iteration)        
        v_y = random.sample(range(self.LSCC_vsizes[0]-1), k=self.num_samples)
        random.shuffle(v_y)

        for i in range(self.num_samples-1):
            distances.append(self.graph.shortest_paths(source=v_x[i], target=v_y[i])[0])

        return distances


    ### Sample random sources algorithm implementation
    def random_sources(self, iteration):
        random.seed(2018 + 100*iteration)
        sources = random.sample(range(self.LSCC_vsizes[0]-1), k=self.num_samples)
        random.shuffle(sources)
        distances = self.graph.shortest_paths(sources)
        return distances

    def bitmask(self,size):
        mask = ''
        for i in range(0,size):
            mask = mask + str(np.random.binomial(1, 0.5 ** (i + 1)))
        return mask

    def compute_b(self,bitmask,n):
        bitmask = np.binary_repr(bitmask)
        masks = [bitmask[i:i+n] for i in range(0, len(bitmask), n)]
        sum = 0
        for mask in masks:
            pos = mask.find('0')
            if pos > -1:
                sum += pos
        return sum / len(masks)

    ### Sample random sources algorithm implementation
    def anf(self, iteration):
        ### Define:
        # k = number of bitmasks; n = length of 1 bitmask; h = iteration parameter
        k = 3
        n = math.ceil(math.log2(len(self.nodes)))
        
        # Define array of M dictionaries to hold values of each iteration, h
        M = [dict() for i in range(iteration)]
        
        # Define array of IN^ estimates for each iteration, h
        IN = [[] for i in range(iteration)]

        # Generate K bitmasks of length n each
        # Set 1 bit randomly using exponential distribution
        for node in self.nodes:
            mask = ''
            for i in range(0,k):
                mask = mask + self.bitmask(n)
            M[0][node] = int(mask, base=2)
        
        N = []
        for h in range(1,iteration):
            M[h] = M[h - 1].copy()
            for edge in self.graph.get_edgelist():
                # Do Bitwise OR
                M[h][edge[0]] = M[h][edge[0]] | M[h-1][edge[1]]
            for node in self.nodes:
                IN[h-1].append((2 ** self.compute_b(M[h][node],n)) / .77351)
            # if max(IN[h-1]) > 0.5 * len(self.nodes):
            #     print("Median: " + str(h))       
            # if max(IN[h-1]) > 0.9 * len(self.nodes):
            #     print("Effective Diameter: " + str(h))
            #     return
            # if max(IN[h-1]) > len(self.nodes):
            #     print("Diameter: " + str(h))   
            if IN[h-1] == IN[h-2]:
                return h
        return False

    def median(self, function):
        medians = []
        for i in range(self.num_iterations):
            med = np.median(function(i))
            medians.append(med)
        return np.mean(medians)

    def mean(self, function):
        means = []
        for i in range(self.num_iterations):
            mean = np.mean(function(i))
            means.append(mean)
        return np.mean(means)

    def diameter(self, function):
        diameters = []
        for i in range(self.num_iterations):
            diameter = np.max(function(i))
            diameters.append(diameter)
        return max(diameters)

    def effective_diameter(self, function):
        eff_diameters = []
        for i in range(self.num_iterations):
            d_sorted = np.sort(np.amax(function(i), axis=1))
            eff_diameters.append(d_sorted[int(np.floor(self.num_samples*0.9))])
        return mean(eff_diameters)


    # def main(self):
    #     self.nodes = self.graph.vs.indices
    #     algorithms = ['Sample_random_pairs', 'Sample_random_sources']#, 'Flajolet-Martin']
    #     algorithms_func = [self.random_pairs, self.random_sources]#, self.flajolet_martin]

    #     statistics = ['Median', 'Mean', 'Diameter', 'Effective_diameter']
    #     statistics_func = [self.median, self.mean, self.diameter, self.effective_diameter]
    #     for i, algorithm in enumerate(algorithms):
    #         print("--------------------" + algorithm + "--------------------") 
    #         for index, statistic in enumerate(statistics):
    #             print("----------" + statistic + "----------")
    #             start = time.perf_counter()
    #             function = statistics_func[index]
    #             value = function(algorithms_func[i])
    #             elapsed = time.perf_counter() - start
    #             print('Value: ' + str(value))
    #             print('Elapsed Time: %.3f seconds.' % elapsed)

def main():
    # graph = Graph(directed = False)
    # graph.add_vertices([0,1,2,3,4])
    # graph.add_edges([[0,1],[1,2],[2,3],[3,4],[4,1]])
    obj = task_2()
    # obj.graph = graph    
    obj.graph = Graph.Read_GraphMLz('D:/Project/outputs_igraph/ego-Gplus_LSCC.txt', directed = True)
    obj.nodes = obj.graph.vs.indices
    # obj.graph = Graph.Read_GraphMLz('C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/outputs/wiki-Vote_LWCC.txt')
    start = time.perf_counter()
    value = obj.anf(99999)
    elapsed = time.perf_counter() - start
    print('Value: ' + str(value))
    print('Elapsed Time: %.3f seconds.' % elapsed)

if __name__ == "__main__":
    main()