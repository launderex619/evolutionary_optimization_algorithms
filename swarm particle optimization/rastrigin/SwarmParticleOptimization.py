import copy
import random


class INDIVIDUAL:
    def __init__(self, vel, dim, problem):
        self._neighbors = []
        self._bestPosition = [random.random() * 10 for i in range(dim)]
        self._position = [random.random() * 10 for i in range(dim)]
        self._velocity = [vel for i in range(dim)]
        self._min = problem.MIN_VALUE
        self._max = problem.MAX_VALUE
        self._bestFitness = (random.random() * 10)
        self._fitness = 100

class SPO:
    # V = velocity
    # O = neighborhoodSize
    # Q1 = cognitionLearningRate
    # Q2 = socialLearningRate
    def __init__(self, i, p, o, n, q1, q2, problem, problem_name, ejecution_number):
        self._ejecution = ejecution_number
        self._problemName = problem_name
        self._iterations = i
        self._problem = problem
        self._socialLearningRate = q2
        self._cognitionLearningRate = q1
        self._maxVelocity = problem.MAX_VALUE
        self._minVelocity = problem.MIN_VALUE
        self._neighborhood = o
        self._individuals = []
        self._particles = p
        self._dimensions = n
        self._bestGlobalFitness = (random.random() * 1000000)
        self._bestGlobalPosition = [random.random() * 1000 for i in range(n)]

    def run(self):
        self.initializeIndividuals()
        self.createNeighborhood()
        print(self._individuals)
        archivo = open(self._problemName + "_" + str(self._ejecution)+"_"+str(self._dimensions)+".txt", "w")
        generation = 0
        while generation < self._iterations:
            for particle in self._individuals:
                for dimension in range(self._dimensions):
                    # calculate the velocity factors
                    particle._velocity[dimension] = ((particle._velocity[dimension]) +
                                                     (self._cognitionLearningRate * (
                                                             particle._bestPosition[dimension] -
                                                             particle._position[dimension])) +
                                                     (self._socialLearningRate * (
                                                                 self._bestGlobalPosition[dimension] -
                                                                 particle._position[dimension])))
                    if particle._velocity[dimension] > self._maxVelocity:
                        particle._velocity[dimension] = self._maxVelocity
                    elif particle._velocity[dimension] < self._minVelocity:
                        particle._velocity[dimension] = self._minVelocity

                    particle._position[dimension] += particle._velocity[dimension]
                # falta definir el fitness y elegir la mejor posicion hasta el momento
                particle._fitness = self.getFitness(particle._position)
                if particle._fitness < particle._bestFitness:
                    particle._bestFitness = particle._fitness
                    particle._bestPosition = particle._position
                if particle._bestFitness < self._bestGlobalFitness:
                    self._bestGlobalFitness = particle._bestFitness
                    self._bestGlobalPosition = copy.copy(particle._bestPosition)
            print("Ejecucion: ", self._ejecution, " Generacion: ", generation, " Mejor posicion: ", self._bestGlobalPosition, ", Mejor fitness: ", self._bestGlobalFitness)
            if generation % 100 == 0:
                archivo.write(str(self._bestGlobalFitness) + "\n")
            generation += 1

    def initializeIndividuals(self):
        for i in range(self._particles):
            velocity = 0  # definir como medir velocidad
            individual = INDIVIDUAL(velocity, self._dimensions, self._problem)
            self._individuals.append(individual)

    def createNeighborhood(self):
        for i in range(self._particles):
            for j in range(self._neighborhood):
                pos = i + 1 + j
                self._individuals[i]._neighbors.append(self._individuals[pos % self._neighborhood])

    def getBestFitness(self, nearest_neighbors):
        best = nearest_neighbors[0].bestFitness
        for i in nearest_neighbors:
            if i.bestFitness < best:
                best = i.bestFitness
        return best

    def getFitness(self, particle):
        return self._problem.fitness(particle)
