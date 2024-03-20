import matplotlib.pyplot as plt


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


def wykresZpunktem(f, a, b, punktx, punkty, tytul):
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
    plt.plot(punktx, punkty, 'ro')
    plt.annotate(f"[{punktx} , {punkty}]", ((punktx), (punkty)),((punktx), (punkty)), ha='center')
    plt.title(tytul)

    plt.show()
