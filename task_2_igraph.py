from igraph import *
import numpy as np
import time
import random

class task_2:
    graph = None
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

    ### Sample random sources algorithm implementation
    def flajolet_martin(self, iteration):
        return "niet"
    

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


    def main(self):
        algorithms = ['Sample_random_pairs', 'Sample_random_sources']#, 'Flajolet-Martin']
        algorithms_func = [self.random_pairs, self.random_sources]#, self.flajolet_martin]

        statistics = ['Median', 'Mean', 'Diameter', 'Effective_diameter']
        statistics_func = [self.median, self.mean, self.diameter, self.effective_diameter]
        for i, algorithm in enumerate(algorithms):
            print("--------------------" + algorithm + "--------------------") 
            for index, statistic in enumerate(statistics):
                print("----------" + statistic + "----------")
                start = time.perf_counter()
                function = statistics_func[index]
                value = function(algorithms_func[i])
                elapsed = time.perf_counter() - start
                print('Value: ' + str(value))
                print('Elapsed Time: %.3f seconds.' % elapsed)

def main():
    obj = task_2()
    # obj.graph = Graph.Read_GraphMLz('D:/Project/outputs_igraph/wiki-Vote_LWCC.txt')
    obj.graph = Graph.Read_GraphMLz('C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/outputs/wiki-Vote_LWCC.txt')
    # start = time.perf_counter()
    # value = obj.diameter(obj.random_pairs)
    # elapsed = time.perf_counter() - start
    # print('Value: ' + str(value))
    # print('Elapsed Time: %.3f seconds.' % elapsed)

    obj.main()

if __name__ == "__main__":
    main()