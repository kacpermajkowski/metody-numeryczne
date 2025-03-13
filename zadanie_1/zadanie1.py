from czas_wykonania import wyswielt_czas_wykonania
from zadanie_1.funkcje_poboru_danych import wybor_funkcji, pobierz_przedzial_poszukiwan, wybierz_warunek_stopu
from zadanie_1.metody_przyblizania import bisekcja, falsi
from zadanie_1.wykresy import rysuj_wykres

def main():
    badana_funkcja = wybor_funkcji()
    przedzial_poszukiwan = pobierz_przedzial_poszukiwan()
    wybor_stop, wartosc_stop = wybierz_warunek_stopu()

    parametry = (badana_funkcja, przedzial_poszukiwan, wybor_stop, wartosc_stop)
    wynik_bisekcja = wyswielt_czas_wykonania(metoda=bisekcja, parametry=parametry)
    wynik_falsi = wyswielt_czas_wykonania(metoda=falsi, parametry=parametry)

    print(f"Bisekcja: {wynik_bisekcja}")
    print(f"Reguła Falsi: {wynik_falsi}")

    rysuj_wykres(badana_funkcja, przedzial_poszukiwan, wynik_bisekcja)
    rysuj_wykres(badana_funkcja, przedzial_poszukiwan, wynik_falsi)

if __name__ == "__main__":
    main()