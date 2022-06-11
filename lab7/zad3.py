import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(1, 30, step=0.01)
sinus = np.sin(x)
cosinus = np.cos(x)

plt.plot(x, sinus, color="r", linestyle="dotted", label="f(x) = sin(x)")
plt.plot(x, cosinus, color="b", linestyle="solid", label="f(x) = cos(x)")
plt.legend()
plt.xlabel("oś x")
plt.ylabel("oś y")
plt.ylim(-2, 2)
plt.xlim(1, 30)
plt.title("Wykresy funkcji sin(x) oraz cos(x)")
plt.show()