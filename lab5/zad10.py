import numpy as np

a = np.ones((9, 9))

print(a.reshape(1, 81))
print(a.reshape(81, 1))
print(a.reshape(9, 3, 3))
print(a.reshape(3, 9, 3))
print(a.reshape(3, 3, 9))

#mamy ograniczoną liczbę opcji ponieważ ilość elementów tablicy na której dokonujemy ".reshape()" musi być równa
#ilości elementów tablicy oryginalnej