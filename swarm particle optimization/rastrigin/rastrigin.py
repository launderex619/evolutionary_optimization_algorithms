import math as m
class Rastrigin:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    def __init__(self):
        pass
    def fitness(self, vector):
        z = 0
        for alelo in vector:
            z += (alelo**2) - (10 * m.cos(2*m.pi*alelo))
        return z +( 10 * len(vector))
