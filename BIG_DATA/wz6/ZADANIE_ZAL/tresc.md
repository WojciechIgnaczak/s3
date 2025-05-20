# BAZA - dopasuj, rozbuduj, dodaj tabele, rozbuduj tabele. Recepta-produkt relacja wiele do wielu i to napraw
Pacjent
    id
    imie
    nazwisko
    imie2
    wiek

Wizyta
    id
    pacjent_id
    lekarz_id
    opis
    zalecenia

Recepta
    id
    wizyta_id

Produkt
    id
    recepta_id
    nazwa

Lekarz
    id
    imie
    nazwisko
    imie2

Skierowanie
    id
    wizyta_id

Badanie
    id
    skierowanie_id


1. porownianei zapisu i wydobywania danych z obciazonego postgres(duzo danych, rownolegle zapytania z wielu procesów)
milion pacjentów, 10 wizyt na pacenta, na co 2 wizyci skierowanie pacjenta, recepta na co 2 wizycie, 2,5mln skierowan, 2,5mln recept
ile danych w ciagu 1s. jeżeli jest n połączeń. ile danych efektywnie wyciągnąć. porównanie z wielkością bazy tzn. jezeli pacjentow jest 100k, 500k, 1mln itd. czy ta zależność jest liniowa czy inaczej(jakieś wykresy itd.), dane przyrastaja. zbadanie operacji zapisu. predkosc zapisu w zalezosci od wielkosci zapisu.
równocześnie update'y i selecty i zwieksanie ich ilosci na kilku procesów(2,20,100)
wszystkie zadania na maszynach wirtualnych. virtualbox na linux'ach
wyniki zadań w formie sprawozdania.


<!-- 2. ile miejsca zajmuje missing value/null
ile miejsca zajmują miejsca puste w bazach danych
n atej samej bazie danych
wypeełnić baze w 100% i sprawdzić ile zajmuje na dysku i w pamięci(jeśli można)
generownie tej samej bazy tylko (10%,20%,30%,40%....100%) w tabelach to nulle i sprawdzić ile miejsca zajmują
w tabelach kolumny różnego typu(int,float,varchar(64), text,data, pole binarne blob) i sprawdzić zależność typów od null w pamięci -->

3. porównaice form zapisu danych hd5(hdf5),parquet, avro
popularne formaty zapisywania dużych zbiorów danych.
jak się zachochują prdkosc zapisu, predkosc odczytu, czy mozna czytac selektywnie dane np. rekord 5,2000, czy musze wczytac cały plik. mozliwosc modyfikacji danych, czy jest możliwy update i jak wygląda, jaki koszt

4. dystrybucja plików w katalogach. utworzenie katalogów z dużą ilościa plików (100 000 +) po 1mb . czy ma znaczenie rozmieszczenie plików jeśli w 1 pliku i uruchomienie procesów do czytania tych danych. 2 opcja rozrzucenie plików po katalogach to czas na odczytanie tych plików jaki jest w porównaniu (mówi sie ze efektywnosc opereccjio plikowych na duzych katalogach maleje).

5. janus db 
baza grafowa
pacjent to węzeł grafu
wizyty do też węzeł
połączenie to krawędzie
szukanie związków
spróbowanie jej użyć, zainstalować i za pomocą jakiegoś języka dodać update ususnac select

6. apache ignite
baza klucz-wartosc 
in merory
zainstalować testy, seria przykładów jak uzywać CRUD
kluczem np. pesel klucz nie sluzy do laczenia danych miedzy soba
opis, wprowadzenie,idea baz
pod jednym kluczem są info o pacjencie , jego ostatnich wizytach, wydanych receptach, skierowaniach
<!-- 7. Hadoop, rozproszony system plików hdfs and save data i 1B 1KiB, 10KiB etc
hdfs jest systemem plików 
dane są porozdzielane
system do przetwarzania dużych zbiorów danych (fizycznie duże pliki)
jednostka alokacji 100mb, cokolwiek zajmie conajmniej 100mb
nie nadaje sie do plików małych
jak wygląda zapisywanie plików o rozmiarach 1B, 1KiB, 10, 100, 1000... 1GB
ile skonsumowały miejsca -->

<!-- 
8. Aplikacja webowa (fastAPI, flask)+ firebase
baza firebase - nierelacyjna , baza jsonowa do klucza głównego jest podpięty json
aplikacja webowa ktora dane o pacjentach zapisuje do firebase
albo flask albo flaskAPI
+ apliakcja moblina która wyciąga dane do apliakcji (dodatek)

9. Algorytmy genetyczne
algorytm genetyczny działa rozwiazanie problemu to ciąg 0,1
ciąg koduje liczbe
funckcja przystosowania jak dobrym rozwiazaniem naszego problemu jest ciąg 
zrobienie problemu
podział na populacje 
jako poszukiwanie minimum funkcji
na wiele procesów
z 1 populacji robi wiele populacji -->


wirtualka + sprawozdanie do oddania