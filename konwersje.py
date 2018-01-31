#!/usr/bin/env python
# -*- coding: utf-8 -*-


def dec2other(liczba, podstawa):
    """Konwersja liczby dziesiętnej na system o podanej podstawie"""
    liczba = []  # pusta liczba do zapamietywania reszt
    while liczba10 != 0:
        reszta = liczba10 % podstawa  # obliczanie reszta z dzielenia
        if reszta > 9:
            reszta = chr(reszta + 55)
        liczba.append(str(reszta))
        liczba10 = liczba / podstawa  # uwaga

    liczba.reverse()  # odwrócenia kolejności elementów

    return "".join(liczba)


def zamiana1():
    """Pobieranie danych wejsciowych"""
    liczba = int(input("Podaj liczbę: "))
    podstawa = 0
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawę: "))
    if podstawa > 9:
        for i in liczba:
            if ord(1) > 70
            print("Zły format danych wejściowych")
            return 0

    print("Wynik konwersji: {}(10) = {}({})". format(
        liczba, dec2other(liczba, postawa), podstawa))


def other2dec(liczba, podstawa):
    liczba10 = 0
    potega = len(liczba) - 1
    for cyfra in liczba:
        if not cyfra.isdigit():
            liczba10 += (ord(cyfra.upper()) - 55) * (podstawa ** potega)

        else:
            liczba10 += int(cyfra) * (podstawa ** potega)
        potega -= 1

    return liczba10

def zmiana2():
    liczba = input("Podaj liczbę: ")
    podstawa = 0
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawę: "))
    if podstawa > 9:
        for i in liczba:
            if ord(i) > 70:
                print("Zły format danych wejściowych")
                return 0
    else:
        for i in liczba:
            if int(i) >= podstawa:
                print("Liczba nie może składać się z cyfr > podstawy")
                return 0

    print("Wynik konwersji: {}(10) = {}({})". format(
        liczba, dec2other(liczba, postawa), podstawa))


def main(args):
    print("zamiana liczby dziesiętnej na liczbę o podanej podstawie"
          "<2;16> lub odwrotnie")
    # zamiana1()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
