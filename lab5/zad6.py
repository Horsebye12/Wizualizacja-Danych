import numpy as np

x = np.random.random((2, 3))
b = np.zeros((2, 3))

print(x)

for i in range(2):
    for y in range(3):
        b[i][y] = np.cos(x[i][y])


print(a)