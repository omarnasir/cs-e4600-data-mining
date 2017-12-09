from networkx import all_pairs_shortest_path_length, shortest_path_length, single_source_shortest_path_length, eccentricity, diameter
from networkx import write_gpickle, read_gpickle
import numpy as np
import time
import concurrent.futures

def median(graph):
    distance = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        nodes = graph.nodes()
        for node in executor.map(nodes):
            distance_node = single_source_shortest_path_length(graph, node)
            distance.extend(np.array(list(distance_node.values())))
    return np.median(distance)

def mean(graph):
    distance = []
    for node in graph.nodes():
        distance_node = single_source_shortest_path_length(graph, node)
        distance.extend(np.array(list(distance_node.values())))
    return np.mean(distance)

def diameter(graph):
    d = 0
    min_paths = []
    for node in graph.nodes():
        min_paths = shortest_path_length(graph, node)
        del min_paths[node]
        min_paths = np.array(list(min_paths.values()))
        d_node = max(min_paths) 
        if d_node > d:
            d = d_node
    return d

def effective_diameter(graph):
    eff_d = []
    for node in graph.nodes():
        d_node = eccentricity(graph, node)
        del d_node[node]
        eff_d.append(d_node)
    eff_d_sorted = np.sort(eff_d)
    return eff_d_sorted[int(np.floor(len(eff_d_sorted)*0.9))]

statistics = ['Median', 'Mean', 'Diameter', 'Effective_diameter']
statistics_func = [median, mean, diameter, effective_diameter]

def task_1(graph):
    for index, statistic in enumerate(statistics):
        print("----------" + statistic + "----------")
        start = time.perf_counter()
        function = statistics_func[index]
        value = function(graph)
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