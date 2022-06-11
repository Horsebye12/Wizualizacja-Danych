import numpy as np
import pandas as pd

data = pd.read_csv("zamowienia.csv", header=0, sep=";")
print(pd.unique(data['Sprzedawca']))
sort = data.sort_values(by=['Utarg'], ascending=False)
print(sort.head(5))

grupa1 = data.groupby(['Sprzedawca'])
print(grupa1.agg('Utarg').sum())

grupa2 = data.groupby(['Kraj'])
print(grupa2.agg('idZamowienia').count())

data['Rok'] = pd.DatetimeIndex(data['Data zamowienia']).year
data_polska = data[data['Kraj'] == 'Polska']
data_polska_2005 = data_polska[data_polska['Rok'] == 2005]
data_polska_2005_suma = data_polska_2005.agg('idZamowienia').count()
print(data_polska_2005_suma)

data_2004 = data[data['Rok'] == 2004]
data_2004_srednia = data_2004.agg('Utarg').mean()
print(data_2004_srednia)

data_2004_save = data[data['Rok'] == 2004]
data_2005_save = data[data['Rok'] == 2005]
data_2004_save.to_csv('zamowienia_2004', index=False)
data_2004_save.to_csv('zamowienia_2005', index=False)