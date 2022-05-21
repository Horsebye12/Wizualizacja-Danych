import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

x = np.arange(1, 20.2)
y = 1/x
plt.plot(x, y, 'ro:', label='f(x) = 1/x')
plt.legend(loc='upper right')
plt.title('Wykres funkcji homograficznej w I ćwiartce')
plt.xlabel("oś x", color='red')
plt.ylabel('oś y', color='red')
plt.tick_params('x', color='red')
plt.tick_params('y', color='red')
plt.show()

x2 = np.arange(0, 10.2, 0.1)
y2 = np.sin(x2)
plt.plot(x2, y2, 'b.--', label='f(x) = sin(x)')
plt.title("Wykres funkcji sinus")
plt.legend(loc='lower left')
plt.xlabel("oś x", color='blue')
plt.ylabel('oś y', color='blue')
plt.tick_params('x', color='blue')
plt.tick_params('y', color='blue')
plt.show()
