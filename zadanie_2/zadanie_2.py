import numpy as np
from wczytaj_uklad import wczytaj_uklad_z_pliku
from wypisz_rozwiazanie import wypisz_rozwiazanie


def eliminacja_jordana(A):
    n, m = A.shape
    n = n  # ilość równań

    for i in range(n):
        # Szukamy elementu głównego
        max_row = i + np.argmax(np.abs(A[i:, i]))
        if abs(A[max_row][i]) < 1e-12:
            continue  # element główny to zero — możliwe, że układ nieoznaczony lub sprzeczny

        # Zamieniamy wiersze
        A[[i, max_row]] = A[[max_row, i]]

        # Dzielimy wiersz przez element główny
        A[i] = A[i] / A[i][i]

        # Zerujemy kolumnę (z wyjątkiem bieżącego wiersza)
        for j in range(n):
            if j != i:
                A[j] = A[j] - A[j][i] * A[i]

    return A

def interpretuj_rozwiazanie(A):
    n, m = A.shape
    A = np.round(A, decimals=6)  # zaokrąglij by uniknąć błędów numerycznych
    rozwiązanie = np.zeros(n)

    for i in range(n):
        # Jeśli cały wiersz (oprócz ostatniej kolumny) to zera, a wyraz wolny ≠ 0 → sprzeczny
        if np.allclose(A[i, :-1], 0) and not np.isclose(A[i, -1], 0):
            return "Układ sprzeczny", None

        # Jeśli cały wiersz to zera → nieoznaczony
        if np.allclose(A[i], 0):
            return "Układ nieoznaczony", None

        rozwiązanie[i] = A[i, -1]

    return "Układ oznaczony", rozwiązanie

if __name__ == "__main__":
    nazwa_pliku = "zadanie_2/uklady/k.txt"
    macierz = wczytaj_uklad_z_pliku(nazwa_pliku)
    A_po_jordanie = eliminacja_jordana(macierz.copy())
    status, rozwiazanie = interpretuj_rozwiazanie(A_po_jordanie)
    wypisz_rozwiazanie(status, rozwiazanie)
