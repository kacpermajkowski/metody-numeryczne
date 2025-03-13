import math
import time
import matplotlib.pyplot as plt
import numpy as np

# def power(base, exp):
#    result = 1
#    for _ in range(abs(exp)):
#        result *= base
#    return result if exp >= 0 else 1 / result

#def power2(base, exp):
#    result = math.e

#Sprawdzanie liczb

def czyLiczbaCal():
    liczba = None
    while liczba is None:
        try:
            liczba = int(input("Podaj liczbę całkowitą: "))
        except ValueError:
            print("To nie jest liczba całkowita, spróbuj ponownie.")
    return liczba


def czyLiczbaDouble():
    liczba = None
    while liczba is None:
        try:
            liczba = float(input("Podaj liczbę rzeczywistą: "))
        except ValueError:
            print("To nie jest liczba rzeczywista, spróbuj ponownie.")
    return liczba



def iteracja():
    liczbaIteracji = None
    while liczbaIteracji is None or liczbaIteracji <= 0:
        liczbaIteracji = czyLiczbaCal()
        if liczbaIteracji <= 0:
            print("Liczba iteracji musi być większa od zera.")
    return liczbaIteracji


def epsilon():
    wartoscE = None
    while wartoscE is None or wartoscE <= 0:
        wartoscE = czyLiczbaDouble()
        if wartoscE <= 0:
            print("Epsilon musi być większy od zera.")
    return wartoscE

#Do funkcji wielomianowej

def horner(x, wspolczynniki, n):
    wynik = wspolczynniki[0]
    for i in range(1, n):
        wynik = wynik * x + wspolczynniki[i]
    return wynik

#warunek stopu

def wybierz_warunek_stopu():
    print("Wybierz warunek stopu:")
    print("1 - Dokładność epsilon")
    print("2 - Maksymalna liczba iteracji")

    wybor = None
    while wybor not in [1, 2]:
        wybor = czyLiczbaCal()
        if wybor not in [1, 2]:
            print("Niepoprawny wybór, spróbuj ponownie.")

    if wybor == 1:
        wartosc = epsilon()
    else:
        wartosc = iteracja()

    return wybor, wartosc

#Funkcje

def funkcjaWielomianowa():
    print("Podaj stopień wielomianu: ")
    stopien = czyLiczbaCal()
    wspolczynniki = []
    for i in range(stopien + 1):
        print(f"Podaj współczynnik przy x^{stopien - i}: ")
        wspolczynniki.append(czyLiczbaDouble())
    return lambda x: horner(x, wspolczynniki, stopien + 1)

def funkcjaTrygonometryczna():
    print("Podaj współczynniki dla funkcji trygonometrycznej: f(x) = a * sin(bx + c) + d")
    a, b, c, d = czyLiczbaDouble(), czyLiczbaDouble(), czyLiczbaDouble(), czyLiczbaDouble()
    return lambda x: a * math.sin(b * x + c) + d


def funkcjaWykladnicza():
    print("Podaj współczynniki dla funkcji wykładniczej: f(x) = a * e^(bx) + c")
    a, b, c = czyLiczbaDouble(), czyLiczbaDouble(), czyLiczbaDouble()
    return lambda x: a * math.exp(b * x) + c

def skladanaFunkcja():
    print("Wybierz dwie funkcje do składania:")
    print("1 - Wielomianowa")
    print("2 - Trygonometryczna")
    print("3 - Wykładnicza")

    wybor1 = None
    wybor2 = None

    while wybor1 == wybor2:
        wybor1 = czyLiczbaCal()
        wybor2 = czyLiczbaCal()
        if wybor1 == wybor2:
            print("Musisz wybrać dwie różne funkcje!")

    funkcje = {
        1: funkcjaWielomianowa,
        2: funkcjaTrygonometryczna,
        3: funkcjaWykladnicza
    }

    f1 = funkcje[wybor1]()
    f2 = funkcje[wybor2]()

    print("Wybierz sposób składania funkcji:")
    print("1 - f(x) = f1(x) + f2(x)")
    print("2 - f(x) = f1(x) * f2(x)")
    print("3 - f(x) = f2(f1(x))")
    print("4 - f(x) = f1(f2(x))")

    wybor_skladania = czyLiczbaCal()

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

#Metody przybizania miejsca zerowego

def Bisekcja(funkcja, a, b, warunekStop, wartoscStop):
    startTime = time.time()
    if funkcja(a) * funkcja(b) >= 0:
        print("Funkcja nie spełnia warunku zmiany znaku na krańcach przedziału.")
        return None

    iteracje = 0
    while True:
        c = (a + b) / 2
        iteracje += 1
        if warunekStop == 1 and abs(funkcja(c)) < wartoscStop:
            endTime = time.time()
            print(f"Przybliżenie Bieskcja wykonane zostalo po {iteracje} iteracjach "
                  f"oraz po {endTime - startTime:.6f} sekundach")
            return c
        if warunekStop == 2 and iteracje >= wartoscStop:
            endTime = time.time()
            print(f"Przybliżenie Bieskcja wykonane zostalo po {iteracje} iteracjach "
                  f"oraz po {endTime-startTime:.6f} sekundach")
            return c
        if funkcja(a) * funkcja(c) < 0:
            b = c
        else:
            a = c

def Falsi(funkcja, a, b, warunekStop, wartoscStop):
    startTime = time.time()
    if funkcja(a) * funkcja(b) >= 0:
        print("Funkcja nie spełnia warunku zmiany znaku na krańcach przedziału.")
        return None

    iteracje = 0
    while True:
        c = b - (funkcja(b) * (a - b)) / (funkcja(a) - funkcja(b))
        if warunekStop == 1 and abs(funkcja(c)) < wartoscStop:
            endTime = time.time()
            print(f"Przybliżenie Falsi wykonane zostalo po {iteracje} iteracjach "
                  f"oraz po {endTime - startTime:.6f} sekundach")
            return c
        if warunekStop == 2 and iteracje >= wartoscStop:
            endTime = time.time()
            print(f"Przybliżenie Falsi wykonane zostalo po {iteracje} iteracjach "
                  f"oraz po {endTime - startTime:.6f} sekundach")
            return c
        if funkcja(a) * funkcja(c) < 0:
            b = c
        else:
            a = c

#Rysowanie wykresu

def rysujWykres(funkcja, a, b, wynik):
    x = np.linspace(a, b, 400)
    y = np.array([funkcja(xi) for xi in x])
    plt.plot(x, y, label="Funkcja")
    if wynik is not None:
        plt.scatter(wynik, 0, color='red', label=f'Miejsce zerowe: {wynik:.4f}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title("Wykres funkcji")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    funkcja = None
    while funkcja is None:
        print("Wybierz funkcję:")
        print("1 - Wielomianowa")
        print("2 - Trygonometryczna")
        print("3 - Wykładnicza")
        print("4 - Złożenie funkcji")
        wybor = czyLiczbaCal()
        if wybor == 1:
            funkcja = funkcjaWielomianowa()
        elif wybor == 2:
            funkcja = funkcjaTrygonometryczna()
        elif wybor == 3:
            funkcja = funkcjaWykladnicza()
        elif wybor == 4:
            funkcja = skladanaFunkcja()
        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

    print("Podaj przedział poszukiwań:")
    a, b = None, None
    while a is None or b is None or a >= b:
        a, b = czyLiczbaDouble(), czyLiczbaDouble()
        if a >= b:
            print("Lewy przedział musi być mniejszy od prawego!")

    wyborStop, wartoscStop = wybierz_warunek_stopu()

    wynikBisekcja = Bisekcja(funkcja, a, b, wyborStop, wartoscStop)
    wynikFalsi = Falsi(funkcja, a, b, wyborStop, wartoscStop)

    print(f"Bisekcja: {wynikBisekcja}")
    print(f"Reguła Falsi: {wynikFalsi}")


    rysujWykres(funkcja, a, b, wynikBisekcja)
    rysujWykres(funkcja, a, b, wynikFalsi)


if __name__ == "__main__":
    main()