# -*- coding: utf-8 -*-
import quartic
import AGC

def main():
    s = quartic.Quartic()
    for i in range(5):
        ag = AGC.AGC(32, 16, 2000, 0.02, s, i)
        ag.run()

if __name__ == '__main__':
    main()