import numpy as np
import matplotlib.pyplot as plt


def main():
    global lines
    dimensions = {"2", "4", "8","16"}
    files = {"quartic", "rastrigin", "rosenbrock", "sphere"}
    for file in files:
        w, h = 4, 20
        data = [[0 for x in range(w)] for y in range(h)]
        cont = 0
        for case in dimensions:
            lists = np.array([[]])
            for i in range(len(dimensions) + 1):
                f = open(file + "/" + file + "_" + str(i) + "_" + case + ".txt", "r")
                lines = f.readlines()
                minn = float(100000)
                maxx = float(0)
                for line in lines:
                    if float(line) < minn:
                        minn = float(line)
                    if float(line) > maxx:
                        maxx = float(line)
                y = np.array(lines)
                y = list(map(lambda x: x.replace('\n',''),y))
                y = np.array(y)
                y = y.astype(np.float)
                print(" Y : ",y)
                if i == 0:
                    lists = np.array([y])
                else:
                    lists = np.append(lists, [y] , axis = 0)
                f.close()
            #print("Average :",file, case, i, np.average(lists, axis=0))
            x = np.linspace(0, 2000, len(lines))
            plt.plot(x, np.average(lists, axis=0),  label="Problema_" +file +"_"+ case)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title("Problema_" +file +"_"+ case)
            plt.legend()
            plt.show()
            data[cont] = list(np.average(lists, axis=0))
            cont = cont + 1
        print("DATA_ ", data)
        x = np.linspace(0, 2000, len(lines))
        cont = 2
        for i in range(4):
            plt.plot(x, data[i])
            cont = cont * 2
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Problema_" +file)
        plt.legend()
        plt.show()

if __name__ == '__main__':
    main()
