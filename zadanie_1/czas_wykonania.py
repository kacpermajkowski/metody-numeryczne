import time

def wyswietl_czas_wykonania(funkcja, parametry):
    czas_rozpoczecia = time.time()
    wynik = funkcja(*parametry)
    czas_zakonczenia = time.time()
    print(f"Funkcja wykonała się po {czas_zakonczenia - czas_rozpoczecia:.6f} sekundach")
    return wynik