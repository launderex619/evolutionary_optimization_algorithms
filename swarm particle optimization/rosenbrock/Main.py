import SwarmParticleOptimization
import rosenbrock
problems = 4
iterations = 5


def main():
    problema = rosenbrock.Rosenbrock()
    problema_nombre = "rosenbrock"
    cantidadParticulas = 50
    tamanioVecindario = 16
    iteraciones = 2000
    dimensiones = 2
    cognitionLearningRate = 1.4944
    socialLearningRate = 1.4944
    for dim in range(4):
        for i in range(5):
            spo = SwarmParticleOptimization.SPO(iteraciones,
                                                cantidadParticulas,
                                                tamanioVecindario,
                                                dimensiones,
                                                cognitionLearningRate,
                                                socialLearningRate,
                                                problema,
                                                problema_nombre,
                                                i)
            spo.run()
        dimensiones = dimensiones*2

if __name__ == '__main__':
    main()
