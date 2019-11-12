class rosenbrock:
    MIN_VALUE = -2.048
    MAX_VALUE = 2.048
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        z = 0
        cont = 0
        for i in cromosoma:
            if (cont == len(cromosoma)-1):
                return z
            z += (100 * (cromosoma[cont+1] - cromosoma[cont]**2)**2) + ((cromosoma[cont] - 1)**2)
            cont+=1