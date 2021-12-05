import pandas as pd

path = 'C:\\Users\\ldoma\\Downloads\\Rybnik\\'

Dane_Ostateczne_Processing = pd.read_csv(path+'Dane_Przejazdy.csv')

dane2 = Dane_Ostateczne_Processing
przystanki = Dane_Ostateczne_Processing['begin_id'].unique()
przystanki.sort()

for i in przystanki:
    new_string = input(i) 
    Dane_Ostateczne_Processing['end_id'] = Dane_Ostateczne_Processing['end_id'].apply(lambda j: new_string if  j==i else j)
    Dane_Ostateczne_Processing['begin_id'] = Dane_Ostateczne_Processing['begin_id'].apply(lambda j: new_string if  j==i else j)


Dane_Ostateczne_Processing.to_csv(path+'Nowe_indeksy.csv',index=False)