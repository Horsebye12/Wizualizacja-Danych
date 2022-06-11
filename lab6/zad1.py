import numpy as np
import pandas as pd

data = pd.read_excel('imiona.xlsx')

print(data[data.Liczba > 1000])
print(data[data['Imie'] == "DAWID"])
print(data['Liczba'].sum())

r1 = data[data['Rok'] == 2000]
r2 = data[data['Rok'] == 2001]
r3 = data[data['Rok'] == 2002]
r4 = data[data['Rok'] == 2003]
r5 = data[data['Rok'] == 2004]
r6 = data[data['Rok'] == 2005]

print("Liczba dzieci urodzonych w roku 2000: ", r1['Liczba'].sum())
print("Liczba dzieci urodzonych w roku 2001: ", r2['Liczba'].sum())
print("Liczba dzieci urodzonych w roku 2002: ", r3['Liczba'].sum())
print("Liczba dzieci urodzonych w roku 2003: ", r4['Liczba'].sum())
print("Liczba dzieci urodzonych w roku 2004: ", r5['Liczba'].sum())
print("Liczba dzieci urodzonych w roku 2005: ", r6['Liczba'].sum())

#dokończyć


