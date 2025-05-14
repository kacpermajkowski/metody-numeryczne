import numpy as np
from math import exp, sqrt, pi
import matplotlib.pyplot as plt  # Add this import for plotting
from zadanie4.funkcje_pomocnicze import oblicz_wartosc_wielomianu

# Funkcje do wyboru
def f1(x):
    return oblicz_wartosc_wielomianu(x, [1, 0, 0])  # x^2

def f2(x):
    return oblicz_wartosc_wielomianu(x, [1, 0, -2, 1])  # x^4 - 2x^2 + 1

def f3(x):
    return np.sin(x) #sinus x

def f4(x):
    return np.exp((-x) * x) # wykladnicza -x^2

def f5(x):
    return 1 / (1 + x * x) # funkcja Lorentza - 1/(1+x^2)

# Weight function for Simpson's method
def weight_simpson(x):
    return 1  # Constant weight for Simpson's method

# Weight function for Gauss-Hermite quadrature
def weight_hermite(x):
    return np.exp(-x * x)

# Złożona kwadratura Simpsona z adaptacyjnym podziałem
def simpson_adaptive(f, a, b, eps):
    n = 2

    def simpson(f, a, b, n):
        h = (b - a) / n
        result = f(a) + f(b)
        for i in range(1, n, 2):
            result += 4 * f(a + i * h)
        for i in range(2, n - 1, 2):
            result += 2 * f(a + i * h)
        return result * h / 3

    prev = simpson(f, a, b, n)
    while True:
        n *= 2
        curr = simpson(f, a, b, n)
        if abs(curr - prev) < eps:
            return curr
        prev = curr


def simpson_infinite(f, eps, delta=5.0, max_iterations=1000):
    total = 0
    a = 0
    iterations = 0
    continue_loop = True

    # Positive direction
    while continue_loop and iterations < max_iterations:
        area = simpson_adaptive(f, a, a + delta, eps)
        total += area
        continue_loop = abs(area) >= eps
        a += delta
        iterations += 1

    # Reset for negative direction
    a = 0
    iterations = 0
    continue_loop = True

    # Negative direction
    while continue_loop and iterations < max_iterations:
        area = simpson_adaptive(f, -a - delta, -a, eps)
        total += area
        continue_loop = abs(area) >= eps
        a += delta
        iterations += 1

    return total


# Kwadratura Gaussa-Hermite'a
def gauss_hermite_quadrature(f, n):
    xi, wi = np.polynomial.hermite.hermgauss(n)  # Replacing scipy with numpy
    return sum(w * f(x) for x, w in zip(xi, wi))

def main():
    functions = [f1, f2, f3, f4, f5]
    print("Wybierz funkcję do całkowania:")
    for i, f in enumerate(functions, 1):
        print(f"{i}. f{i}(x)")
    choice = int(input("Numer funkcji: ")) - 1
    f = functions[choice]

    eps = float(input("Podaj dokładność dla Simpsona (np. 1e-6): "))

    # Input interval for Simpson's method
    try:
        a = float(input("Podaj dolną granicę przedziału a: "))
        b = float(input("Podaj górną granicę przedziału b: "))
    except ValueError:
        print("Nieprawidłowe wartości. Używam domyślnie przedziału [0, 1].")
        a, b = 0.0, 1.0

    print("\nObliczanie całki za pomocą kwadratury Simpsona na podanym przedziale...")
    simpson_result = simpson_adaptive(lambda x: f(x) * weight_simpson(x), a, b, eps)
    print(f"Wynik kwadratury Simpsona: {simpson_result}")

    print("\nObliczanie całki za pomocą kwadratury Gaussa-Hermite'a...")
    for n in [2, 3, 4, 5]:
        gh_result = gauss_hermite_quadrature(f, n)  # Pass f directly, without multiplying by weight_hermite
        print(f"Wynik Gauss-Hermite (n={n}): {gh_result}")

    # Plot the weight function for Gauss-Hermite
    x_vals = np.linspace(-5, 5, 500)
    y_vals = [weight_hermite(x) for x in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label="Funkcja wagowa $e^{-x^2}$", color="blue")
    plt.title("Wykres funkcji wagowej dla Gauss-Hermite")
    plt.xlabel("x")
    plt.ylabel("Waga")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Plot the selected function
    y_func_vals = [f(x) for x in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_func_vals, label=f"Wybrana funkcja f{choice + 1}(x)", color="green")
    plt.title(f"Wykres funkcji f{choice + 1}(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()