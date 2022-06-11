import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(1,21)
y = 1/x

plt.plot(x,y, label="f(x) = 1/x")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(1, len(x))
plt.ylim(0, 1)
plt.show()