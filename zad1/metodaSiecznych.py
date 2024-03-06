def medtodaSiecznychIteracje(f, a, b, maxI):
    if ((b > a) | (f(a) * f(b) < 0)):
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
