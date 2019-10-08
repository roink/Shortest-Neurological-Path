import numpy as np
from brain_path import BrainPath
from paths import Paths
from heapq import heappush
from heapq import heappop

distances = np.loadtxt('/home/philipp/alzheimers/neurodegeneration-forecast/Network_Data/AD_Patients/Average/adj_average.txt')

distances = np.max(distances)-distances

[m, _] = np.shape(distances)

heap = []

k = 1

connections = np.zeros((m,m),dtype=int);

with open('1-best-connectivity-path.txt', 'w') as file:
    for start in range(m):
        print(start)

        ps = Paths(k, m)

        p = BrainPath(start)
        heappush(heap, p)

        while len(heap) > 0:
            path: BrainPath = heappop(heap)
            for next_node in range(m):
                if next_node not in path.elements:
                    new_path = path.add(next_node, distances[path.last(), next_node])
                    if ps.add(new_path):
                        heappush(heap, new_path)
        file.write(ps.str(start) + '\n')

        connections += ps.matrix_representation()

np.savetxt('best_connectivity_paths_matrix.txt',connections)

