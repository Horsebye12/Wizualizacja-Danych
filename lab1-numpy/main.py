import numpy as np

a = np.array([0, 1]) #tablica
print(a)

b = np.arange(1, 5, 1) #tablica range
print(b)

print(type(a))
print(b.dtype) #typ elementów tablicy

c = b.astype('float64') #zapisz elementy jako inny typ
print(c.dtype)

print(c.shape) #ilość elementów przy jednowymiarowej, wiersze i kolumny przy dwuwymiarowej

d = np.array([np.arange(2), np.arange(2)]) #tablica dwuwymiarowa
print(d)
print(d.shape)
print(d.ndim) #ilość wymiarów tablicy

zera = np.zeros((5, 5)) #tablica dwuwymiarowa z samymi zerami
print(zera)

jedynka = np.ones((5,5)) #tablica dwuwymiarowa z samymi jedynkami
print(jedynka)

pusta = np.empty((2,2)) #pusta tablica dwuwymiarowa, zostanie wypełniona losowymi elementami
print(pusta)

print(pusta[1][1]) #odniesienie do elementu 1 wiersza i 1 kolumny, zaczyna się od zera

a = np.arange(1, 5, 0.5) #arange można ustawić krok o wartości zmiennoprzecinkowej
print(a)

b = np.linspace(1, 2, 5, endpoint=False) #tworzy tablice z liczb z  przedziału 1 do 2, 5 elementową, krok ustala sama,
# endpoint usuwa ostanią możliwą wartość czyli 2
print(b)

c, d = np.indices((5, 5)) #tworzenie dwoch macierzy, pierwsza ustawia wartości w kolumnach a druga w wierszach
print(c)
print(d)

e = np.indices((3,3)) #tworzenie tablicy trójwymiarowej
print(e)
print(e[0][1][1]) #odniesienie do elementu tablicy trójwymiarowej, [nr macierzy][nr wiersza][nr kolumny]

f, g = np.mgrid[0:5, 0:5] #tworzenie macierzy o wartościach od 0 do 5, podobne do indices
print(f)
print(g)

h = np.diag([a for a in range(5)], -1) #tworzy macierz diagonalną ustalając macierz używając przekątnej macierzy,
# wartości wektora po przecinku ustalają przesunięcie przekątnej (dodatnie w górę, ujemne w prawo)
print(h)

i = np.fromiter(range(5), dtype='int32') #tworzy tablicę z obiektu iterowanego po podaniu zakresu i typu
print(i)



