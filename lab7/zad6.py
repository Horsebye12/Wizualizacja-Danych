import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('zamowienia.csv', sep=';')
policzone = df.groupby('Sprzedawca')['Utarg'].sum()
print(policzone)
# explode
explode = [0.0 for n in range(len(policzone.index))]
# określamy które kawałki i o ile wysunąć, tu losujemy jeden
explode[np.random.randint(0, len(policzone.index))] = 0.2
wedges, texts, autotext = plt.pie(x=policzone, labels=policzone.index,
                                  autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color='black'), explode=explode, shadow=True)
plt.title("Procentowy udział kwot zamówień sprzedawców")
plt.show()