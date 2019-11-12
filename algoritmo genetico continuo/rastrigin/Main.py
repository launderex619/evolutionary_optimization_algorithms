# -*- coding: utf-8 -*-
import rastrigin
import AGC

def main():
    r = rastrigin.Rastrigin()
    for i in range(5):
        ag = AGC.AGC(32, 16, 2000, 0.02, r, i)
        ag.run()

if __name__ == '__main__':
    main()