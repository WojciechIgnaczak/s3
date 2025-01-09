# Inne

### Wyświetlenie wartości id
```sql
SELECT * FROM klienci_id_seq;

SELECT last_value FROM klienci_id_seq;
```
### Wartość następnego id
```sql
SELECT nextval('klienci_id_seq');
```


### Uprawnienia do baz
- `-C` pozwla tworzyc nowe schematy

- `-c` sprawdza uprawnienia roli przy próbie połączenie do bazy

- `-T` tworzenie tabel tymczasowych niszczone po zakończeniu sesji usera

jeśli nie ma wpisu w *Access privileges* to rola przypisna jest PUBLIC

Encoding pozwla na przechowywanie 1 lub wielobajtowych zestawów znaków tj *SQL_ACII* lub *UTF-8*.

### Inne atrybuty baz danych

- Maintenance - *datafrozenxid* - do określenia czt baza wymaga procesu vacuum

- Zarządzanie przestrzenią dyskową- *dattablespace* -określa przestrzeń tabel dla baz danych

- Równoczesność- *datconnlimit* - liczba pozwolonych połączeń. Wartość -1 oznacza brak ograniczeń

- Ochrona- *datallowconn* - wyłącz możliwość połączenia z bazą danych, głównie w celu ochrony template0 przed modyfikacjami

#
### Tablespace w bazach danych
Przestrzeń dyskowa którą wskazujemy gdzie nasze dane będą przechowywane. Każda baza/tabela może być na innym dysku, katalogu. 

#### Utrzymaniowość i zarządzanie miejscem (Maintenance)
- Jeśli na dysku brakuje miejsca, można utworzyć tablespace na innej partycji. Dzięki temu możemy przenieść dane do nowej lokalizacji, unikając problemów związanych z brakiem miejsca

#### Optymalizacyjne
- Przenoszenie danych na szybsze dyski

#### Tworzenie tablespace
```sql
CREATE TABLESPACE fast_storage LOCATION '/mnt/ssd_partition/';
```
#### Używanie tablespace
```sql
CREATE TABLE moja_tabela(
    id SERIAL PRIMARY KEY;
    nazwa VARCHAR(255) NOT NULL;
)TABLESPACE fast_storage;
```


Ustawienia kontekstu
w jaki sposób będziemy zmieniać wartości

- Internal(wewnętrzy) Nie można zmieniać bezpośrednio

- Postmaster        Zmiana parametrów wiąże się z restartem postgres

- Sighup            Trzeba wysłać sygnał po zmianie do procesu

- Backend           Nie wymaga restartu i od razu powinny działać

- Superuser         Przez komendę set, będą działać cały czas 

- User              W trakcie działanie bieżącej sesji

`SET` i `SHOW` służą do zmiany i sprawdzania wartości parametrów ustawień

Zmiana w `postgresql.conf` ma efekt globalny

Przeładowanie konfiguracji `SELECT pg_reload_conf();`

Pełne nazwy są czasochłonne, dlatego preferuje się korzystanie z nazw obiektów, które zawierają tylko nazwę obiektu bez schematu.

PostgreSQL umożliwia ustawienie `search_path` które ma ścieżkę wyszukiwania.

# Modelowanie danych
Reprezentowanie pojedynczych encji

Diagramy ER

Obiekty owalne - proste

Obiekty prostikątne mają atrybuty złożone

Znaczenie modeli danych odgrywają rolę w utrzymaniu spójności danych w systemach współpracujących. Źle zdefiniowane encje mogą prowadzić do zamieszania i niespójności w całej organizacji. np. (klient vs kontrahent), moze prowadzić do nieporozumień. 

## Trzy modele danych:

- konceptualny

- logiczny - struktura danych okreslnonych technologii

- fizyczny - implementacja bazy danych

## Model encji i relacji (ER) 

Jest typem modelu danych konceptualnego zaprojektowanych do uchwycenia i reprezentowania encji oraz ich relacji.

Używany przez developerów i biznes

## Praktyki w modelowaniu
- nadmiarowość danych - zbyt duze moga powodowac problemy tj. niespójnosc i degradacja wydajnosci

- saturacjia wartosci null - problem aby w JSON dany klucz nie przyjmuje wartosci NULL 

- ścisłe powiązanie - ścisłe powiązanie miedzy enacjami moze prowadzic do sztywnych struktur, co utrudnia przyszle zmiany

### pytania kontrolne check list
co jest kluczem głównym?

jaka domyślna wartość kolumny

jaki typ kolumny

ograniczenia

uprawnienia

klucze obce

cykl życia danych

jakie operacje są dozwolone



### KLUCZE naturalne a zastepcze
klucze naturalne - oczywiste i rozpoznawalne - mogą się zmieniać. a użycie klucza zastępczego zapewnia ze referencja do innych wierszy nie zostanie utracony, poniewać klucz zastepczy sie nie zmienia.

błędne założenia o kluczach naturalnych 

klucze zastepcze moga wspierac projekty bazy danych tymczasowej

klucze zastepcze czesto uzywaja kompaktowych typow danych (liczby calkowite)

klucz zastepcze sa generowane automatyczne co moze prowadzic do roznych wynikow w roznych bazach testowych

klucz zastepczy nie jest opisowy



