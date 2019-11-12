import numpy as np

class Monedas:
    def __init__(self, monedas, adyacencias):
        self.monedas = monedas
        self.adyacencias = adyacencias
    
    def f(self, cromosoma):
        #funcion de fitness = max(sum[monedas]) donde el contador es += adyacencias
        f = 0
        if cromosoma[0] == 1:
            f = self.monedas[0]
        prev = 0
        act = 0
        for i in range(1, len(cromosoma)):
            prev = cromosoma[i - 1]
            act = cromosoma[i]
            if prev == 1:
                if act == 1:
                    return 0
            if(act == 1):
                f = f + self.monedas[i]
        return f