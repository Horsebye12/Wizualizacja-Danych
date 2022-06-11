import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(1,20)
y = 1/x

plt.plot(x,y, label="f(x) = 1/x", linestyle="dashed", color="g", marker=">")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(0, len(x)+1)
plt.ylim(0, 1)
plt.title("Wykres funkcji f(x) dla x [1, 20]")
plt.show()