import copy
import numpy as np

class Ant:
    def __init__(self, n, B, x, t0):
        #probabilidad de cada intérvalo de cada dimensión
        self._p = np.ones([n,B])/B
        #vector solución
        self._x = x
        #fitness
        self._L = np.finfo(float).max
        #vector de intervalos seleccionados
        self._b = np.ones(n)
        #feromona de cada intervalo de cada dimensión
        self._t = np.ones([n,B])*t0

class ACO:
    def __init__(self,ej, N, n, B, a, Q, p, t0, problema, g):
        #ejecucion
        self._ejecucion = ej
        #cantidad de individuos
        self._N = N
        #cantiad de dimensiones
        self._n = n
        #intérvalos por dimensión
        self._B = B
        #alfa
        self._a = a
        #constante de depósito
        self._Q = Q
        #tasa de evaporación
        self._p = p
        #feromona inicial
        self._t0 = t0
        #problema
        self._problema = problema
        #generaciones
        self._g = g
        #rango
        self._rango = self._problema.MAX_VALUE - self._problema.MIN_VALUE
        #individuos
        self._ants = np.array([])
        #feromona para cada intervalo de cada dimensión
        self._t = np.ones([n, B])*t0
        #mejor histórico
        self._best = []

    def run(self):
        self.crearIndividuos()
        self._best = copy.deepcopy(self._ants[0])
        archivo = open("quartic_" + str(self._ejecucion)+"_"+str(self._n)+".txt", "w")
        generacion = 0
        while generacion < self._g:
            for ant in self._ants:
                for i in range(self._n):
                    for j in range(self._B):
                        ant._p[i][j] = (self._t[i][j]**self._a)/np.sum(self._t[i])
                    idx = self.ruleta(ant._p[i])
                    xi = ( np.random.random() * (self._rango / self._B) +
                          idx * (self._rango / self._B) + self._problema.MIN_VALUE )
                    ant._x[i] = xi
                    ant._b[i] = idx
                ant._L = self._problema.fitness(ant._x)
                if ant._L < self._best._L:
                    self._best = copy.deepcopy(ant)
            for i in range(self._n):
                for j in range(self._B):
                    s = 0.0
                    for ant in self._ants:
                        ant._t[i] = np.zeros(self._B)
                        ant._t[i][int(ant._b[i])] = self._Q/ant._L
                        s += ant._t[i][j]
                    self._t[i][j] = (1-self._p)*self._t[i][j]+s
            if generacion % 100 == 0:
                archivo.write(str(self._best._L) + "\n")
            generacion += 1
            print('generación: ', generacion, 'Mejor histórico: ', self._best._x, self._best._L)
        archivo.close()

    def crearIndividuos(self):
        for i in range(self._N):
            x = np.random.random(size=self._n)*self._rango+self._problema.MIN_VALUE
            ant = Ant(self._n, self._B, x, self._t0)
            self._ants = np.append(self._ants, [ant])

    def ruleta(self, p):
        suma = np.sum(p)
        r = np.random.random()
        k = 0
        F = p[k]
        while F < r:
            k += 1
            F += p[k]
        return k
