def medtodaSiecznychIteracje(f, a, b, maxI):
    if ((b > a) & (f(a) * f(b) < 0)):
        #     return "Błąd"
        x_n, x__1, i = b, a, maxI
        while (maxI > 0):
            #print(x__1, x_n)
            maxI = maxI - 1
            temp = x_n
            if (f(x_n) == f(x__1)):
                return x_n, (i-maxI)
            x_n = x_n - ((f(x_n) * (x_n - x__1)) / (f(x_n) - f(x__1)))

            x__1 = temp
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
            return x1
        x1 = x1 - ((f(x1) * (x1 - x2)) / (f(x1) - f(x2)))
        x2 = temp
        # print(x1,x2)

    return x1, i
