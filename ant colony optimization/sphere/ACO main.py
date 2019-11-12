import sphere
import ACO

def main():    
    problema = sphere.Sphere()
    individuos = 32
    dimensiones = [2,4,8,16]
    intervalos = 8
    a = 1
    Q = 20
    evaporacion = 0.9
    t0 = 0.00001
    generaciones = 2000
    for dim in dimensiones:
        for i in range(5):
            aco = ACO.ACO(i,
                  individuos, 
                  dim, 
                  intervalos, 
                  a, 
                  Q,
                  evaporacion,
                  t0,
                  problema,
                  generaciones)
            aco.run()

if __name__ == '__main__':
    main()
