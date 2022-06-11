import numpy as np

a = np.random.randint(12, size=12)

b = a.reshape(3, 4)
c = a.reshape(4, 3)
d = a.reshape(2, 6)

print(b.flatten())
print(c.flatten())
print(d.flatten())

#wyniki są identyczne