import numpy as np
import matplotlib.pyplot as plt

from funkcje_pomocnicze import oblicz_wartosc_wielomianu

def funkcja_liniowa(x):
    return 2*x + 3

def funkcja_bezwzgledna(x):
    return np.abs(x)

def funkcja_wielomian(x):
    # np. x^3 - 4x + 1
    return x * x * x - 4*x + 1

def funkcja_trygonometryczna(x):
    return np.sin(x)

def funkcja_zlozona(x):
    return np.sin(x * x)

def lagrange_coefficients(wezly_x, wezly_y):
    n = len(wezly_x)
    coefficients = np.zeros(n)
    for i in range(n):
        basis_coeff = np.poly1d([1])
        for j in range(n):
            if i != j:
                basis_coeff *= np.poly1d([1, -wezly_x[j]]) / (wezly_x[i] - wezly_x[j])
        coefficients += wezly_y[i] * basis_coeff.coeffs
    return coefficients
#wczytujemy wspolrzedne x a program obliczy y
def wczytaj_wezly_z_pliku(nazwa_pliku, funkcja):
    wezly_x = []
    try:
        with open(nazwa_pliku, 'r') as plik:
            for linia in plik:
                x = float(linia.strip())
                wezly_x.append(x)
    except FileNotFoundError:
        print(f"Plik {nazwa_pliku} nie został znaleziony.")
        exit(1)
    except ValueError:
        print("Błąd w formacie pliku. Upewnij się, że każda linia zawiera jedną liczbę.")
        exit(1)
    wezly_x = np.array(wezly_x)
    wezly_y = funkcja(wezly_x)
    return wezly_x, wezly_y

def wczytaj_wezly_reczne(funkcja):
    print("Podaj liczbę węzłów:")
    n = int(input())
    wezly_x = []
    print("Podaj węzły x (każdy węzeł w nowej linii):")
    for _ in range(n):
        x = float(input().strip())
        wezly_x.append(x)
    wezly_x = np.array(wezly_x)
    wezly_y = funkcja(wezly_x)
    return wezly_x, wezly_y

def wybierz_funkcje():
    print("Wybierz funkcję:")
    print("1. Liniowa (2x + 3)")
    print("2. Bezwzględna (|x|)")
    print("3. Wielomian (x^3 - 4x + 1)")
    print("4. Trygonometryczna (sin(x))")
    print("5. Złożona (sin(x^2))")
    wybor = int(input("Twój wybór: "))
    if wybor == 1:
        return funkcja_liniowa
    elif wybor == 2:
        return funkcja_bezwzgledna
    elif wybor == 3:
        return funkcja_wielomian
    elif wybor == 4:
        return funkcja_trygonometryczna
    elif wybor == 5:
        return funkcja_zlozona
    else:
        print("Nieprawidłowy wybór. Domyślnie funkcja liniowa.")
        return funkcja_liniowa

def wezly_rownoodlegle(a, b, n):
    return np.linspace(a, b, n)

def lagrange_interpolacja(x, wezly_x, wezly_y):
    n = len(wezly_x)
    wynik = 0.0
    for i in range(n):
        iloczyn = wezly_y[i]
        for j in range(n):
            if i != j:
                iloczyn *= (x - wezly_x[j]) / (wezly_x[i] - wezly_x[j])
        wynik += iloczyn
    return wynik

def main():
    print("Wybierz sposób wprowadzenia węzłów:")
    print("1. Wczytaj węzły z pliku")
    print("2. Wygeneruj węzły równoodległe")
    print("3. Wprowadź węzły ręcznie (nierówne odstępy)")
    wybor = int(input("Twój wybór: ").strip())

    if wybor == 1:
        funkcja = wybierz_funkcje()
        nazwa_pliku = input("Podaj nazwę pliku: ").strip()
        wezly_x, wezly_y = wczytaj_wezly_z_pliku(nazwa_pliku, funkcja)
        a, b = wezly_x[0], wezly_x[-1]
    elif wybor == 2:
        funkcja = wybierz_funkcje()
        a = float(input("Podaj początek przedziału a: "))
        b = float(input("Podaj koniec przedziału b: "))
        n = int(input("Podaj liczbę węzłów interpolacji: "))
        wezly_x = wezly_rownoodlegle(a, b, n)
        wezly_y = funkcja(wezly_x)
    elif wybor == 3:
        funkcja = wybierz_funkcje()
        wezly_x, wezly_y = wczytaj_wezly_reczne(funkcja)
        a, b = wezly_x[0], wezly_x[-1]
    else:
        print("Nieprawidłowy wybór.")
        return

    coefficients = lagrange_coefficients(wezly_x, wezly_y)

    x_rysuj = np.linspace(a, b, 1000)
    lagrange_rysuj = np.array([oblicz_wartosc_wielomianu(x, coefficients) for x in x_rysuj])

    # Rysowanie wykresów
    plt.figure(figsize=(10, 6))
    if wybor == 2:
        f_rysuj = funkcja(x_rysuj)
        plt.plot(x_rysuj, f_rysuj, label="Funkcja oryginalna", color='blue')
    plt.plot(x_rysuj, lagrange_rysuj, label="Wielomian interpolacyjny", color='red', linestyle='--')
    plt.plot(wezly_x, wezly_y, 'go', label="Węzły interpolacji")  # zielone punkty
    plt.title("Interpolacja Lagrange'a z obsługą nierównych odstępów")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
