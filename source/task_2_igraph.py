from igraph import *
import numpy as np
import time
import random
import utilities.bitmask
import matplotlib.pyplot as plt

class task_2:
    graph = None
    nodes = []

    num_samples = 20
    k = 4

    def setSamples(self, num):
        self.num_samples = num

    ### Sample random pairs algorithm implementation
    def random_pairs(self):
        v_x = []
        v_y = []
        distances = []

        # Generate a list of random vertices indexes as origins x
        random.seed(2017)
        v_x = random.sample(range(len(self.nodes)), k=self.num_samples)
        random.shuffle(v_x)

        # Generate a list of random vertices indexes as destinations y
        random.seed(2018)        
        v_y = random.sample(range(len(self.nodes)), k=self.num_samples)       
        random.shuffle(v_y)

        for i in range(self.num_samples-1):
            distances.append(self.graph.shortest_paths(source=v_x[i], target=v_y[i])[0])

        return distances

    ### Sample random sources algorithm implementation
    def random_sources(self):
        random.seed(1234)
        sources = random.sample(range(len(self.nodes)), k=self.num_samples)
        random.shuffle(sources)
        distances = self.graph.shortest_paths(sources)
        return distances

    ### ANF algorithm implementation
    def anf(self):
        ### Define:
        # k = number of bitmasks; n = length of 1 bitmask; h = iteration parameter
        k = self.k
        n = math.ceil(math.log2(len(self.nodes)))
        
        # Define array of M dictionaries to hold values of each iteration, h
        M = [dict() for i in range(2)]
        
        # Define array of IN^ estimates for each iteration, h
        IN = [[] for i in range(2)]

        # Generate K bitmasks of length n each
        # Set 1 bit randomly using exponential distribution
        for node in self.nodes:
            mask = ''
            for i in range(0,k):
                mask = mask + utilities.bitmask.generate_bitmask(n)
            M[0][node] = int(mask, base=2)

        h = 0
        N = []
        while (True):
            i = h % 2
            M[1] = M[0].copy()
            for edge in self.graph.get_edgelist():
                # Do Bitwise OR
                M[1][edge[0]] = M[1][edge[0]] | M[0][edge[1]]
            for node in self.nodes:
                IN[i].append((2 ** utilities.bitmask.compute_b(M[1][node],n)) / .77351)
            # Stop Criterion
            if IN[1] == IN[0]:
                return h
            M[0] = M[1].copy()
            h += 1
            IN[h % 2] = []
        return False

    def median(self, function):
        return np.median(function())

    def mean(self, function):
        return np.mean(function())

    def diameter(self, function):
        return np.max(function())

    def effective_diameter(self, function):
        d_sorted = np.sort(np.amax(function(), axis=1))
        return d_sorted[int(np.floor(self.num_samples*0.9))]

    def task_2_1(self):
        self.nodes = self.graph.vs.indices
        algorithms = ['Sample_random_pairs', 'Sample_random_sources']
        algorithms_func = [self.random_pairs, self.random_sources]

        statistics = ['Median', 'Mean', 'Diameter', 'Effective_diameter']
        statistics_func = [self.median, self.mean, self.diameter, self.effective_diameter]
        for i, algorithm in enumerate(algorithms):
            print("--------------------" + algorithm + "--------------------") 
            for index, statistic in enumerate(statistics):
                print(" ")
                print(statistic)
                start = time.perf_counter()
                function = statistics_func[index]
                value = function(algorithms_func[i])
                elapsed = time.perf_counter() - start
                print('-> Value: ' + str(value))
                print('-> Elapsed Time: %.3f seconds.' % elapsed)
        print("--------------------ANF Basic--------------------") 
        print("Approximate Diameter")
        start = time.perf_counter()
        value = self.anf()
        elapsed = time.perf_counter() - start
        print('-> Value: ' + str(value))
        print('-> Elapsed Time: %.3f seconds.' % elapsed)

    def task_2_2(self):
        self.nodes = self.graph.vs.indices
        algorithms = ['Sample_random_pairs', 'Sample_random_sources']
        algorithms_func = [self.random_pairs, self.random_sources]

        statistics = ['Median', 'Mean', 'Diameter', 'Effective_diameter']
        statistics_func = [self.median, self.mean, self.diameter, self.effective_diameter]
        samples = range(1, 10, 1)
        k = range(2,8,2)
        for index, statistic in enumerate(statistics):
            stat = []
            print("--------------------" + statistic + "--------------------") 
            for i, algorithm in enumerate(algorithms):
                print("----------" + algorithm + "----------")
                tmp = []
                function = statistics_func[index]
                for sample in samples:
                    tmp.append(function(algorithms_func[i]))
                stat.append(tmp)
            plt.figure()
            plt.xlabel('Numbers of samples')
            plt.ylabel(statistics[index])
            plt.title('Graph of the estimation of the ' + statistics[index] + ' for the different approximation algorithms on the Epinion_LSCC graph')
            alg_0, = plt.plot(samples, stat[0], 'ro', label='Sample random pairs')
            alg_1, = plt.plot(samples, stat[1], 'bs', label='Sample random sources')
            plt.legend(handles = [alg_0, alg_1])
            plt.show()

        print("--------------------Effective Diameter--------------------") 
        print("----------ANF Basic----------")
        tmp = []
        for k_ in k:
            self.k = k_
            tmp.append(self.anf())
        plt.figure()
        plt.xlabel('Value of k bitmask length')
        plt.title('Graph of the estimation of the ANF Basic on the Epinion_LSCC graph')
        alg_0, = plt.plot(k, tmp, 'ro', label='ANF Basic')
        plt.legend(handles = [alg_0])
        plt.show()