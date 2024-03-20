from math import *


class wykladnicza:
    a = 0.0
    b = 0.0
    c = 0.0

    def __init__(self):
        print("Wybrano funkcje \"wykladnicza\" mająca wzór ((a)^bx)-c")
        self.a = float(input("Podaj podstawę (a): "))
        self.b = float(input("Podaj wykładnik (b): "))
        self.c = float(input("Podaj wartość wyrazu wolnego c (powinien być ujemny aby przecięto oś Ox): "))

    def wartosc(self, _x):
        wynik = pow(self.a, (self.b * _x)) + self.c
        return wynik
