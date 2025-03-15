
def iterator_metody(wzor_na_c, funkcja, przedzial_poszukiwan, warunek_stopu, nazwa_metody):
    typ_warunku_stopu, wartosc_warunku_stopu = warunek_stopu
    a, b = przedzial_poszukiwan
    iteracje = 0
    wynik = None
    while wynik is None:
        c = wzor_na_c(a, b)
        iteracje += 1
        if typ_warunku_stopu == 1 and abs(funkcja(c)) < wartosc_warunku_stopu:
            wynik = c
        if typ_warunku_stopu == 2 and iteracje >= wartosc_warunku_stopu:
            wynik = c
        if funkcja(a) * funkcja(c) < 0:
            b = c
        else:
            a = c
    print(f"Przybliżenie {nazwa_metody} ukonczone zostalo po {iteracje} iteracjach ")
    return wynik

def bisekcja(funkcja, przedzial_poszukiwan, warunek_stopu):
    c = lambda a, b: (a+b)/2
    return iterator_metody(c, funkcja, przedzial_poszukiwan, warunek_stopu, "biekcja")

def falsi(funkcja, przedzial_poszukiwan, warunek_stopu):
    c = lambda a, b: (funkcja(b) * a - funkcja(a)*b ) / (funkcja(b) - funkcja(a))
    return iterator_metody(c, funkcja, przedzial_poszukiwan, warunek_stopu, "falsi")

def sprawdz_warunek_zmiany_znaku(funkcja, przedzial_poszukiwan):
    a, b = przedzial_poszukiwan
    if funkcja(a) * funkcja(b) >= 0:
        print("Funkcja nie spełnia warunku zmiany znaku na krańcach przedziału.")
        return False
    else:
        return True