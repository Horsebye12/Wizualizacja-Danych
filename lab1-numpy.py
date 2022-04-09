import numpy as np

marcin = b'Marcin'
mar = np.frombuffer(marcin, dtype='S1') #tworzy tablicę z bufora,
# dtype określa ile elementów pobiera z bufora do jednego elementu
print(mar)

marcin2 = 'Marcin'
mar_1 = np.array(list(marcin2)) #tworzenie tablicy z łańcucha znakowego
print(mar_1)
mar_2 = np.array(list(marcin2), dtype='S1') #tworzenie tablicy z łańcucha znakowego dodaje bufor
print(mar_2)

mar_3 = np.array(list(marcin)) #przekazuje kody ASCII znaków z b'Łańcuch'
print(mar_3)

mar_4 = np.fromiter(marcin2, dtype="U1")
print(mar_4)



