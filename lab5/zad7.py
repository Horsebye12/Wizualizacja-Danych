import numpy as np

x = np.random.random((2, 3))
a = np.zeros((2, 3))

for i in range(2):
    for y in range(3):
        a[i][y] = np.sin(x[i][y])

z = np.random.random((2, 3))
b = np.zeros((2, 3))


for i in range(2):
    for y in range(3):
        b[i][y] = np.cos(z[i][y])


suma = a + b
print(suma)
