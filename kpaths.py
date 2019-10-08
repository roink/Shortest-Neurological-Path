from brain_path import BrainPath
from copy import deepcopy
import numpy as np

class KPaths:
    def __init__(self, k):
        self.list_of_paths = []
        self.k = k

    def add(self, other: BrainPath):
        if deepcopy(other) in self.list_of_paths:
            return 0

        self.list_of_paths.append(deepcopy(other))
        self.list_of_paths = sorted(self.list_of_paths)
        self.list_of_paths = self.list_of_paths[:self.k]
        if other in self.list_of_paths:
            return 1
        else:
            return 0

    def __str__(self):
        string = '['
        if len(self.list_of_paths) > 0:
            string += str(self.list_of_paths[0])
        else:
            return string + ']'
        for i in range(1,len(self.list_of_paths)):
            string += ', '+str(self.list_of_paths[i])
        return string + ']'

    def __len__(self):
        return len(self.list_of_paths)

    def matrix_representation(self, numregions):
        m = np.zeros((numregions, numregions),dtype=int)
        if not(self.list_of_paths):
            return m
        i: BrainPath
        for i in self.list_of_paths:
            m += i.matrix_representation(numregions)
        return m
