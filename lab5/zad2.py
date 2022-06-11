import numpy as np

a = np.random.random((3, 3))
b = np.random.random((4, 4))

print(a)
print("Najmniejsze wartosci macierzy 3x3 - wiersze: ", a.min(axis=1))
print("Najmniejsze wartosci macierzy 3x3 - kolumny: ", a.min(axis=0))
print("\n", b)
print("Najmniejsze wartosci macierzy 4x4 - wiersze: ", a.min(axis=1))
print("Najmniejsze wartosci macierzy 4x4 - kolumny: ", a.min(axis=0))
