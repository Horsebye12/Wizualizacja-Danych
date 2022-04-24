import numpy as np

n = int(input("Podaj wymiar macierzy: "))


def macierz(n):
    mat = np.eye(n) * 2

    for x in range(1, n):
        mat = mat + (np.eye(n, k=0 - x) * (2 * (x + 1))) + (np.eye(n, k=0 + x) * (2 * (x + 1)))

    return mat


print(macierz(n))
