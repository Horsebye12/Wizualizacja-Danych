import numpy as np

macierz = np.array([[1, 2], [83, 31]])
kierunek = input("Podaj kierunek dzielenia (pion/poziom): ")

def podziel(macierz, kierunek):
    if(kierunek == 'poziom'):
        try:
            return np.split(macierz, 2)
        except(ValueError):
            print('Ilość wierszy nie pozwala na dzielenie')
    elif(kierunek == 'pion'):
        try:
            return np.split(macierz, 2, axis=1)
        except(ValueError):
            print('Ilość kolumn nie pozwala na dzielenie')


print(podziel(macierz, kierunek))