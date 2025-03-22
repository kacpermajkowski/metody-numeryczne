from zadanie_1.czas_wykonania import wyswietl_czas_wykonania
from zadanie_1.funkcje_poboru_danych import wybierz_funkcje, wybierz_przedzial_poszukiwan, wybierz_warunek_stopu
from zadanie_1.metody_przyblizania import bisekcja, falsi
from zadanie_1.wykresy import rysuj_wykres

def main():
    badana_funkcja, rodzaj_funkcji = wybierz_funkcje()
    przedzial_poszukiwan = wybierz_przedzial_poszukiwan()

    parametry = (badana_funkcja, przedzial_poszukiwan, wybierz_warunek_stopu())
    wynik_bisekcja = wyswietl_czas_wykonania(funkcja=bisekcja, parametry=parametry)
    wynik_falsi = wyswietl_czas_wykonania(funkcja=falsi, parametry=parametry)

    print(f"Bisekcja: {wynik_bisekcja}")
    print(f"Reguła Falsi: {wynik_falsi}")

    wyniki = [wynik_bisekcja, wynik_falsi]
    rysuj_wykres(badana_funkcja, przedzial_poszukiwan, wyniki, rodzaj_funkcji)

if __name__ == "__main__":
    main()