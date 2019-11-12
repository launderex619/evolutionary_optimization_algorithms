# -*- coding: utf-8 -*-
import sphere
import AGC

def main():
    s = sphere.Sphere()
    for i in range(5):
        ag = AGC.AGC(32, 16, 2000, 0.02, s, i)
        ag.run()

if __name__ == '__main__':
    main()