import DifferentialEvolution
import rastrigin
problems = 4
iterations = 5


def main():
    problema = rastrigin.Rastrigin()
    problema_nombre = "rastrigin"
    cantidadParticulas = 50
    iteraciones = 2000
    dimensiones = 2
    for dim in range(4):
        for i in range(5):
            de = DifferentialEvolution.DE(iteraciones,
                                                cantidadParticulas,
                                                dimensiones,
                                                problema,
                                                problema_nombre,
                                                i)
            de.run()
        dimensiones = dimensiones*2

if __name__ == '__main__':
    main()
