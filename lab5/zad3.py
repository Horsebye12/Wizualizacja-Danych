import numpy as np

a = np.arange(1, 4).reshape(3, 1)
b = np.arange(6, 9).reshape(3, 1)

c = a / b
print(c)
