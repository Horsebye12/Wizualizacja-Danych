import numpy as np

def macierz(n):
    a = np.arange(n*n)
    b = a.reshape(n, n)

    print(b)


n = input("Podaj wymiar boku macierzy: ")

print(macierz(int(n)))
