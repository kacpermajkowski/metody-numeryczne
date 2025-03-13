
def iterator_metody(wzor_na_c, funkcja, przedzial_poszukiwan, warunek_stopu, wartosc_warunku_stopu):
    a, b = przedzial_poszukiwan
    iteracje = 0
    wynik = None
    while wynik is None:
        # Dodac warunek, czy znaleziono miejsce zerowa = 0
        c = wzor_na_c(a, b)
        iteracje += 1
        if warunek_stopu == 1 and abs(funkcja(c)) < wartosc_warunku_stopu:
            wynik = c
        if warunek_stopu == 2 and iteracje >= wartosc_warunku_stopu:
            wynik = c
        if funkcja(a) * funkcja(c) < 0:
            b = c
        else:
            a = c
    print(f"Przybliżenie Nazwa ukonczone zostalo po {iteracje} iteracjach ")
    return wynik

def bisekcja(funkcja, przedzial_poszukiwan, warunek_stopu, wartosc_warunku_stopu):
    c = lambda a, b: (a+b)/2
    return iterator_metody(c, funkcja, przedzial_poszukiwan, warunek_stopu, wartosc_warunku_stopu)

def falsi(funkcja, przedzial_poszukiwan, warunek_stopu, wartosc_warunku_stopu):
    c = lambda a, b: b - (funkcja(b) * (a - b)) / (funkcja(a) - funkcja(b))
    return iterator_metody(c, funkcja, przedzial_poszukiwan, warunek_stopu, wartosc_warunku_stopu)

def sprawdz_warunek_zmiany_znaku(funkcja, przedzial_poszukiwan):
    a, b = przedzial_poszukiwan
    if funkcja(a) * funkcja(b) >= 0:
        print("Funkcja nie spełnia warunku zmiany znaku na krańcach przedziału.")
        return False
    else:
        return True