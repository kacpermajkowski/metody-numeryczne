import numpy as np

def wczytaj_uklad_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as f:
        linie = f.readlines()
        n = int(linie[0])
        A = np.zeros((n, n + 1))
        for i in range(n):
            A[i] = list(map(float, linie[i + 1].split()))
    return A