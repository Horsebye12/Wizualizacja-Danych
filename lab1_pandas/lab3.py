import numpy as np
import pandas as pd
import openpyxl

s2 = pd.Series([10, 12, 14, 8], index=['a', 'b', 'c', 'd'])

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia',],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 130317035, 207847528]}
df = pd.DataFrame(data)

print(s2['a']) #wybieranie elementu serii po indeksach
print(s2.a)

print(df[0:1])
print(df['Kraj'])
print(df.Kraj)

print(df.iloc[[0], [0]])
print(df.loc[[0], ['Kraj']])
print(df.at[0, 'Kraj'])

print(df.sample(2))
print(df.sample(10, replace=True))