import matplotlib.pyplot as plt
import metodaBisekcji
import metodaSiecznych
import wielomian

@staticmethod
def SchematHornera(x, wspTab, length):
    wynik = wspTab[0]  # dzieki temu współczynnik ten

    for stopien in range(length):
        wynik = wynik * x + wspTab[stopien + 1]
    return wynik


def pobieranieWielomianu():
    stopien = int(input("Podaj stopien wielomianu: "))
    wspTab = []
    for i in reversed(range(int(stopien + 1))):
        print(f"Podaj współczynniki wielomianu dla stopnia : {i} ")
        wspTab.append(float(input()))
    return wspTab, stopien


def narysujWykres(f, a, b):
    zbiorf = []
    zbiorx = []
    while (a < b):
        a = a + 0.05
        zbiorf.append(f(a))
        zbiorx.append(a)
    plt.plot(zbiorx, zbiorf)
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()


def kwadratowa(_x):
    return (_x - 5) * (_x + 2) * (_x - 7)


# wsp, stp = pobieranieWielomianu()
# x = int(input("Podaj wartość wielomianu: "))

# print(f"Wartość wielomianu o współczynnikach {wsp} w punkcie {x} wynosi", SchematHornera(x, wsp, stp))

# MENU
# wyjscie = 1
# choice = 0
# while wyjscie:
#     while True:
#         print("Wybierz którąs z poniższych funkcji:")
#         print("1. wielomian")
#         print("2. trygonometryczna")
#         print("3. wykładnicza")
#         print("4. złożenie")
#         print("5. wjsc z programu")
#         input(choice)
#         match choice:
#             case 1:
#                 print(metodaBisekcji.metodaBisekcjiIteracje(kwadratowa, -19.8746869, 20, 200000))
#             case 2:
#                 print(metodaBisekcji.metodaBisekcjiDokladnosc(kwadratowa, -20, 20, 0.00000000001))
#             case 3:
#                 print(metodaSiecznych.medtodaSiecznychIteracje(kwadratowa, -20, 20, 12))
#             case 4:
#                 print(metodaSiecznych.medtodaSiecznychDokladnosc(kwadratowa, -20, 20, 0.00000000001))
#                 break
#             case 5:
#                 wyjscie = 0
#                 break
            #case _:
               # print("Podano nieodpowiednią opcje, wybierz poprawną.")
funkcje = []

print(metodaBisekcji.metodaBisekcjiIteracje(kwadratowa, -19.8746869, 20, 200000))
print(metodaBisekcji.metodaBisekcjiDokladnosc(kwadratowa, -20, 20, 0.00000000001))
print(metodaSiecznych.medtodaSiecznychIteracje(kwadratowa, -20, 20, 12))
print(metodaSiecznych.medtodaSiecznychIteracje(kwadratowa, -20, 20, 13))
print(metodaSiecznych.medtodaSiecznychDokladnosc(kwadratowa, -20, 20, 0.00000000001))

narysujWykres(kwadratowa, -20, 20)
