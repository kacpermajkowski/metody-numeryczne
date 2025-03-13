def bisekcja(funkcja, przedzial_poszukiwan, warunekStop, wartoscStop):
    a, b = przedzial_poszukiwan
    if funkcja(a) * funkcja(b) >= 0:
        print("Funkcja nie spełnia warunku zmiany znaku na krańcach przedziału.")
        return None

    iteracje = 0
    while True:
        c = (a + b) / 2
        iteracje += 1
        if warunekStop == 1 and abs(funkcja(c)) < wartoscStop:
            print(f"Przybliżenie Bieskcja wykonane zostalo po {iteracje} iteracjach ")
            return c
        if warunekStop == 2 and iteracje >= wartoscStop:
            print(f"Przybliżenie Bieskcja wykonane zostalo po {iteracje} iteracjach ")
            return c
        if funkcja(a) * funkcja(c) < 0:
            b = c
        else:
            a = c

def falsi(funkcja, przedzialPoszukiwan, warunekStop, wartoscStop):
    a, b = przedzialPoszukiwan
    if funkcja(a) * funkcja(b) >= 0:
        print("Funkcja nie spełnia warunku zmiany znaku na krańcach przedziału.")
        return None

    iteracje = 0
    while True:
        c = b - (funkcja(b) * (a - b)) / (funkcja(a) - funkcja(b))
        if warunekStop == 1 and abs(funkcja(c)) < wartoscStop:
            print(f"Przybliżenie Falsi wykonane zostalo po {iteracje} iteracjach ")
            return c
        if warunekStop == 2 and iteracje >= wartoscStop:
            print(f"Przybliżenie Falsi wykonane zostalo po {iteracje} iteracjach ")
            return c
        if funkcja(a) * funkcja(c) < 0:
            b = c
        else:
            a = c
