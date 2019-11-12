# -*- coding: utf-8 -*-
import rosenbrock
import AGC

def main():
    r = rosenbrock.rosenbrock()
    for i in range(5):
        ag = AGC.AGC(32, 16, 2000, 0.02, r, i)
        ag.run()

if __name__ == '__main__':
    main()