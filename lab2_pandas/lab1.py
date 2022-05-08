import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([10, 12, 14, 18], index=['a', 'b', 'c', 'd'])
print(s)

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190826, 130317835, 207847528]}
df = pd.DataFrame(data)

# df3 = pd.read_csv('dane.csv', header=0, sep=';', decimal=".")  #czytanie plików csv, header to który wiersz jest nazwami
# # kolumn, sep czym są oddzielone dane, decimal znak określający liczby dziesiętne
# print(df3)
# df3.to_csv('dane2.csv', index=False)  #zapis do pliku csv
#
# xlsx = pd.ExcelFile('imiona.xlsx')  #odczyt pliku excel
# df4 = pd.read_excel(xlsx, header=0)  #zapis danych excel do ramki danych
# print(df4)
# df4.to_excel('imiona2.xlsx', sheet_name='dane')  #zapis do pliku excel, sheet_name to nazwa arkusza

# print(df4.head(10))  #ilość wyświetlanych wierszy z danych od góry
# print(df4.tail(10))  #ilość wyświetlanych wierszy z danych od dołu

print(s[s > 16])  #wyświetlanie danych z serii przy określonym warunku
print(s[(s < 13) & (s > 8)])

print(s.where(s > 10, 'warunek niespełniony'))  #podobne do tego powyżej, ale wyświetla gdzie warunek nie jest spełniony,
# określić co się ma wyświetlać gdy warunek nie jest spełniony
seria = s.copy() #kopiuje serię danych
seria.where(s > 10, 'warunek niespełniony', inplace=True)  #inplace modyfikuje serię danych
print(seria)

print(df[df['Populacja'] > 12000000])  #warunki dla ramek danych

s['e'] = 14  #dodawanie nowego elementu serii danych poprzez odniesienie do nieistniejącego, kolejnego indeksu
print(s)

df.loc[3] = 'nowy element'  #dodawanie nowego elementu ramki danych podobnie jak wyżej
print(df)
df.loc[4] = ['Polska', 'Warszawa', 38675468]
print(df)

new_df = df.drop([3])  #usuwanie wiersza z ramki danych
print(df)
#jeżeli chcemy zredukować liczbę indeksów przy usuwaniu wiersza należy df.drop zapisać do nowej zmiennej
print(new_df)
new_df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
print(new_df)

print(new_df.sort_values(by='Kraj'))  #sortuje ramkę
new = new_df.sort_values(by="Kraj")  #zapisuje posortowaną ramkę
print(new)

grupa = new_df.groupby(by='Kontynent').agg({'Populacja': ['sum']})  #grupowanie danych
# print(grupa.get_group('Europa'))  #wybieranie grupy
# print(grupa.agg({'Populacja': ['sum']}))  #agregacja danych

# grupa.plot(kind='bar', xlabel='Kontynenty', ylabel='Populacja', rot=0, title='Populacja na kontynentach')  #tworzenie wykresu, x i y label to nazwy etykiet, kind to rodzaj wykresu, rot to obrót, title to tytuł

wykres = grupa.plot.bar() #tworzenie wykresu bez ustawień dodatkowych
wykres.set_xlabel('Kontynent')
wykres.set.ylabel('Populacja w mld')
wykres.tick_params(axis='x', labelrotation=0)
wykres.set_title('Populacja na kontynentach')
plt.savefig('plot1.png')
plt.show()
