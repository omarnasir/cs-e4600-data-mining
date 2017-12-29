from igraph import *
import numpy as np
import time
import random

class task_2:
    graph = None
    LSCC_vsizes = [1300, 32223, 1304537, 69501] # Respective LSCC number of nodes of datasets 'wiki-Vote', 'soc-Epinions1', 'soc-Pokec' and 'ego-Gplus'
    LWCC_vsizes = [7066, 75877, 1632803, 107614] # Respective LWCC number of nodes of datasets 'wiki-Vote', 'soc-Epinions1', 'soc-Pokec' and 'ego-Gplus'
    directed = False # Set to False to consider LWCC, set to True to consider LSCC

    dataset_i = 0 # Set to 0 for wiki-Vote, to 1 for soc-Epinions1, to 2 for soc-Pokec, to 3 for ego-Gplus.

    num_samples = 100
    num_iterations = 5

    def setDirected(self, boolean):
        self.directed = boolean

    def setDatasetIndex(self, i):
        self.dataset_i = i
    

    ### Sample random pairs algorithm implementation
    def random_pairs(self, iteration):
        v_x = []
        v_y = []
        distances = []

        # Generate a list of random vertices indexes as origins x
        random.seed(2017 + 300*iteration)
        if self.directed:
            v_x = random.sample(range(self.LSCC_vsizes[self.dataset_i]-1), k=self.num_samples)
        else:
            v_x = random.sample(range(self.LWCC_vsizes[self.dataset_i]-1), k=self.num_samples)
        random.shuffle(v_x)

        # Generate a list of random vertices indexes as destinations y
        random.seed(2018 + 100*iteration)        
        if self.directed:
            v_y = random.sample(range(self.LSCC_vsizes[self.dataset_i]-1), k=self.num_samples)
        else:
            v_y = random.sample(range(self.LWCC_vsizes[self.dataset_i]-1), k=self.num_samples)            
        random.shuffle(v_y)

        for i in range(self.num_samples-1):
            distances.append(self.graph.shortest_paths(source=v_x[i], target=v_y[i])[0])

        return distances


    ### Sample random sources algorithm implementation
    def random_sources(self, iteration):
        random.seed(2018 + 100*iteration)
        if self.directed:
            sources = random.sample(range(self.LSCC_vsizes[self.dataset_i]-1), k=self.num_samples)
        else:
            sources = random.sample(range(self.LWCC_vsizes[self.dataset_i]-1), k=self.num_samples)            
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

    filenames = ['wiki-Vote', 'soc-Epinions1', 'soc-Pokec', 'ego-Gplus']
    ext = [['_LSCC.txt','Strongly Connected Component', True],['_LWCC.txt','Weakly Connected Component', False]]

    for i, fileobj in enumerate(filenames):
        print("######################################################")
        print("\n" + "Reading Subgraph from Disk: " + fileobj + "\n")
        print("######################################################")
        
        for e in ext:
            print("\n--------- Type: " + e[1] + " ---------")
            obj = task_2()
            obj.setDatasetIndex(i)
            obj.setDirected(e[2])
            # obj.graph = Graph.Read_GraphMLz('D:/Project/outputs_igraph/' + fileobj + e[0])
            obj.graph = Graph.Read_GraphMLz('C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/outputs/' + fileobj + e[0])
            obj.main()

    # obj = task_2()
    # # obj.graph = Graph.Read_GraphMLz('D:/Project/outputs_igraph/wiki-Vote_LWCC.txt')
    # obj.graph = Graph.Read_GraphMLz('C:/Users/Pc Laura/Desktop/Data_Mining/Project/cs-e4600-data-mining/outputs/wiki-Vote_LWCC.txt')
    # # start = time.perf_counter()
    # value = obj.diameter(obj.random_pairs)
    # elapsed = time.perf_counter() - start
    # print('Value: ' + str(value))
    # print('Elapsed Time: %.3f seconds.' % elapsed)

    

if __name__ == "__main__":
    main()