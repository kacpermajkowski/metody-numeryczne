#Rysowanie wykresu
import numpy as np
from matplotlib import pyplot as plt

colors = {
    0: "red",
    1: "blue",
    2: "green",
    3: "yellow",
    4: "orange",
    5: "purple",
    6: "black",
    7: "pink",
    8: "brown",
    9: "gray"
}

def rysuj_wykres(funkcja, przedzial, miejsca_zerowe):
    a, b = przedzial
    x = np.linspace(a, b, 400)
    y = np.array([funkcja(xi) for xi in x])
    plt.plot(x, y, label="Funkcja")
    for i, x0 in enumerate(miejsca_zerowe):
        plt.scatter(x0, 0, color=colors[i], label=f'Miejsce zerowe: {x0:.4f}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title("Wykres funkcji")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()