import metodaBisekcji
import metodaSiecznych
from math import *
from wielomian import wielomian
from wykladnicza import wykladnicza
from trygonometryczna import trygonometryczna


def zlozenie(_x):
    return sin(_x)+(0.1*_x*_x)-1

poczatek = 1
while poczatek:

    funktor = 0

    wyb = 1
    while wyb:
        funktorNumer = int(input("Dostępne funkcje: \n1 - wielomian\n2 - trygonometryczna\n3 - wykładnicza\n4 - złożenie\nWybór: "))
        match funktorNumer:
            case 1:
                funktor = wielomian().SchematHornera
                wyb = 0
            case 2:
                funktor = trygonometryczna().wartosc
                wyb = 0
            case 3:
                funktor = wykladnicza().wartosc
                wyb = 0
            case 4:
                funktor = zlozenie
                wyb = 0
            case _:
                print("Wybrano niedostępną opcję")

    a = float(input("Podaj lewy przedział: "))
    b = float(input("Podaj prawy przedział: "))
    warStopu = 0
    wyjscie = 1
    while wyjscie:
        warStopu = int(input("1 - iteracje \n2 - dokładność\n0 - wyjscie z programu\n9 - powrót do poczatku programu\nWybierz ograniczenie: "))
        match warStopu:
            case 1:
                maxI = int(input("Podaj liczbę iteracji: "))
                wybranaMetoda = int(input("1 - metoda Bisekcji\n2 - metoda Siecznych\nWybierz metodę: "))
                match wybranaMetoda:
                    case 1:
                        print(metodaBisekcji.metodaBisekcjiIteracje(funktor, a, b, maxI))
                    case 2:
                        print(metodaSiecznych.medtodaSiecznychIteracje(funktor, a, b, maxI))
            case 2:
                epsilon = float(input("Podaj dokładność (epsilon) : "))
                wybranaMetoda = int(input("1 - metoda Bisekcji\n2 - metoda Siecznych\nWybierz metodę: "))
                match wybranaMetoda:
                    case 1:
                        print(metodaBisekcji.metodaBisekcjiDokladnosc(funktor, a, b, epsilon))
                    case 2:
                        print(metodaSiecznych.medtodaSiecznychDokladnosc(funktor, a, b, epsilon))
            case 9:
                print("Wracamy do poczatku.")
                break
            case 0:
                print("Wyjście z programu.")
                poczatek=0
                break
            case _:
                print("Podano nieodpowiednią opcje, wybierz poprawną.")