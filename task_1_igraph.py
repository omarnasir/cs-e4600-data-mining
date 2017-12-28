from igraph import *
import numpy as np
import time
import multiprocessing as mp
import concurrent.futures
from memory_profiler import profile

class task_1:
    NUM_PROCESS = 2
    graph = None
    nodes = []

    ### Utility functions for each exact statistic
    ### Called by each Parallelization process
    def getdistance(self, node):
        return np.sort(self.graph.shortest_paths(source=node)[0])

    def getdistancesumcount(self, node):
        sum_tmp = 0
        count = 0
        distance_node = self.graph.shortest_paths(source=node)[0]
        distance = np.array(distance_node)
        sum_tmp += sum(distance)
        count += len(distance)
        return [sum_tmp, count]

    def getshortestpaths(self, node):
        min_paths = self.graph.shortest_paths(source=node)[0]
        return max(np.array(min_paths))

    def geteccentricity(self, node):
        return self.graph.eccentricity(vertices=node)

    ### Exact Statistics Function Definitions
    ### Spawn NUM_PROCESS processes and execute a Process Pool
    @profile
    def median(self):
        pool = mp.Pool(processes=self.NUM_PROCESS)
        results = pool.map(self.getdistance, self.nodes)
        pool.close()
        pool.join()
        return np.median(results, overwrite_input = True)
    
    @profile
    def mean(self):
        pool = mp.Pool(processes=self.NUM_PROCESS)
        results = pool.map(self.getdistancesumcount, self.nodes)
        pool.close()
        pool.join()
        sum_all= np.sum(results, axis=0)
        d_mean = sum_all[0] / sum_all[1]
        return d_mean

    @profile
    def diameter(self):
        pool = mp.Pool(processes=self.NUM_PROCESS)
        results = pool.map(self.getshortestpaths, self.nodes)
        pool.close()
        pool.join()
        return max(np.array(results))         

    @profile
    def effective_diameter(self):
        pool = mp.Pool(processes=self.NUM_PROCESS)
        results = pool.map(self.geteccentricity, self.nodes)
        pool.close()
        pool.join()
        eff_d_sorted = np.sort(results)
        return eff_d_sorted[int(np.floor(len(eff_d_sorted)*0.9))]

    @profile
    def main(self):
        self.nodes = self.graph.vs.indices
        statistics = ['Median', 'Mean', 'Diameter', 'Effective_diameter']
        statistics_func = [self.median, self.mean, self.diameter, self.effective_diameter]
        for index, statistic in enumerate(statistics):
            print(" ")
            print(statistic)
            start = time.perf_counter()
            function = statistics_func[index]
            value = function()
            elapsed = time.perf_counter() - start
            print('-> Value: ' + str(value))
            print('-> Elapsed Time: %.3f seconds.' % elapsed)
    
# def main():
#     obj = task_1()
#     obj.graph = Graph.Read_GraphMLz('D:/Project/outputs_igraph/wiki-Vote_LWCC.txt')
#     obj.nodes = obj.graph.vs.indices
#     start = time.perf_counter()
#     value = obj.effective_diameter()
#     elapsed = time.perf_counter() - start
#     print('Value: ' + str(value))
#     print('Elapsed Time: %.3f seconds.' % elapsed)

# if __name__ == "__main__":
#     main()