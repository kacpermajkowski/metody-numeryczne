import math

from zadanie_1.funkcje_poboru_danych import pobierz_liczbe_calkowita, epsilon, pobierz_liczbe_rzeczywista
from zadanie_1.funkcje_pomocnicze import horner

#Funkcje

def funkcja_wielomianowa():
    print("Podaj stopień wielomianu: ")
    stopien = pobierz_liczbe_calkowita()
    wspolczynniki = []
    for i in range(stopien + 1):
        print(f"Podaj współczynnik przy x^{stopien - i}: ")
        wspolczynniki.append(pobierz_liczbe_rzeczywista())
    return lambda x: horner(x, wspolczynniki)

def funkcja_trygonometryczna():
    print("Podaj współczynniki dla funkcji trygonometrycznej: f(x) = a * sin(bx + c) + d")
    a, b, c, d = pobierz_liczbe_rzeczywista(), pobierz_liczbe_rzeczywista(), pobierz_liczbe_rzeczywista(), pobierz_liczbe_rzeczywista()
    return lambda x: a * math.sin(b * x + c) + d


def funkcja_wykladnicza():
    print("Podaj współczynniki dla funkcji wykładniczej: f(x) = a * e^(bx) + c")
    a, b, c = pobierz_liczbe_rzeczywista(), pobierz_liczbe_rzeczywista(), pobierz_liczbe_rzeczywista()
    return lambda x: a * math.exp(b * x) + c

def skladana_funkcja():
    print("Wybierz dwie funkcje do składania:")
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
        1: funkcja_wielomianowa,
        2: funkcja_trygonometryczna,
        3: funkcja_wykladnicza
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
