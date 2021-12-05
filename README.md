## FungyOpti -  Repozytorium preprocessingu

FungyOpti to prosta i łatwa w użyciu aplikacja do wizualizacji 
ilości wsiadających i wysiadających na przystankach oraz Analizy przemieszczenia z komunikacją Miejską. 
W tym Repozytoium znajdują się Notatniki i skrypty służące do preprocessingu danych, do formatu wykorzystywanego przez aplikację.

### Zawartość Repozytorium
+ **Rybnik_Preprocessing** - notatnik jupytera służący do wstępnego preprocessingu,
	czyszczenia i transformacji zmiennych 
+ **Rybnik_Preprocessing_CD** - Ciąg dalszy analiz, gdzie dane dla biletów nieokresowych, są sprowadzane do właściwej formy.
	Również Dane Geograficzne są sprowadzane i procesowane by stworzyć Bazę Danych Przystanków
+ **Rybnik_Preprocessing_CD** - Ciąg dalszy analiz, gdzie dane dla biletów nieokresowych, są sprowadzane do właściwej formy.
	Również Dane Geograficzne są sprowadzane i procesowane by stworzyć Bazę Danych Przystanków
+ **Rybnik_Preprocessing_Okresowe** - Preprocessing danych dla biletów okresowych, wraz z wydobyciem przystanków końcowych.

+ **Przystanki.csv** - Baza danych z Nazwami przystanków, kodem, Dzielnicą oraz współrzędnymi geograficznymi
+ **Połączenia.csv** - Baza z rekordami zawierająca numer karty, datę dzienną, godzinę , dzień tygodnia, oraz kod przystanku początkowego i końcowego
+ **Przepracowanie.py** - Skrypt Pythona umożliwiający szybkie manualne poprawienie ID rekordów
+ + **Rybnik_Analiza** - W tym pliku znajdują się  wstępne analizy i wizualizacje Danych. Głównie zorientowane na Histogramy oraz mapy ciepła obrazujące częstość 	wsiadania/wysiadania na przystanku zależne od parametrów. Przykładowo, tutaj widnieje wzajemna zależność obłożenia dwóch linii:


![image](https://user-images.githubusercontent.com/56306081/144738386-079ea4cc-1ece-4430-800a-b84f0715e36f.png)


