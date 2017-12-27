from igraph import *
import numpy as np
import time
import multiprocessing as mp
import concurrent.futures

class task_1:
    graph = None
    
    def getdistance(self, node):
        return self.graph.shortest_paths(source=node)[0]

    def getdistancesumcount(self, node):
        sum_tmp = 0
        count = 0
        distance_node = self.graph.shortest_paths(source=node)[0]
        distance = np.array(distance_node)
        sum_tmp += sum(distance)
        count += len(distance)
        return [sum_tmp, count]

    def getshortestpaths(self, node, index):
        min_paths = self.graph.shortest_paths(source=node)[0]
        del min_paths[index]
        return max(np.array(min_paths))

    def median(self):
        pool = mp.Pool(processes=5)
        results = pool.map(self.getdistance, self.graph.vs.indices)
        output = [res for res in results]
        pool.close()
        pool.join()
        return np.median(output)

    def mean(self):
        pool = mp.Pool(processes=5)
        results = pool.map(self.getdistancesumcount, self.graph.vs.indices)
        output = [res for res in results]
        pool.close()
        pool.join()
        sum_all= np.sum(output, axis=0)
        d_mean = sum_all[0] / sum_all[1]
        return d_mean

    def diameter(self):
        d = 0
        pool = mp.Pool(processes=5)
        min_paths = []
        results = pool.map(self.getdistancesumcount, self.graph.vs.indices, range(0,len(self.graph.vs.indices)))
        output = [res for res in results]
        pool.close()
        pool.join()
        
        # for index,node in enumerate(self.graph.vs.indices):
        #     min_paths = self.graph.shortest_paths(source=node)[0]
        #     del min_paths[index]
        #     d_node = max(np.array(min_paths))
        #     if d_node > d:
        #         d = d_node
        return min(np.array(output))

    def effective_diameter(self):
        eff_d = []
        for node in self.graph.vs.indices:
            d_node = self.graph.eccentricity(vertices=node)
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
    
def main():
    obj = task_1()
    obj.graph = Graph.Read_GraphMLz('D:/Project/outputs_igraph/wiki-Vote_LWCC.txt')
    start = time.perf_counter()
    value = obj.diameter()
    elapsed = time.perf_counter() - start
    print('Value: ' + str(value))
    print('Elapsed Time: %.3f seconds.' % elapsed)

if __name__ == "__main__":
    main()