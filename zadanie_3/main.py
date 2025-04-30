import numpy as np
import matplotlib.pyplot as plt
import sys

from funkcje_pomocnicze import oblicz_wartosc_wielomianu

def get_function():
    print("Wybierz rodzaj funkcji (wpisz numer):")
    print(" 1: funkcja liniowa (np. f(x) = 2*x + 1)")
    print(" 2: wartość bezwzględna (f(x) = |x|)")
    print(" 3: wielomian (np. f(x) = x^3 - 4*x + 1)")
    print(" 4: funkcja trygonometryczna (1: sin(x), 2: cos(x), 3: sin(x)+cos(x))")
    print(" 5: złożenie (1: sin(|x|), 2: x*cos(x))")
    try:
        choice = int(input("Twój wybór: "))
    except ValueError:
        print("Nieprawidłowy wybór. Domyślnie wybieram funkcję liniową.")
        choice = 1

    if choice == 1:
        f = lambda x: 2*x + 1
        func_name = "2*x+1"
        file_func_name = "liniowa"
    elif choice == 2:
        f = lambda x: np.abs(x)
        func_name = "abs(x)"
        file_func_name = "bezwzgledna"
    elif choice == 3:
        coefficients = np.array([3, 0, -4, 1], dtype=float)
        f = lambda x: oblicz_wartosc_wielomianu(x, coefficients)
        # f = lambda x: x**3 - 4*x + 1
        func_name = "x^3-4*x+1"
        file_func_name = "wielomian"
    elif choice == 4:
        print("Wybierz typ funkcji trygonometrycznej:")
        print(" 1: sin(x)")
        print(" 2: cos(x)")
        print(" 3: sin(x) + cos(x)")
        try:
            t = int(input("Twój wybór: "))
        except ValueError:
            t = 1
        if t == 2:
            f = lambda x: np.cos(x)
            func_name = "cos(x)"
            file_func_name = "cosinus"
        elif t == 3:
            f = lambda x: np.sin(x) + np.cos(x)
            func_name = "sin(x)+cos(x)"
            file_func_name = "sinus_cosinus"
        else:
            f = lambda x: np.sin(x)
            func_name = "sin(x)"
            file_func_name = "sinus"
    elif choice == 5:
        print("Wybierz funkcję złożoną:")
        print(" 1: sin(|x|)")
        print(" 2: x * cos(x)")
        try:
            t = int(input("Twój wybór: "))
        except ValueError:
            t = 1
        if t == 2:
            f = lambda x: x * np.cos(x)
            func_name = "x*cos(x)"
            file_func_name = "x_cosinus"
        else:
            f = lambda x: np.sin(np.abs(x))
            func_name = "sin(|x|)"
            file_func_name = "sin_bezwzgledna"
    else:
        print("Nieprawidłowy wybór. Domyślnie wybieram funkcję liniową.")
        f = lambda x: 2*x + 1
        func_name = "2*x+1"
        file_func_name = "liniowa"
    return f, func_name, file_func_name

def lagrange_interpolation(x_nodes, y_nodes, x):
    """
    Oblicza wartość wielomianu interpolacyjnego Lagrange'a P(x) w punktach x.
    Parametry:
      x_nodes, y_nodes – węzły interpolacji i wartości funkcji w tych węzłach
      x – punkt lub tablica punktów, w których liczymy P(x).
    Zwraca wartości P(x) (jako tablicę numpy).
    """
    x = np.array(x, dtype=float)
    x_nodes = np.array(x_nodes, dtype=float)
    y_nodes = np.array(y_nodes, dtype=float)
    n = len(x_nodes)
    P = np.zeros_like(x, dtype=float)
    # Suma wielomianów bazowych L_i(x) pomnożonych przez y_i
    for i in range(n):
        L_i = np.ones_like(x, dtype=float)
        for j in range(n):
            if j != i:
                L_i *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        P += y_nodes[i] * L_i
    return P

import numpy as np

def get_from_file():
    print("Czy chcesz wczytać węzły z pliku? (t/n)")
    choice = input().strip().lower()
    x_nodes = []
    y_nodes = []
    if choice == 't':
        filename = "test.txt"
        try:
            with open(filename, 'r') as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) != 2:
                        raise ValueError("Nieprawidłowy format pliku. Każda linia powinna zawierać dokładnie dwie liczby oddzielone spacją.")
                    x, y = map(float, parts)
                    x_nodes.append(x)
                    y_nodes.append(y)
            x_nodes = np.array(x_nodes)
            y_nodes = np.array(y_nodes)
        except FileNotFoundError:
            print(f"Nie znaleziono pliku {filename}. Program przerwany.")
            exit(-1)
        except ValueError as e:
            print(f"Błąd formatu pliku: {e}. Program przerwany.")
            exit(-1)
        is_from_file = True
    else:
        x_nodes = None
        y_nodes = None
        is_from_file = False
    return is_from_file, x_nodes, y_nodes

def main():
    is_from_file, x_nodes, y_nodes = get_from_file()
    n = len(x_nodes)
    f, func_name, file_func_name = None, "punkty danych", "punkty_danych"
    if not is_from_file:
        f, func_name, file_func_name = get_function()

    num_dense = 500
    x_dense = []
    y_dense = []
    if is_from_file:
        x_dense = np.linspace(x_nodes[0], x_nodes[-1], num_dense)

    if not is_from_file:
        try:
            a = float(input("Podaj dolną granicę przedziału a: "))
            b = float(input("Podaj górną granicę przedziału b: "))
        except ValueError:
            print("Nieprawidłowy przedział. Używam domyślnie [0, 1].")
            a, b = 0.0, 1.0
        if a > b:
            print("Dolna granica większa od górnej. Zamieniam kolejność.")
            a, b = b, a

        try:
            n = int(input("Podaj liczbę węzłów interpolacyjnych (>=2): "))
        except ValueError:
            print("Nieprawidłowa liczba. Używam domyślnie n=2.")
            n = 2
        if n < 2:
            print("Liczba węzłów musi być >= 2. Ustawiam n=2.")
            n = 2

        x_nodes = np.linspace(a, b, n)
        y_nodes = f(x_nodes)

        x_dense = np.linspace(a, b, num_dense)
        y_dense = f(x_dense)

    y_interp = lagrange_interpolation(x_nodes, y_nodes, x_dense)

    y_at_nodes = lagrange_interpolation(x_nodes, y_nodes, x_nodes)
    error_nodes = np.max(np.abs(y_at_nodes - y_nodes))
    print(f"Maksymalny błąd w węzłach interpolacji: {error_nodes:.6e}")

    if not is_from_file:
        error_max = np.max(np.abs(y_interp - y_dense))
        print(f"Maksymalny błąd interpolacji na gęstej siatce: {error_max:.6e}")

    plt.figure(figsize=(8, 6))
    if not is_from_file:
        plt.plot(x_dense, y_dense, 'b', label="Funkcja oryginalna")
    plt.plot(x_dense, y_interp, 'r--', label="Wielomian interpolacyjny")
    plt.plot(x_nodes, y_nodes, 'ko', label="Węzły interpolacyjne")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Interpolacja Lagrange'a, f(x) = {func_name}, n = {n}")
    plt.legend()
    plt.grid(True)

    filename = f"lagrange_{file_func_name}_n{n}.png"
    plt.savefig(filename)
    print(f"Wykres zapisano do pliku '{filename}'")

if __name__ == "__main__":
    main()
