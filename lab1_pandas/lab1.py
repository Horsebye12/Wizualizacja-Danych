import numpy as np
import pandas as ps

a = np.arange(12).reshape(4,3)
print(a)
print(a.sum()) #suma elementów tablicy
print(a.sum(axis=0)) #suma elementów znajdująca się na określonej płaszczyźnie, pion, poziom
print(a.sum(axis=1))
print(a.cumsum(axis=0)) #suma kumulowana na pionie lub poziomie

b = np.array([20, 30, 40, 50])
c = np.arange(4)
d = c + b
print(d)
e = np.sqrt(c)
f = d + e
print(f)

g = np.array([[2, 5, 1], [5, 7, 1]])
h = np.array([[2, 3], [4, 5], [7, 1]])
i = np.dot(g, h) #mnożenie macierzy
j = g.dot(h) #to samo co wyżej
print(i)

k = np.arange(3)
l = np.arange(3)
print(np.dot(k, l)) #mnożenie, liczba wierszy i kolumn jednej listy musi być równa drugiej

m = np.arange(3)
n = np.array([[0], [1], [3]])
print(m.dot(n)) #mnożenie takich macierzy zmieni rozmiar na 1x1

o = np.arange(6).reshape((3, 2))
print(a)
for p in o.flat: #spłaszcza macierz do jednowymiarowej tablicy
    print(p)


r = o.reshape((2, 3))
print(r)





