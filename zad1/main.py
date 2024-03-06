import matplotlib.pyplot as plt


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


def metodaBisekcjiDokladnosc(f, a, b, epislon):
    if (f(a) * f(b) < 0):
        x = float(a + b) / 2
        i = 0
        while (abs(a - b) > epislon):
            i = i + 1
            x = float(a + b) / 2
            if (f(x) == 0):
                return x, i
            if (f(a) * f(x) < 0):
                b = x
            else:
                a = x
        return x, i
    else:
        print("Funkcja na tym przedziale nie przechodzi przez 0")
        return "Błąd"


def metodaBisekcjiIteracje(f, a, b, maxI):
    i = maxI
    if (maxI < 0):
        return "Liczba iteracji ma być dodatnia!"
    if (f(a) * f(b) < 0):
        x = float(a + b) / 2
        while (maxI > 0):
            maxI = maxI - 1
            x = float(a + b) / 2
            if (f(x) == 0):
                return x
            if (f(a) * f(x) < 0):
                b = x
            else:
                a = x
        return x, maxI
    else:
        print("Wartości funkcji na krańcach tego przedziału mają ten sam znak!")
        return "Błąd"


def medtodaSiecznychIteracje(f, a, b, maxI):
    # if ((b < a) | (f(a) * f(b) < 0)):
    #     return "Błąd"
    x1, x2, i = a, b, maxI
    while (maxI > 0):
        maxI = maxI - 1
        temp = x1
        x1 = x1 - ((f(x1) * (x1 - x2)) / (f(x1) - f(x2)))
        x2 = temp
        # print(x1, x2)
    return x1


def medtodaSiecznychDokladnosc(f, a, b, epsilon):
    # if ((b < a) | (f(a) * f(b) < 0)):
    #     return "Błąd"
    x1, x2 = a, b
    i = 0
    while (abs(x1 - x2) > epsilon):
        i = i + 1
        temp = x1
        x1 = x1 - ((f(x1) * (x1 - x2)) / (f(x1) - f(x2)))
        x2 = temp
        # print(x1,x2)
    return x1, i


# funkcje = [kwadratowa]

# wsp, stp = pobieranieWielomianu()
# x = int(input("Podaj wartość wielomianu: "))

# print(f"Wartość wielomianu o współczynnikach {wsp} w punkcie {x} wynosi", SchematHornera(x, wsp, stp))

print(metodaBisekcjiIteracje(kwadratowa, -20, 20, 200))
print(metodaBisekcjiDokladnosc(kwadratowa, -20, 20, 0.00000000001))
print(medtodaSiecznychIteracje(kwadratowa, -20, 20, 11))
print(medtodaSiecznychDokladnosc(kwadratowa, -20, 20, 0.00000000001))

narysujWykres(kwadratowa, -20, 20)
