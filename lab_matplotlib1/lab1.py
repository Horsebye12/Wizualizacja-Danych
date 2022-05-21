import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro:')
plt.ylabel('liczby z wektora')
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r:')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')

plt.axis([0, 6, 0, 20]) - granice osi xmin, xmax, ymin, ymax
plt.show()

x = np.arange(0, 5.2, 0.2)

plt.plot(x, x, 'r-', x, x**2, 'b^', x, x**3, 'gs')
plt.legend(labels=['liniowa', 'kwadratowa', 'sześcienna'], loc='center left')
plt.show()

plt.plot(x, x, label='liniowa')
plt.plot(x, x**2, label='kwadratowa')
plt.plot(x, x**3, label='sześcienna')
plt.legend()
plt.savefig('plot.png')
plt.show()
im1 = Image.open('plot.png')
im1 = im1.convert('RGB')
im1.save('plot.jpg')

x1 = np.arange(0, 2.02, 0.02)
x2 = np.arange(0, 2.02, 0.02)

y1 = np.sin(2*np.pi*x1)
y2 = np.cos(2*np.pi*x2)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'r--')
plt.ylabel('sin(y)')
plt.xlabel('x')
plt.title('wykres sin(x)')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'go')
plt.xlabel('x')
plt.ylabel('cos(y)')
plt.title('wykres cos(x)')

plt.subplots_adjust(hspace=0.5)
plt.show()

fig, axs = plt.subplots(3, 2)

axs[0, 0].plot(x1, y1, 'r-')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('sin(x)')
axs[0, 0].set_title('wykres sin(x)')

axs[1, 1].plot(x2, y2, 'g-')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('cos(x)')
axs[1, 1].set_title('wykres cos(x)')

axs[2, 0].plot(x2, y2, 'b-')
axs[2, 0].set_xlabel('x')
axs[2, 0].set_ylabel('cos(x)')
axs[2, 0].set_title('wykres cos(x)')

fig.delaxes(axs[0, 1])
fig.delaxes(axs[1, 0])
fig.delaxes(axs[2, 1])
plt.show()

dane = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

dane['b'] = dane['a'] + 10 * np.random.randn(50)
dane['d'] = np.abs(dane['d']) * 100

plt.scatter(data=dane, x='a', y='b', c='c', s='d', cmap='turbo')
plt.xlabel('wartości a')
plt.ylabel('wartości b')
plt.show()
print(dane['c'])

dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasillia', 'Warszawa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}

df = pd.DataFrame(dane)
grupa = df.groupby('Kontynent')
etykiety = list(grupa.groups.keys())
wartosc = list(grupa.agg('Populacja').sum())

plt.bar(x=etykiety, height=wartosc, color=['red', 'green', 'blue'])
plt.xlabel('Kontynenty')
plt.ylabel('Populacja na kontynentach')
plt.show()

x = np.random.randn(10000)

plt.hist(x, bins=15, facecolor='g', alpha=0.75, density=True)
plt.xlabel('wartości x')
plt.ylabel('prawdopodobieństwa')
plt.show()