import numpy as np
from math import exp, sqrt, pi
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

# Funkcja wagowa dla Simpsona
def weight(x): return np.exp((-x) * x)


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


# Całkowanie od -∞ do +∞ za pomocą Simpsona
def simpson_infinite(f, eps, delta=5.0):
    total = 0
    a = 0
    continue_loop = True

    while continue_loop:
        area = simpson_adaptive(f, a, a + delta, eps)
        total += area
        continue_loop = abs(area) >= eps
        a += delta

    a = 0
    continue_loop = True

    while continue_loop:
        area = simpson_adaptive(f, -a - delta, -a, eps)
        total += area
        continue_loop = abs(area) >= eps
        a += delta

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

    print("\nObliczanie całki za pomocą kwadratury Simpsona (z wagą)...")
    simpson_result = simpson_infinite(lambda x: f(x) * weight(x), eps)
    print(f"Wynik kwadratury Simpsona: {simpson_result}")

    for n in [2, 3, 4, 5]:
        gh_result = gauss_hermite_quadrature(f, n)
        print(f"Wynik Gauss-Hermite (n={n}): {gh_result}")


if __name__ == "__main__":
    main()