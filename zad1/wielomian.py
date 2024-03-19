class wielomian:
    wspTab = []
    stopien = 0

    def __init__(self):
        print("Wybrano funkcje \"wielomian\"")

        stopien = int(input("Podaj stopien wielomianu: "))
        for i in reversed(range(int(stopien + 1))):
            print(f"Podaj współczynniki wielomianu dla stopnia : {i} ")
            self.wspTab.append(float(input()))
        self.stopien = stopien

    def SchematHornera(self, x):
        wynik = self.wspTab[0]  # dzieki temu współczynnik ten

        for stopien in range(self.stopien + 1):
            wynik = wynik * x + self.wspTab[stopien + 1]
        return wynik
