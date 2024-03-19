import rysowanie
def medtodaSiecznychIteracje(f, a, b, maxI):
    if ((b > a) & (f(a) * f(b) < 0)):
        #     return "Błąd"
        x_n, x__1, i = b, a, maxI
        while (maxI > 0):
            print(x__1, x_n)
            maxI = maxI - 1
            temp = x_n
            if (f(x_n) == f(x__1)):
                if(((x_n < a)) | ((x_n) > b)):
                    print("Metoda znalazła poprawne miejsce zerowe, jednak z racji na jej działanie, jest ono poza podanym zakresem.")
                rysowanie.wykresZpunktem(f, a, b, x_n, f(x_n),f"Metoda Siecznych maxI : {i}, liczba iteracji {i-maxI}")
                return x_n, (i-maxI)
            x_n = x_n - ((f(x_n) * (x_n - x__1)) / (f(x_n) - f(x__1)))

            x__1 = temp
        if (((x_n < a)) | ((x_n) > b)):
            print("Metoda znalazła poprawne miejsce zerowe, jednak z racji na jej działanie, jest ono poza podanym zakresem.")
        rysowanie.wykresZpunktem(f, a, b, x_n, f(x_n), f"Metoda Siecznych maxI : {i}, liczba iteracji {i - maxI}")
        return x_n, int(i-maxI)


def medtodaSiecznychDokladnosc(f, a, b, epsilon):
    # if ((b < a) | (f(a) * f(b) < 0)):
    #     return "Błąd"
    x1, x2 = b, a
    i = 0
    while (abs(x1 - x2) > epsilon):
        i = i + 1
        temp = x1
        if (f(x1) == f(x2)):
            if (((x1 < a)) | ((x1) > b)): #może się tak zdarzyć
                print("Metoda znalazła poprawne miejsce zerowe, jednak z racji na jej działanie, jest ono poza podanym zakresem.")
            rysowanie.wykresZpunktem(f, a, b, x1, f(x1), f"Metoda Siecznych Dokladnosc : {epsilon}, liczba iteracji {i}")
            return x1,i
        x1 = x1 - ((f(x1) * (x1 - x2)) / (f(x1) - f(x2)))
        x2 = temp
    if (((x1 < a)) | ((x1) > b)):
        print("Metoda znalazła poprawne miejsce zerowe, jednak z racji na jej działanie, jest ono poza podanym zakresem.")
    rysowanie.wykresZpunktem(f, a, b, x1, f(x1), f"Metoda Siecznych Dokladnosc : {epsilon}, liczba iteracji {i}")
    return x1, i
