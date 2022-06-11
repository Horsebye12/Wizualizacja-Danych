import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
plt.subplot(1, 3, 1)
grouped = df.groupby('Plec')
etykiety = list(grouped.groups.keys())
wartosci = list(grouped.agg('Liczba').sum())
plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
plt.xlabel('Płeć')
plt.ylabel('Liczba narodzonych dzieci')
# wykres 2
plt.subplot(1, 3, 2)
x = df['Rok'].unique()
kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
plt.plot(x, kobiety, label="Kobiety")
plt.plot(x, mezczyzni, label="Mężczyźni")
plt.xlabel('Rok')
#
# # wykres 3
plt.subplot(1, 3, 3)
x = df['Rok'].unique()
y = df.groupby('Rok').agg('Liczba').sum()
plt.bar(x, y)
plt.xlabel('Rok')
# wyświetlamy cały wykres
plt.subplots_adjust(wspace=0.85)
plt.show()