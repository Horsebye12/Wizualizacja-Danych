import numpy as np

a = np.ones((2,2))
b = np.ones((2,2))
c = a + b #działania na tablicach i macierzach można wykonywać tylko na zmiennych tego samego typu
print(c)

d = c - b
print(d)

e = np.arange(10)

s = slice(2, 7, 2) #wybór elementów z tabeli, od którego do którego(ten element zostanie pominięty) oraz krok(indeksy)
print(e[s])

s2 = range(2, 7, 2)
print(e[s2]) #podobne do slice
print(e[2:7:2]) #podobne do slice
print(e[1:]) #od którego indesku wyświetlać do końca

f = np.arange(25)
mat = f.reshape(5,5) #zamiana tablicy jednowymiarowej na dwuwymiarową
# (iloczyn kolumn i wierszy ma dać ilość elementów tablicy jednowymiarowej)
print(mat)
print(mat[1:2]) #wyświetla drugi wiersz macierzy

print(mat[1:, 0:5]) #wyświetla od drugiego wiersza do końca
print(mat[:, 1:2]) #wycina kolumnę z macierzy "1:2" ustawia w kolumnę
print(mat[2:5, 1:3]) #wycina wiersze od 2 do 4 i kolumny od 1 do 2

g = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) #wycinanie macierzy za pomocą tablic pomocniczych
print(g)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
h = g[rows, cols]
print(h)