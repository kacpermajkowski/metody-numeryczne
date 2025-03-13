import math

from zadanie_1.funkcje_poboru_danych import pobierz_liczbe_calkowita, pobierz_liczbe_rzeczywista, \
    pobierz_wspolczynniki_wielomianu, pobierz_liczby_rzeczywiste
from zadanie_1.funkcje_pomocnicze import oblicz_wartosc_wielomianu

#Funkcje

def pobierz_funkcje_wielomianowa():
    wspolczynniki = pobierz_wspolczynniki_wielomianu()
    return lambda x: oblicz_wartosc_wielomianu(x, wspolczynniki)

def pobierz_funkcje_trygonometryczna():
    print("Podaj współczynniki dla funkcji trygonometrycznej: f(x) = a * sin(bx + c) + d")
    a, b, c, d = pobierz_liczby_rzeczywiste(4)
    return lambda x: a * math.sin(b * x + c) + d

def pobierz_funkcje_wykladnicza():
    print("Podaj współczynniki dla funkcji wykładniczej: f(x) = a * e^(bx) + c")
    a, b, c = pobierz_liczby_rzeczywiste(3)
    return lambda x: a * math.exp(b * x) + c

