import numpy as np
from brain_path import BrainPath
from paths import Paths
from kpaths import KPaths
from copy import deepcopy
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

distances = np.loadtxt('/home/philipp/alzheimers/combined-atlas/euclidean_distances.txt')

delaunay = np.loadtxt('/home/philipp/alzheimers/combined-atlas/delaunay_triangulation/delaunay-edges.txt',
                      delimiter=',')

distances *= delaunay

[m, _] = np.shape(distances)

from heapq import heappush
from heapq import heappop

heap = []

k = 10

with open('10-shortest-path-delaunay.txt', 'w') as file:
    for start in range(m):
        print(start)

        ps = Paths(k, m)

        p = BrainPath(start)
        heappush(heap, p)

        while len(heap) > 0:
            path: BrainPath = heappop(heap)
            for next_node in np.nonzero(distances[path.last()])[0]:
                if next_node not in path.elements:
                    new_path = path.add(next_node, distances[path.last(), next_node])
                    if ps.add(new_path):
                        heappush(heap, new_path)
        file.write(ps.str(start) + '\n')
