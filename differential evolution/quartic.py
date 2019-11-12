# -*- coding: utf-8 -*-


class Quartic:
    MIN_VALUE = -1.28
    MAX_VALUE = 1.28
    def __init__(self):
        pass

    def fitness(self, vector):
        z = 0
        for dimension in range(len(vector)-1):
            z += (dimension+1) * vector[dimension]**4
        return z