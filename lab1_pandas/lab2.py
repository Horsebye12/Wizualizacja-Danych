import pandas as pd
import numpy as np
import openpyxl as opx

s = pd.Series([1, 3, 4, 'a', 3.5]) #tworzy serię danych
print(s)
s2 = pd.Series([10, 12, 14, 8], index=['a', 'b', 'c', 'd']) #nadawanie własnych indeksów
print(s2)

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia',],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 130317035, 207847528]}

df = pd.DataFrame(data) #tworzy ramkę danych jako tablicę dwuwymiarową oraz etykietami kolumn
print(df)

daty = pd.date_range('20220507', periods=5) #seria dat w formacie yyyymmdd, periods określa liczbę dni
print(daty)

df2 = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD')) #ramka danych, jako indeksy ma daty z powyżej oraz nazwy kolumn
print(df2)

df3 = pd.read_csv('dane.csv', header=0, sep=';', decimal='.') #odczytuje dane z pliku csv, header określa który wiersz zawiera nazwy kolumn,
# sep to separator który został użyty do rodzielenia danych, decimal to jaki znak oddziela wartości dziesiętne
print(df3)
df3.to_csv('dane2.csv', index=False) #zapisuje dane do pliku csv, index określa czy indeksy mają być również zapisane


xlsx = pd.ExcelFile('datasets/imiona.xlsx') #odczytuje pliki excelowe
df4 = pd.read_excel(xlsx, header=0)
print(df4)

df4.to_excel('imiona.xlsx', sheet_name='dane') #zapisuje dane do pliku excel, sheet_name określa nazwę arkusza

