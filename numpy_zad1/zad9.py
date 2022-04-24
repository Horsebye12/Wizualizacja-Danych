import numpy as np

fib = [0, 1]
n = 2

while n < 25:
    temp_fib = fib[n - 1] + fib[n - 2]
    fib.append(temp_fib)
    n += 1


fib2 = np.array(list(fib))
fib3 = fib2.reshape(5, 5)

print(fib3)
