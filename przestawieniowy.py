#!/usr/bin/env python
# -*- coding: utf-8 -*-

def szyfruj(tekst, klucz):
    reszta = len(tekst) % klucz
    if reszta:
        tekst += (klucz - reszta) * "."


    for i in range(klucz):
        for j in range(int(len(tekst) / klucz)):


            print(i + j * klucz, tekst[i + j*klucz])
            szyfrogram += tekst[i + j]

    return ""


def main(args):
    tekst = input("Podaj tekst: ")

    klucz = int(input("Podaj klucz: ")
    while (2 * klucz > len(tekst)):
        klucz = int(input("Podaj klucz: "))

    szyfrogram = szyfruj(tekst, klucz)
    print(szyfrogram)
    # print(deszyruj(szyfrogram, klucz))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
