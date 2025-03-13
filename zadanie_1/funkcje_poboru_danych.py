
menuWyboruFunkcji = [
    "Wybierz funkcję:",
    "1 - Wielomianowa",
    "2 - Trygonometryczna",
    "3 - Wykładnicza",
    "4 - Złożenie funkcji"
]

def wybierz_warunek_stopu():
    print("Wybierz warunek stopu:")
    print("1 - Dokładność epsilon")
    print("2 - Maksymalna liczba iteracji")

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


def wybor_funkcji():
    from zadanie_1.definicje_funkcji import \
        funkcja_wielomianowa, \
        funkcja_trygonometryczna, \
        funkcja_wykladnicza, \
        skladana_funkcja

    funkcja = None
    while funkcja is None:
        drukujListeString(menuWyboruFunkcji)
        wybor = pobierz_liczbe_calkowita()


        funkcje = {
            1: funkcja_wielomianowa(),
            2: funkcja_trygonometryczna(),
            3: funkcja_wykladnicza(),
            4: skladana_funkcja()
        }
        funkcja = funkcje[wybor]
        if(funkcja is None):
            print("Niepoprawny wybór, spróbuj ponownie.")
    return funkcja

def pobierz_przedzial_poszukiwan():
    print("Podaj przedział poszukiwań:")
    a, b = None, None
    while a is None or b is None or a >= b:
        a, b = pobierz_liczbe_rzeczywista(), pobierz_liczbe_rzeczywista()
        if a >= b:
            print("Lewy przedział musi być mniejszy od prawego!")
        if a is None or b is None:
            print("Oba krańce przedziału muszą być zdefiniowane")
    return a, b

def pobierz_liczbe_iteracji():
    liczbaIteracji = None
    while liczbaIteracji is None or liczbaIteracji <= 0:
        liczbaIteracji = pobierz_liczbe_calkowita()
        if liczbaIteracji <= 0:
            print("Liczba iteracji musi być większa od zera.")
    return liczbaIteracji


def epsilon():
    wartoscE = None
    while wartoscE is None or wartoscE <= 0:
        wartoscE = pobierz_liczbe_rzeczywista()
        if wartoscE <= 0:
            print("Epsilon musi być większy od zera.")
    return wartoscE

def drukujListeString(stringList):
    for string in stringList:
        print(string)
