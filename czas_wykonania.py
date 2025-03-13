import time

def wyswielt_czas_wykonania(metoda, parametry):
    czas_rozpoczecia = time.time()
    wynik = metoda(*parametry)
    czas_zakonczenia = time.time()
    print(f"Funkcja wykonała się po {czas_zakonczenia - czas_rozpoczecia:.6f} sekundach")
    return wynik