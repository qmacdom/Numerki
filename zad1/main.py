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
    return (_x * _x - 5 * x - 60)


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
        return x
    else:
        print("Wartości funkcji na krańcach tego przedziału mają ten sam znak!")
        return "Błąd"


def medtodaSiecznychIteracje(f, a, b, maxI):
    # if ((b < a) | (f(a) * f(b) < 0)):
    #     return "Błąd"
    x1, x2 = a, b
    while (maxI > 0):
        maxI = maxI - 1
        temp = x2
        f1 = f(x1)
        f2 = f(x2)
        x1 = x1 - ((f(x1) * (x1 - x2)) / (f(x1) - f(x2)))
        x2 = temp
    return x1


def medtodaSiecznychDokladnosc(f, a, b, dokladnosc):
    # if ((b < a) | (f(a) * f(b) < 0)):
    #     return "Błąd"
    x1, x2 = a, b
    i = 0
    while (abs(x1 - x2) > dokladnosc):
        i = i + 1
        temp = x2
        f1 = f(x1)
        f2 = f(x2)
        x1 = x1 - ((f(x1) * (x1 - x2)) / (f(x1) - f(x2)))
        x2 = temp
    return x1, i


funkcje = [kwadratowa]

wsp, stp = pobieranieWielomianu()
x = int(input("Podaj wartość wielomianu: "))

print(f"Wartość wielomianu o współczynnikach {wsp} w punkcie {x} wynosi", SchematHornera(x, wsp, stp))

print(metodaBisekcjiIteracje(kwadratowa, -1, 8, 200))
print(metodaBisekcjiDokladnosc(kwadratowa, -1, 8, 0.0000001))
print(medtodaSiecznychIteracje(kwadratowa, -2.1, 10.5, 2000))
print(medtodaSiecznychDokladnosc(kwadratowa, -2.1, 10.5, 0.01))

narysujWykres(kwadratowa, -20, 20)
