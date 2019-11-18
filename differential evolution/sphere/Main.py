import DifferentialEvolution
import sphere
problems = 4
iterations = 5


def main():
    problema = sphere.Sphere()
    problema_nombre = "sphere"
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
