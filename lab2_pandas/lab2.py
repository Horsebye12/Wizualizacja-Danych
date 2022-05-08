#biblioteka matplotlib 3.5.1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df3 = pd.read_csv('dane.csv', header=0, sep=';', decimal=".")

grupa = df3.groupby('Imię i nazwisko').agg({'Wartość zamówienia': ['sum']})
print(grupa)
grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, colors=['red', 'green'], figsize=(19.20, 10.80)) #tworzenie wykresu kołowego, subplots odseparowuje
# wartości, autopct wyświetlanie danych w zaokrągleniu
plt.legend(loc='upper left')
plt.show()

seria = pd.Series(np.random.randn(1000))
seria = seria.cumsum()

seria.plot() #domyślnie wykres liniowy
plt.show()
