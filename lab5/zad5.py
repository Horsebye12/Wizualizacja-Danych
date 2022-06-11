import numpy as np

x = np.random.random((2, 3))
a = np.zeros((2, 3))

print(x)

for i in range(2):
    for y in range(3):
        a[i][y] = np.sin(x[i][y])


print(a)
