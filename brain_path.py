from copy import deepcopy
import numpy as np


class BrainPath:
    len = 0
    elements = []

    def __init__(self, first_element, start_val = 0):
        self.len = start_val
        self.elements = [first_element]

    def last(self):
        return self.elements[-1]

    def first(self):
        return self.elements[0]

    def add(self, element, dist):
        bp = BrainPath(77)
        bp.elements = deepcopy(self.elements)
        bp.elements.append(element)
        bp.len = self.len + dist
        return bp

    def __len__(self):
        return self.len

    def __str__(self):
        return str([round(self.len*100)/100, [i+1 for i in self.elements]])

    def __eq__(self, other):
        if not isinstance(other, BrainPath):
            return False
        return self.elements == other.elements

    def __lt__(self, other):
        return self.len < other.len

    def matrix_representation(self,numregions):
        m = np.zeros((numregions, numregions),dtype=int)
        if not(self.elements):
            return m
        for i in range(len(self.elements)-1):
            m[i,i+1]+=1
        return m



