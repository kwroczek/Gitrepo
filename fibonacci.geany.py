#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib_iter(n):
    """funkcja wyświetla kolejne wyrazy ciągu Finabocciego
    funkcja zwraca n-ty wyraz ciągu
    F(0) = 0
    F(1) = 1
    F(n) = F(n-2) + F(n-2) dla n > 1
    """
    a, b = (0, 1)
    if n == 0:
        print a
        return a
    elif n == 1:
        print b
        return b

    for i in range(1, n):


    return b


def main(args):
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
