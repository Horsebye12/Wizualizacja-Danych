import numpy as np

print("Znajdź w wykreślance następujące słowa: numpy, nawyk, basen")

word = 'numpyaekjuwrscxyuraekikgb'
mat = np.array(list(word))
mat2 = mat.reshape(5, 5)

print(mat2)
