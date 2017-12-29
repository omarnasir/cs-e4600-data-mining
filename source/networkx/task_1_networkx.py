from networkx import all_pairs_shortest_path_length, shortest_path_length, single_source_shortest_path_length, eccentricity, diameter
from networkx import write_gpickle, read_gpickle
import numpy as np
import time
import multiprocessing as mp
import concurrent.futures
from memory_profiler import profile

class task_1:
    graph = None
    NUM_PROCESS = 1
    nodes = []

    def getdistance(self, node):
        return list(single_source_shortest_path_length(self.graph, node).values())

    def getdistancesumcount(self, node):
        sum_tmp = 0
        count = 0
        distance_node = single_source_shortest_path_length(self.graph, node)
        distance = np.array(list(distance_node.values()))
        sum_tmp += sum(distance)
        count += len(distance)
        # print(sum_tmp)
        return [sum_tmp, count]

    def getshortestpaths(self, node):
        min_paths = single_source_shortest_path_length(self.graph, node)
        return max(np.array(list(min_paths.values())))

    def geteccentricity(self, node):
        return eccentricity(self.graph,node)

    @profile
    def median(self):
        pool = mp.Pool(processes=5)
        results = pool.map(self.getdistance, self.graph.nodes())
        pool.close()
        pool.join()
        return np.median(results)

    @profile
    def mean(self):
        pool = mp.Pool(processes=5)
        results = pool.map(self.getdistancesumcount, self.graph.nodes())
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
        self.nodes = self.graph.nodes()
        statistics = ['Median','Mean', 'Diameter', 'Effective_diameter']
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
#     graph = read_gpickle('D:/Project/outputs/wiki-Vote_LSCC.txt')
#     start = time.perf_counter()
#     value = diameter(graph)
#     elapsed = time.perf_counter() - start
#     print('Value: ' + str(value))
#     print('Elapsed Time: %.3f seconds.' % elapsed)

# if __name__ == "__main__":
#     main()