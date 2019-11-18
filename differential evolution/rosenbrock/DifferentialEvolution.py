import copy
import random


class DE:
    def __init__(self, i, p, n, problem, problem_name, ejecution_number):
        self._ejecution = ejecution_number
        self._problemName = problem_name
        self._iterations = i
        self._problem = problem
        self._maxValue = problem.MAX_VALUE
        self._minValue = problem.MIN_VALUE
        self._individuals = [[]]
        self._particles = p
        self._dimensions = n
        self._bestGlobalFitness = 100000
        self._F = 0.4
        self._C = 0.4
        self._bestGlobalIndivudual = []

    def run(self):
        self.initializeIndividuals()
        #self.initializeBestFitness()
        print(self._individuals)
        archivo = open(self._problemName + "_" + str(self._ejecution)+"_"+str(self._dimensions)+".txt", "w")
        generation = 0
        while generation < self._iterations:
            for individual in self._individuals:
                randomIndividuals = self.getRandomIndividuals(individual)
                x1 = randomIndividuals[0]
                x2 = randomIndividuals[1]
                x3 = randomIndividuals[2]
                difference = [x2_i - x3_i for x2_i, x3_i in zip(x2, x3)]
                mutant_vector = [x1_i + self._F * difference_i for x1_i, difference_i in zip(x1, difference)]
                test_vector = []
                for k in range(self._dimensions):
                    crossover = random.random()
                    if crossover <= self._C:
                        test_vector.append(mutant_vector[k])
                    else:
                        test_vector.append(individual[k])

                testFitness = self._problem.fitness(test_vector)
                actualFitness = self._problem.fitness(individual)
                
                if(testFitness < actualFitness):
                    individual = test_vector
                    if(testFitness < self._bestGlobalFitness):
                        self._bestGlobalFitness = testFitness
                        self._bestGlobalIndivudual = individual
            
            print("Ejecucion: ", self._ejecution, " Generacion: ", generation, " Mejor vector: ", self._bestGlobalIndivudual, ", Mejor fitness: ", self._bestGlobalFitness)
            if generation % 100 == 0:
                archivo.write(str(self._bestGlobalFitness) + "\n")
            generation += 1

    def initializeIndividuals(self):
        self._individuals.clear()
        for i in range(self._particles):
            velocity = 0  # definir como medir velocidad
            individual = [random.uniform(self._minValue, self._maxValue) for x in range(self._dimensions)]
            self._individuals.append(individual)
        self._bestGlobalIndivudual = self._individuals[0]

    def getRandomIndividuals(self, actual):
        return random.sample(copy.copy(self._individuals), 3)

    def getBestFitness(self, nearest_neighbors):
        best = nearest_neighbors[0].bestFitness
        for i in nearest_neighbors:
            if i.bestFitness < best:
                best = i.bestFitness
        return best

    def getFitness(self, particle):
        return self._problem.fitness(particle)
