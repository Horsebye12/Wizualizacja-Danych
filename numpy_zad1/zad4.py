import numpy as np

def potegi(a, b):
    tab = np.logspace(1, b, base=a, num=b)
    print(tab)


a = input("Podaj liczbę którą chcesz potęgować(Podstawę potęgi): ")
b = input("Podaj do której maksymalnej potęgi chcesz wykonywać działania(Wykładnik ostatniej potęgi): ")

potegi(int(a), int(b))