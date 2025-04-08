def wypisz_rozwiazanie(status, rozw=None):
    print(status)
    if rozw is not None:
        for i, val in enumerate(rozw, start=1):
            print(f"x{i} = {val}")