import numpy as np

a = np.arange(1, 4).reshape(1, 3)
b = np.arange(6, 9).reshape(1, 3)

c = a * b

print(c)
