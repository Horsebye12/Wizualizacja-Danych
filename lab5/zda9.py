import numpy as np

a = np.random.random((3, 3))

for x in range(9):
    print(a.flat[x])

