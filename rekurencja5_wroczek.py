#!/usr/bin/env python
# -*- coding: utf-8 -*-


def ciag(n):
    if n == 0:
        return 0
    return ciag(n - 1) + (n - 1) * 2

def main(args):
    n = int(input ('podaj wyraz ciągu: '))
    print(ciag(n))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
