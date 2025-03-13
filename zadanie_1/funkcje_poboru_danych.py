
MENU_WYBORU_FUNKCJI = [
    "Wybierz funkcję:",
    "1 - Wielomianowa",
    "2 - Trygonometryczna",
    "3 - Wykładnicza",
    "4 - Złożenie funkcji"
]

MENU_WARUNKU_STOPU = [
    "Wybierz warunek stopu:",
    "1 - Dokładność epsilon",
    "2 - Maksymalna liczba iteracji"
]

def pobierz_liczbe_calkowita():
    liczba = None
    while liczba is None:
        try:
            liczba = int(input("Podaj liczbę całkowitą: "))
        except ValueError:
            print("To nie jest liczba całkowita, spróbuj ponownie.")
    return liczba


def pobierz_liczbe_rzeczywista():
    liczba = None
    while liczba is None:
        try:
            liczba = float(input("Podaj liczbę rzeczywistą: "))
        except ValueError:
            print("To nie jest liczba rzeczywista, spróbuj ponownie.")
    return liczba

def pobierz_liczby_rzeczywiste(ilosc):
    liczby = []
    for i in range(ilosc):
        liczby.append(pobierz_liczbe_rzeczywista())
    liczby = tuple(liczby)
    return liczby

def wybierz_funkcje():
    from zadanie_1.definicje_funkcji import \
        pobierz_funkcje_wielomianowa, \
        pobierz_funkcje_trygonometryczna, \
        pobierz_funkcje_wykladnicza

    funkcja = None
    while funkcja is None:
        drukuj_liste_string(MENU_WYBORU_FUNKCJI)
        wybor = pobierz_liczbe_calkowita()

        if wybor == 1:
            funkcja = pobierz_funkcje_wielomianowa()
        if wybor == 2:
            funkcja = pobierz_funkcje_trygonometryczna(),
        if wybor == 3:
            funkcja = pobierz_funkcje_wykladnicza()
        if wybor == 4:
            funkcja = wybor_skladania_funkcji()

        if(funkcja is None):
            print("Niepoprawny wybór, spróbuj ponownie.")
    return funkcja

def pobierz_wspolczynniki_wielomianu():
    print("Podaj stopień wielomianu: ")
    stopien = pobierz_liczbe_calkowita()
    wspolczynniki = []
    for i in range(stopien + 1):
        print(f"Podaj współczynnik przy x^{stopien - i}: ")
        wspolczynniki.append(pobierz_liczbe_rzeczywista())
    return wspolczynniki

def wybierz_przedzial_poszukiwan():
    print("Podaj przedział poszukiwań:")
    a, b = None, None
    while a is None or b is None or a >= b:
        a, b = pobierz_liczbe_rzeczywista(), pobierz_liczbe_rzeczywista()
        if a >= b:
            print("Lewy przedział musi być mniejszy od prawego!")
        if a is None or b is None:
            print("Oba krańce przedziału muszą być zdefiniowane")
    return a, b

#
#   Wybór warunków stopu
#

def wybierz_warunek_stopu():
    drukuj_liste_string(MENU_WARUNKU_STOPU)

    wybor = None
    while wybor not in [1, 2]:
        wybor = pobierz_liczbe_calkowita()
        if wybor not in [1, 2]:
            print("Niepoprawny wybór, spróbuj ponownie.")

    if wybor == 1:
        wartosc = epsilon()
    else:
        wartosc = pobierz_liczbe_iteracji()

    return wybor, wartosc

def pobierz_liczbe_iteracji():
    liczba_iteracji = None
    while liczba_iteracji is None or liczba_iteracji <= 0:
        liczba_iteracji = pobierz_liczbe_calkowita()
        if liczba_iteracji <= 0:
            print("Liczba iteracji musi być większa od zera.")
    return liczba_iteracji

def epsilon():
    epsilon = None
    while epsilon is None or epsilon <= 0:
        epsilon = pobierz_liczbe_rzeczywista()
        if epsilon <= 0:
            print("Epsilon musi być większy od zera.")
    return epsilon

def drukuj_liste_string(lista_string):
    for string in lista_string:
        print(string)

def wybor_skladania_funkcji():
    from zadanie_1.definicje_funkcji import \
        pobierz_funkcje_wielomianowa, \
        pobierz_funkcje_trygonometryczna, \
        pobierz_funkcje_wykladnicza
    print("Wybierz dwie różne funkcje do składania:")
    print("1 - Wielomianowa")
    print("2 - Trygonometryczna")
    print("3 - Wykładnicza")

    wybor1 = None
    wybor2 = None

    while wybor1 == wybor2:
        wybor1 = pobierz_liczbe_calkowita()
        wybor2 = pobierz_liczbe_calkowita()
        if wybor1 == wybor2:
            print("Musisz wybrać dwie różne funkcje!")

    funkcje = {
        1: pobierz_funkcje_wielomianowa,
        2: pobierz_funkcje_trygonometryczna,
        3: pobierz_funkcje_wykladnicza
    }

    f1 = funkcje[wybor1]()
    f2 = funkcje[wybor2]()

    print("Wybierz sposób składania funkcji:")
    print("1 - f(x) = f1(x) + f2(x)")
    print("2 - f(x) = f1(x) * f2(x)")
    print("3 - f(x) = f2(f1(x))")
    print("4 - f(x) = f1(f2(x))")

    wybor_skladania = pobierz_liczbe_calkowita()

    if wybor_skladania == 1:
        return lambda x: f1(x) + f2(x)
    elif wybor_skladania == 2:
        return lambda x: f1(x) * f2(x)
    elif wybor_skladania == 3:
        return lambda x: f2(f1(x))
    elif wybor_skladania == 4:
        return lambda x: f1(f2(x))
    else:
        print("Niepoprawny wybór, domyślnie dodajemy funkcje.")
        return lambda x: f1(x) + f2(x)