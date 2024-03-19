import metodaBisekcji
import metodaSiecznych
from wielomian import wielomian


# @staticmethod
# def SchematHornera(x, wspTab):
#     wynik = wspTab[0]  # dzieki temu współczynnik ten
#
#     for stopien in wspTab:
#         wynik = wynik * x + wspTab[stopien + 1]
#     return wynik


# def pobieranieWielomianu():
#     stopien = int(input("Podaj stopien wielomianu: "))
#     wspTab = []
#     for i in reversed(range(int(stopien + 1))):
#         print(f"Podaj współczynniki wielomianu dla stopnia : {i} ")
#         wspTab.append(float(input()))
#     return wspTab, stopien


def kwadratowa(_x):
    return (_x + 2) * (_x - 7)


# wsp, stp = pobieranieWielomianu()
# x = int(input("Podaj wartość wielomianu: "))

# print(f"Wartość wielomianu o współczynnikach {wsp} w punkcie {x} wynosi", SchematHornera(x, wsp, stp))

# asd = wielomian()

# tablica_funkcji = [kwadratowa, asd.SchematHornera]
# wiel = 0
# input()
# if(True):
#     wiel = wielomian()
# else:
#     print("dadadad")

# print((tablica_funkcji[1](5)))

# MENU
# wyjscie = 1
# while wyjscie:
#     while True:
#         print("Wybierz którąs z poniższych funkcji:")
#         print("1. wielomian")
#         print("2. trygonometryczna")
#         print("3. wykładnicza")
#         print("4. złożenie")
#         print("5. wjsc z programu")


a = float(input("podaj lewy przedział: "))
b = float(input("Podaj prawy przedział: "))
choice = 0
wyjscie = 1
while wyjscie:
    choice = int(input("Wybierz opcje: "))
    match choice:
        case 1:
            print(metodaBisekcji.metodaBisekcjiIteracje(kwadratowa, a, b, 200000))
        case 2:
            print(metodaBisekcji.metodaBisekcjiDokladnosc(kwadratowa, a, b, 0.00000000001))
        case 3:
            print(metodaSiecznych.medtodaSiecznychIteracje(kwadratowa, a, b, 12))
        case 4:
            print(metodaSiecznych.medtodaSiecznychDokladnosc(kwadratowa, a, b, 0.00000000001))
        case 5:
            print("Idziemy wyżej.")
            break
        case _:
            print("Podano nieodpowiednią opcje, wybierz poprawną.")
funkcje = []

# print(metodaBisekcji.metodaBisekcjiIteracje(kwadratowa, 0, 20, 200000))
# print(metodaBisekcji.metodaBisekcjiDokladnosc(kwadratowa, 0, 20, 0.00000000001))
# print(metodaSiecznych.medtodaSiecznychIteracje(kwadratowa, 3, 20, 200))
# print(metodaSiecznych.medtodaSiecznychDokladnosc(kwadratowa, 3, 20, 0.00000000001))

# rysowanie.narysujWykres(kwadratowa, -10, 10)
