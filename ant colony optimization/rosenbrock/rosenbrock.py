class Rosenbrock:
    MIN_VALUE = -2.048
    MAX_VALUE = 2.048
    def __init__(self):
        pass
    def fitness(self, vector):
        z = 0
        for dimension in range(len(vector)-1):
            z += 100 * (vector[dimension + 1] - vector[dimension]**2)**2 + (vector[dimension]-1)**2
        return z
