#Do funkcji wielomianowej

# Korzystamy tutaj ze sposobu Hornera
def oblicz_wartosc_wielomianu(x, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * x + wspolczynniki[i]
    return wynik
