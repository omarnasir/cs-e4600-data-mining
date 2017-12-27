from networkx import all_pairs_shortest_path_length, shortest_path_length, single_source_shortest_path_length, eccentricity, diameter
from networkx import write_gpickle, read_gpickle
import numpy as np
import time
import multiprocessing as mp
import concurrent.futures

class task_1:
    graph = None
    
    def getdistance(self, node):
        return single_source_shortest_path_length(self.graph, node)

    def getdistancesumcount(self, node):
        sum_tmp = 0
        count = 0
        distance_node = single_source_shortest_path_length(self.graph, node)
        distance = np.array(list(distance_node.values()))
        sum_tmp += sum(distance)
        count += len(distance)
        # print(sum_tmp)
        return [sum_tmp, count]


    def median(self):
        pool = mp.Pool(processes=5)
        results = pool.map(self.getdistance, self.graph.nodes())
        output = [list(res.values()) for res in results]
        pool.close()
        pool.join()
        # distance = []
        # for node in graph.nodes():
        #     distance_node = single_source_shortest_path_length(graph, node)
        #     distance.extend(np.array(list(distance_node.values())))
        return np.median(output)

    def mean(self):
        pool = mp.Pool(processes=5)
        results = pool.map(self.getdistancesumcount, self.graph.nodes())
        output = [res for res in results]
        pool.close()
        pool.join()
        sum_all= np.sum(output, axis=0)
        print(sum_all[0])
        d_mean = sum_all[0] / sum_all[1]
        # distance = []
        # for node in self.graph.nodes():
        #     distance_node = single_source_shortest_path_length(self.graph, node)
        #     distance.extend(np.array(list(distance_node.values())))
        return d_mean

    def diameter(self):
        d = 0
        min_paths = []
        for node in self.graph.nodes():
            min_paths = shortest_path_length(self.graph, node)
            del min_paths[node]
            min_paths = np.array(list(min_paths.values()))
            d_node = max(min_paths) 
            if d_node > d:
                d = d_node
        return d

    def effective_diameter(self):
        eff_d = []
        for node in self.graph.nodes():
            d_node = eccentricity(self.graph, node)
            eff_d.append(d_node)
        eff_d_sorted = np.sort(eff_d)
        return eff_d_sorted[int(np.floor(len(eff_d_sorted)*0.9))]

    def main(self):
        statistics = ['Median', 'Mean', 'Diameter', 'Effective_diameter']
        statistics_func = [self.median, self.mean, self.diameter, self.effective_diameter]
        for index, statistic in enumerate(statistics):
            print("----------" + statistic + "----------")
            start = time.perf_counter()
            function = statistics_func[index]
            value = self.mean()
            elapsed = time.perf_counter() - start
            print('Value: ' + str(value))
            print('Elapsed Time: %.3f seconds.' % elapsed)
    
# def main():
#     graph = read_gpickle('D:/Project/outputs/wiki-Vote_LSCC.txt')
#     start = time.perf_counter()
#     value = diameter(graph)
#     elapsed = time.perf_counter() - start
#     print('Value: ' + str(value))
#     print('Elapsed Time: %.3f seconds.' % elapsed)

# if __name__ == "__main__":
#     main()