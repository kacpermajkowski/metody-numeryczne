#Rysowanie wykresu
import numpy as np
from matplotlib import pyplot as plt

def rysuj_wykres(funkcja, przedzial, miejsce_zerowe):
    a, b = przedzial
    x = np.linspace(a, b, 400)
    y = np.array([funkcja(xi) for xi in x])
    plt.plot(x, y, label="Funkcja")
    if miejsce_zerowe is not None:
        plt.scatter(miejsce_zerowe, 0, color='red', label=f'Miejsce zerowe: {miejsce_zerowe:.4f}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title("Wykres funkcji")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()