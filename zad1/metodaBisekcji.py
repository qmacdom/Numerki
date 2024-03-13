import rysowanie


def metodaBisekcjiDokladnosc(f, a, b, epislon):
    if (f(a) * f(b) < 0):
        x = float(a + b) / 2
        i = 0
        while (abs(a - b) > epislon):
            i = i + 1
            x = float(a + b) / 2
            if (f(x) == 0):
                rysowanie.wykresZpunktem(f, a, b, 5, 0, "Metoda Bisekcji Dokladnosc")
                return x, i
            if (f(a) * f(x) < 0):
                b = x
            else:
                a = x
        rysowanie.wykresZpunktem(f, a, b, x, 0, "Metoda Bisekcji Dokladnosc")
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
