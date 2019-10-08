from brain_path import BrainPath
from kpaths import KPaths
import numpy as np


class Paths:

    def __init__(self, k, num_regions):
        self.num_shortest_paths = k
        self.num_regions = num_regions

        self.list_of_paths = [KPaths(k) for i in range(num_regions)]

    def add(self, path: BrainPath):
        return self.list_of_paths[path.last()].add(path)

    def __len__(self):
        return min([len(i) for i in self.list_of_paths])

    def __str__(self):
        string = ''
        if self.num_regions>0:
            string += str(self.list_of_paths[0])
        else:
            return string
        for i in range(1,self.num_regions):
            string += '\n'
            string += str(self.list_of_paths[i])
        return string

    def str(self,j):
        string = ''
        if self.num_regions>0:
            string += str(j+1)+', 1, '+str(self.list_of_paths[0])
        else:
            return string
        for i in range(1,self.num_regions):
            string += '\n'
            string += str(j+1)+', '+str(i+1)+', '+str(self.list_of_paths[i])
        return string

    def matrix_representation(self):
        m = np.zeros((self.num_regions, self.num_regions),dtype=int)
        if not(self.list_of_paths):
            return m
        i: KPaths
        for i in self.list_of_paths:
            m += i.matrix_representation(self.num_regions)
        return m






