from igraph import *
import numpy as np
import time
import multiprocessing as mp
import concurrent.futures

class task_1:
    NUM_PROCESS = 4
    graph = None
    nodes = []

    ### Utility functions for each exact statistic
    ### Called by each Parallelization process
    def getdistance(self, node):
        return self.graph.shortest_paths(source=node)[0]

    def getdistancesumcount(self, node):
        distance_node = self.graph.shortest_paths(source=node)[0]
        distance = np.array(distance_node)
        return sum(distance) / len(distance)

    def getshortestpaths(self, node):
        min_paths = self.graph.shortest_paths(source=node)[0]
        return max(np.array(min_paths))

    def geteccentricity(self, node):
        return self.graph.eccentricity(vertices=node)

    ### Exact Statistics Function Definitions
    ### Spawn NUM_PROCESS processes and execute a Process Pool
    def median(self):
        pool = mp.Pool(processes=self.NUM_PROCESS)
        results = pool.map(self.getdistance, self.nodes)
        pool.close()
        pool.join()
        return np.median(results, overwrite_input = True)
    
    def mean(self):
        pool = mp.Pool(processes=self.NUM_PROCESS)
        results = pool.map(self.getdistancesumcount, self.nodes)
        pool.close()
        pool.join()
        d_mean = np.sum(results) / len(results)
        return d_mean

    def diameter(self):
        pool = mp.Pool(processes=self.NUM_PROCESS)
        results = pool.map(self.getshortestpaths, self.nodes)
        pool.close()
        pool.join()
        return max(np.array(results))         

    def effective_diameter(self):
        pool = mp.Pool(processes=self.NUM_PROCESS)
        results = pool.map(self.geteccentricity, self.nodes)
        pool.close()
        pool.join()
        eff_d_sorted = np.sort(results)
        return eff_d_sorted[int(np.floor(len(eff_d_sorted)*0.9))]

    def main(self):
        self.nodes = self.graph.vs.indices
        statistics = ['Mean', 'Diameter', 'Effective_diameter', 'Median']
        statistics_func = [self.mean, self.diameter, self.effective_diameter, self.median]
        for index, statistic in enumerate(statistics):
            print(" ")
            print(statistic)
            start = time.perf_counter()
            function = statistics_func[index]
            value = function()
            elapsed = time.perf_counter() - start
            print('-> Value: ' + str(value))
            print('-> Elapsed Time: %.3f seconds.' % elapsed)