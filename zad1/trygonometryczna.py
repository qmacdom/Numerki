from math import *


class trygonometryczna:
    a = 0.0
    b = 0.0
    func = [sin, cos, tan]
    wyb = 0

    def __init__(self):
        print(
            "Wybrano funkcje \"trygonoemtryczna\" ogólny wzór to: a*funkcja(b*x) \n1 - sinus\n2 - cosinus\n3 - tangens\n Wybierz rodzaj funkcji trygonometrycznej: ")
        while True:
            self.wyb = int(input())
            if ((self.wyb <= 3) | (self.wyb >= 1)):
                self.wyb = self.wyb - 1
                break
        self.a = float(input("Podaj współczynnik a: "))
        self.b = float(input("Podaj współczynnik b: "))

    def wartosc(self, _x):
        wynik = self.a * (self.func[self.wyb](self.b * (_x)))
        return wynik
