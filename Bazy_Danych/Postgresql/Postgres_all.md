# Podstawa
### Logowanie do postgreSQL
```
sudo -i -u user_name
```
### Wylogowanie z postgreSQL
```
exit
```
### Wejście do psql
```
psql

psql -U user_name -d nazwa_bazy -h host -p port   
```
Host domyślnie **localhost**

Port domyślnie **5432**

Nie trzeba wykorzystywać wszystkich parametrów jeśli są domyślne
### Wyjście z psql
```
\q
```
# Pomoc
### Pomoc do  poleceń SQL (np. SELECT)
```
\h SELECT
```

### Pomoc do  poleceń psql, wyświetla wszyskie komendy psqlq
```
\? 
```
# Zarządzanie Bazami Danych
### Lista baz danych
```
\l
```
### Sprawdzenie z jaką bazą jesteśmy połączeni. Informacje o aktualnym połączeniu.
```
\c

\conninfo
```
### Połączenie z bazą danych i zamknięcie aktualnego połączenia
```
\c nazwa_bazy
```


# Zarządzanie tabelami w bierzącej bazie

### Lista tabel
```
\dt
```

### Lista widoków
```
\dv
```

### Opis struktury tabeli lub widoku
```
\d nazwa_tabeli_lub_widoku
```

### Lista wszystkich obiektów na bazie (tabele,widoki,indeksy)
```
\d
```


# Zarządzanie użytkownikami i rolami

### Lista użytkowników (ról) na bazie
```
\du
```

### Informacje o konkretnym użytkowniku
```
\du nazwa_uzytkownika
```


# Zarządzanie schematami
### Wyświetlenie wszystkich schematów na bazie
```
\dn
```
### Wyświetlenie tabel w określonym schemacie
```
\dt nazwa_schematu.*
```

# Zarządzanie funkcjami
### Wyświetlanie funckji na bazie
```
\df
```


# Zarządzanie sekwencjami
### Wyświetlanie sekwencji na bazie
```
\ds
```
### Wyświetlenie wartości id
```
SELECT * FROM klienci_id_seq;

SELECT last_value FROM klienci_id_seq;
```
### Wartość następnego id
```
SELECT nextval('klienci_id_seq');
```


# Zarządzanie wyjściem i zapis wyników do pliku
### Zapis danych wyjściowych do pliku
```
\o nazwa_pliku.txt
SELECT * FROM nazwa_tabeli;
\o
```


# Praca z danymi
### Ustawienie pojedynczego rekordu na linie
```
\x
```


# Historia
### Historia użytych komend
```
\s
```

# Z/do pliku
### Eksport danych do pliku csv
```
\copy nazwa_tabeli TO 'ścieżka/do/pliku.csv' CSV HEADER;

```
### Import danych z pliku csv
```
\copy nazwa_tabeli FROM 'ścieżka/do/pliku.csv' CSV HEADER;

```
### Wywołanie zapytania z pliku
```
\i '/sciezka/do/schema.sql'
```
### Aliasy
```
\alias ll \! ls -l

\alias mytables \dt public.*
```
alias **ll** - wyświela nam wszystkie pliki

alias **mytables** - wyświetla nam wszystkie tabele w schemacie


# Timing
### Włączenie trybu pomiaru czasu wykonania zapytań
```
\timing
```
### Tryb rozszerzonego wyświetlenia
```
\x
```


# Zmienne
### Definiowanie zmiennej, aby użyc jej w zapytaniu
```
\set min_salary 50000
SELECT * FROM employees WHERE salary > :min_salary
```

# Zapytanie w edytorze
```
\e
```
# Zmiana kodowania
```
\encoding UTF-8
```

# Powtórzenie zapytania
```
\g
```

# Wyswietlenie aktywnych sesji co 10 sekund
```
\watch 10
```


# Polecenia w terminalu (nie w psql)

### Usuwanie istniejącej bazy danych PostgreSQL
```
dropdb nazwa_bazy;
```

### Tworzenie nowej  bazy danych PostgreSQL
```
createdb nazwa_bazy;
```

### Usuwanie usera
```
dropuser name
```
### Tworzenie usera
```
createuser name
```

### Tworzy ponownie indeksy
```
reindexdb
```

# Teoria postgres
### Bazy danych template
podczas tworzenia nowej bazy danych w Postgres jest domyślnie klonowana template o nazwie template1. Zawiera tabele,widoki,funckje służą do modelowania relacji między obiektami tworzonymi przez usera.

### Schema
Służy do organizacji obiektów baz danych

Serwer postgres ma 2 bazy szablonowe template0, template1 można wyświetlić przez ```\l```

### Template1
Domyślna baza która jest klonowana przy tworzeniu nowych baz. Można ją modyfikować aby wprowadzić zmiany globalne dla wszystkich nowo tworzonych baz. Np. chcemy używać we wszystkich nowych bazach jakiegoś rozszerzenia

### Template0
Baza zabezpieczająca lub wersjonowana która może służyć do naprawy template1, przywracania zrzutu bazy, nie zawiera danych kodowania,lokalizacji. Nie utworzymy z niej nowej bazy.

### Tworzenie bazy z szablonu
Można w Postgres tworzyć bazy z wykorzystaniem dowolnej bazy jako szablonu. Przydatne do testowania, refaktoryzacji bazy

### Bazy danych w klastrze bazy danych
W klastrze może mieć dowolną liczbę baz danych

Połączenie z serwerem  może uzyskać dostęp do danych w jednej bazue danych 

Dane nie są współdzielone między bazami. chyba że użyte są rozszerzenia tj postgres foreign data wrappper

Każda baza ma właściciela oraz zestaw uprawnien które kontrolują dzialania dozwolone dla danej roli


### Uprawnienia do baz
- ```-C``` pozwla tworzyc nowe schematy

- ```-c``` sprawdza uprawnienia roli przy próbie połączenie do bazy

- ```-T``` tworzenie tabel tymczasowych niszczone po zakończeniu sesji usera

jeśli nie ma wpisu w *Access privileges* to rola przypisna jest PUBLIC

Encoding pozwla na przechowywanie 1 lub wielobajtowych zestawów znaków tj *SQL_ACII* lub *UTF-8*.

### Inne atrybuty baz danych

- Maintenance - *datafrozenxid* - do określenia czt baza wymaga procesu vacuum

- Zarządzanie przestrzenią dyskową- *dattablespace* -określa przestrzeń tabel dla baz danych

- Równoczesność- *datconnlimit* - liczba pozwolonych połączeń. Wartość -1 oznacza brak ograniczeń

- Ochrona- *datallowconn* - wyłącz możliwość połączenia z bazą danych, głównie w celu ochrony template0 przed modyfikacjami

### Tabele katalogowe *pg_catalog*
Zwykłe tabele na których możemy używać ```SELECT```,```UPDATE```,```DELETE```. Nie zaleca się modyfikacji ręcznej, chyba że w wyjątkowych sytuacjach.

```
SELECT datconnlimit FROM pg_database WHERE datname="nazwa_bazy";        // wyświetlenie limitu połączeń z bazą danych
ALTER DATABASE nazwa_bazy CONNECTION LIMIT 1                            //zmiana limitu połączeń na 1. -1 dla wszystkich
UPDATE pg_database SET dataconnlimit=-1 WHERE datname='nazwa_bazy';     //nie zalecania zmiana limitu połączeń, ponieważ  przy nieprawidłowej wartości nie wyrzuca błędu np. "-2"
```

### Role
[ROLE_LINK](https://www.postgresql.org/docs/current/role-attributes.html)

Role należą do klastra serwera a nie do konkretnej bazy.

Rola może być userem bazy danych lub grupą użytkowników. Koncepcja roli łączny pojęcia użytkowników i grup z poprzednich wersji postgres.

Polecenia:
```
CREATE USER
CREATE GROUP
```
ROLE
- create database

- connection limit

- super user

- Login

- Inherit

- settings

- Password (Encrypted, validity)

SuperUżytkownik - rola może pomijać wszystkie sprawdzniea uprawnie n z wyjątkiem logowania

Logowanie - Do łączenia się z bazą danych

Tworzenie bazy - może tworzyć nowe bazy danych

Inicjowanie replikacji -  może być używana do replikacji strumieniowej

Hasło - może zmienić swoje hasło

Limit połączeń - może zmieniać limit połączeń

Dziedziczenie (inherit) - może dziedziczyć uprawnienia do roli których jest członkiem
```
CREATE ROLE janek WITH LOGIN PASSWORD 'hasło' // rola ma możliwość logowania do bazy z hasłem
```
CREATE GROUP jest równoznaczne z poleceniem CREATE ROLE z opcją NOLOGIN
```
CREATE ROLE programisci; // tworzy role która moze byc uzywana jako grupa
```

### Członkowstwo ról
Rola może być członkiem innych roli. Rola bez logowania to grupa. 
Dostęp realizują polecenia SQL ```GRANT``` i ```REVOKE```
```
GRANT programisci TO janek // dodanie janka do grupy programisci

REVOKE programisci FROM janek // usuwa janke z grupy programisci
```
### Uprawnienia ról
```
CREATE ROLE admin WITH CREATEDB LOGIN PASSWORG 'admin';                  // tworznie roli do tworzenia baz danych
GRANT SELECT,INSERT ON tabela TO janek;                                  // przypisanie uprawinen do użytkownika
CREATE ROLE superadmin WITH SUPERUSER LOGIN PASSWORD 'password'          // tworzenie roli superużytkownika
CREATE ROLE limit_user WITH LOGIN PASSWORD 'haslo' CONNECTION LIMIT 5;   // tworzy rolę z limitem max 5 jednoczesnym połączeń
```

### Tablespace w bazach danych
Przestrzeń dyskowa którą wskazujemy gdzie nasze dane będą przechowywane. Każda baza/tabela może być na innym dysku, katalogu. 

#### Utrzymaniowość i zarządzanie miejscem (Maintenance)
- Jeśli na dysku brakuje miejsca, można utworzyć tablespace na innej partycji. Dzięki temu możemy przenieść dane do nowej lokalizacji, unikając problemów związanych z brakiem miejsca

#### Optymalizacyjne
- Przenoszenie danych na szybsze dyski

#### Tworzenie tablespace
```
CREATE TABLESPACE fast_storage LOCATION '/mnt/ssd_partition/';
```
#### Używanie tablespace
```
CREATE TABLE moja_tabela(
    id SERIAL PRIMARY KEY;
    nazwa VARCHAR(255) NOT NULL;
)TABLESPACE fast_storage;
```
### Ustawnienia PostgreSQL 
- Replikacja (Replication) - Konfiguracja replikacji danych pomiędzy serwerami

- Dzienniki Write-Ahead Logs (WAL) - Zarządzanie logami

- Zużycie zasobów (Resource consuption) - Kontrola nad zasobami sprzętowymi tj. RAM, CPU przeznaczonych na działanie serwera

- Planowanie zapytań (Query planning) - optymalizacja planów zapytań, aby uzyskać najlepszą wydajność

- Logowanie (Logging) - zapis logów na serwerze

- Uwierzetylnienie

- Zbieranie staystyk

- Zarządznie blokadami

- Obsługa błędów

- Opcje debugowania


Ustawienia są zawarte w  `pg_settings`

Paramentry ustwawień
- Boolean(wartości logiczne)

- Integer (wartość całkowita)

- Enum (wartości wyliczeniowe)

- Floating Point (wartości zmiennoprzecinkowe)

- String (ciąg znaków) np. ścieżka

Ustawienia kontekstu
w jaki sposób będziemy zmieniać wartości

- Internal(wewnętrzy) Nie można zmieniać bezpośrednio

- Postmaster        Zmiana parametrów wiąże się z restartem postgres

- Sighup            Trzeba wysłać sygnał po zmianie do procesu

- Backend           Nie wymaga restartu i od razu powinny działać

- Superuser         Przez komendę set, będą działać cały czas 

- User              W trakcie działanie bieżącej sesji

```SET``` i ```SHOW``` służą do zmiany i sprawdzania wartości parametrów ustawień

Zmiana w `postgresql.conf` ma efekt globalny

Przeładowanie konfiguracji ```SELECT pg_reload_conf();```


# Typy i obiekty w PostgreSQL

Serwer:

-bazy danych

-role : użytkownicy lub grupy użytkowników. którym można nadawać uprawnienia do dostępu do różnych baz

-przestrzeń tabel:zarządzanie fizyczne przechowywania danych na dysku

-jezyk programowania: baza może wykorzystywać kilka języków programowania

Podczas tworzenia bazy należy określić właściciela oraz kodowanie znaków

Kodowanie określa w jaki sposób dane tekstowe będą przechowywane i przetwarzane

Domyślny szablon kodowania (template1)

```
CREATE ROLE car_portal_role LOGIN;

CREATE DATABASE car_portal
    WITH 
    ENCODING 'UTF8'
    LC_COLLATE 'en_US.UTF-8'
    LC_CTYPE 'en_US.UTF-8'
    OWNER car_portal_role;
```
Schematy

Baza danych może być traktowana jako kontener dla schematów bazy danych.

Podstawowy schemat w bazie postgres to *public*, każda nowo utworzona baza zawiera ten schemat, wszyscy użytkownicy mają dostęp do tego schematu.

Schemat jest wykorzystywany do organizacjii obiektów w bazach danych

Nazwy obiektów mogą się powtarzać w różnych schematach bez konfliktów

Aby zapobiec możliwości tworzenia obiektów w schemacie public przez wszystkich użytkowników należy wykonać
```
REVOKE CREATE ON SCHEMA public FROM PUBLIC
```
Dostęp do konkretnego obiektu
```
SELECT * FROM pg_catalog.pg_database;

TABLE pg_catalog.pg_database;
```

Pełne nazwy są czasochłonne, dlatego preferuje się korzystanie z nazw obiektów, które zawierają tylko nazwę obiektu bez schematu.

PostgreSQL umożliwia ustawienie `search_path` które ma ścieżkę wyszukiwania.

Wykorzystanie schematów:

- kontrola autoryzacji

- organizacja obiektów bazy danych

- utrzymywanie zewnętrznego kodu SQL

Utworzenie schematu dla takiej samej roli (2), w (1) można zmienić na inną rolę
```
CREATE SCHEMA car_portal_app AUTHORIZATION car_portal_app 

CREATE SCHEMA AUTHORIZATION car_portal_app 
```
[SCHEMATY DOKUMENTACJA](https://www.postgresql.org/docs/current/sql-createschema.html)

Warto używać `IF NOT EXISTS` , żeby nie wywalało błędów naprzykład w skryptach automatyzacyjnych.

## TABELE

`CREATE TABLE`

Mają 4 różne typy. Są dedykowane do konkretnych zadań. Jest możliwość klonowania zadań.

Materializacja wyników przez `SELECT`.

Tabele trwałe - zwykłe tabele, cykl od utworzenia do usunięcia

Tabele tymczasowe - tabele, cykl życia to sesja użytkownika.

Tabele bez logowanie *unlogged* - szybsze niż tabele trwałe, dane nie są zapisywane do plików WAL. Nie są odporne na awarie i nie mogą być replikowane na węzeł podrzędny

Tabele podrzędne - tabela, która dziedziczy jedną lub więcej tabel. Dziedzizenie jest często używane z wykluczeniem ograniczeń (constraint exclusion) w celu fizycznego partycjonowania danych na dysku twardym.

[TABELE DOKUMENATCJA](https://www.postgresql.org/docs/current/static/sql-createtable.html)

## Typy danych

Zmiana typu danych na tabeli jest bardzo kosztowna, zwłaszcza dla tabel o dużym obciążeniu. Koszt wynika z blokowania tabeli, a w niektórych przypadkach również z koniecznością jej przypisania.

Czynniki wyboru typu:
- rozszerzalność - czy maksywalna długość typu może być zwiększona bez konieczności pełnego skanowania tabeli

- rozmiar typu danych

Typy:
- numeryczne

- znakowe

- daty i czasu

| Name                                 | Aliases                 | Opis                                                |
|--------------------------------------|-------------------------|-----------------------------------------------------|
| bigint                               | int8                    | ośmiobajtowa liczba całkowita ze znakiem            |
| bigserial                            | serial8                 | ośmiobajtowa liczba całkowita autoincrementowana    |
| bit [ (n) ]                          |                         | bit string o stałej długości                        |
| bit varying [ (n) ]                  | varbit [ (n) ]          | bit string o zmiennej długości                      |
| boolean                              | bool                    | wartość logiczna (prawda/fałsz)                     |
| box                                  |                         | prostokąt na płaszczyźnie                           |
| bytea                                |                         | dane binarne („tablica bajtów”)                     |
| character [ (n) ]                    | char [ (n) ]            | łańcuch znaków o stałej długości                    |
| character varying [ (n) ]            | varchar [ (n) ]         | łańcuch znaków o zmiennej długości                  |
| cidr                                 |                         | adres sieciowy IPv4 lub IPv6                        |
| circle                               |                         | okrąg na płaszczyźnie                               |
| date                                 |                         | data kalendarzowa (rok, miesiąc, dzień)             |
| double precision                     | float8                  | liczba zmiennoprzecinkowa o podwójnej precyzji (8 bajtów) nie są dokładne bo działają na binarnym czyli są zaokrąglone |
| inet                                 |                         | adres hosta IPv4 lub IPv6                           |
| integer                              | int, int4               | czterobajtowa liczba całkowita ze znakiem           |
| interval [ fields ] [ (p) ]          |                         | okres czasu                                         |
| json                                 |                         | dane JSON w postaci tekstowej                       |
| jsonb                                |                         | dane JSON w postaci binarnej                        |
| line                                 |                         | linia nieskończona na płaszczyźnie                  |
| lseg                                 |                         | odcinek linii na płaszczyźnie                       |
| macaddr                              |                         | adres MAC (Media Access Control)                    |
| macaddr8                             |                         | adres MAC (Media Access Control) w formacie EUI-64  |
| money                                |                         | kwota walutowa                                      |
| numeric [ (p, s) ]                   | decimal [ (p, s) ]      | dokładna liczba o konfigurowalnej precyzji 12.344 (p,s)=(5,3)|         |
| path                                 |                         | ścieżka geometryczna na płaszczyźnie                |
| pg_lsn                               |                         | numer sekwencyjny logu PostgreSQL                   |
| point                                |                         | punkt geometryczny na płaszczyźnie                  |
| polygon                              |                         | zamknięta ścieżka geometryczna na płaszczyźnie      |
| real                                 | float4                  | liczba zmiennoprzecinkowa o pojedynczej precyzji (4 bajty) |
| smallint                             | int2                    | dwubajtowa liczba całkowita ze znakiem              |
| smallserial                          | serial2                 | dwubajtowa liczba całkowita autoincrementowana      |
| serial                               | serial4                 | czterobajtowa liczba całkowita autoincrementowana   |
| text                                 |                         | łańcuch znaków o zmiennej długości                  |
| time [ (p) ] [ without time zone ]   |                         | godzina (bez strefy czasowej)                       |
| time [ (p) ] with time zone          | timetz                  | godzina, włącznie ze strefą czasową                 |
| timestamp [ (p) ] [ without time zone]|                         | data i czas (bez strefy czasowej)                   |
| timestamp [ (p) ] with time zone     | timestamptz             | data i czas, włącznie ze strefą czasową             |
| tsquery                              |                         | zapytanie wyszukiwania pełnotekstowego              |
| tsvector                             |                         | dokument wyszukiwania pełnotekstowego               |
| txid_snapshot                        |                         | migawka identyfikatora transakcji na poziomie użytkownika |
| uuid                                 |                         | uniwersalny unikatowy identyfikator                 |
| xml                                  |                         | dane XML                                            |



Typy numeryczne:
- smallint 2 bajty -> int2

- int 4 bajty -> int4

- bigint 8 bajtów ->int8

- numeric/decimal zmienny do 130,000 przed przecinkiem do 16,000 po przecinku

- real 4 bajty -> Infinity/Nan

- double/precision 8 bajtów

typ danych `serial`

część ułamkowa na int jest zawsze odrzucana(nie zaokrąglana) 2/3=0, 3/2=1

Typy znakowe:
- char - pojedynczy znak

- name - odpowiednik varchar(64), używany przez postgres do nazw obiektów

- char(n) - stała długość znaków, gdzie długość to *n*, na końcu zostaną dodane spacje.

- varchar(n) - zmienna długość znaków gdzie maksymalna długość to *n*

- text - zmienna długość znaków nieograniczona ilość

Gdy długość większa od char, varchar to w *insert* i *update* zostanie zgłoszony błąd, chyba że nadmiarowe to spacje. W takim przypadku zostaną obcięte.

Maksymalny rozmiar tekstu, który można przechować wynosi 1GB, co jest maksymalnym rozmiarem kolumny.

Char i varchar dla ciągów o stałej długości zajmują taką samą ilość miejsca, w przypadku zmiennej długości to char zajmuje więcej miejsca bo uzupełnia miejsce spacjami.

Nie ma różnicy w wydajności między typami tekstowymi.

Typy daty i czasu:
- timestamp without timezone - data i czas bez strefy czasowej

- timestamp with timezone - data i czas z strefą czasową

- date - data kalendarzowa rok, miesiąc, dzień

- time without timezone - czas w ciągu dnia bez strefy czasowej

- time with timezone - czas w ciągu dnia ze strefą czasową

- interval - przedział czasu, porównanie 2 czasów

Ustawienia: timezone, datastyle

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


### GUI
[LINK](https://www.pgadmin.org/download/pgadmin-4-apt/)
####
 Setup the repository
####

#### Install the public key for the repository (if not done previously):
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

#### Create the repository configuration file:
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

####
#### Install pgAdmin
####

#### Install for both desktop and web modes:
sudo apt install pgadmin4

#### Install for desktop mode only:
sudo apt install pgadmin4-desktop

#### Install for web mode only:  zainstaluj
sudo apt install pgadmin4-web 

#### Configure the webserver, if you installed pgadmin4-web:
sudo /usr/pgadmin4/bin/setup-web.sh


# Widoki

Widok to nazwana kwerenda lub osłona wokół instrukcji *SELECT*

Widoki są podstawowym elementem relacyjnych baz danych, które można porównać do metod w klasach UML

Jesteśmy wstanie dodawać, usuwać wiersze widoku.

Widoki upraszczają zapytania i zwiększanią modularność kodu

Korzyśći widoków:
- uproszczenie złożonych zapytań
- poprawa wydajności dzięki buforowaniu wyników
- redukcja ilości kodu SQL
- integracja z językami obiektowymi dzięki widokom aktualizowanym
- zastosowanie mechanizmów autoryzacji na poziomie wiersza
- łatwe prowadzenie zmian bez koniecznosci wdrażania nowego oprogramowania
- implementacja warstwy abstrakcji między bazą danych a aplikacjami wysokopoziomowymi

Różnice od procedów składowanych

ich zależności są utrzymywane w bazie danych. są bardziej wydajne. modyfikacja widoku może być zabroniona z powodu efektu kaskadowych

Tworzenie widoku
```
CREATE [OR REPLACE] [TEMP | TEMPORARY] [RECURSIVE] VIEW nazwa_widoku
AS
```

Rodzaje widoków

- tymczasowe : automatycznie usuwane na końcu sesji usera;
~~~~sql
CREATE TEMP VIEW temp_user_view AS
SELECT
    id,
    username,
    email
FROM
    users
WHERE
    active=true;
~~~~
- rekurencyjne obsługują rekurencje podobnie jak funckje w jezykach wysokiego poziomu. dane hierarchiczne
```sql
SELECT RECURSIVE VIEW employee(employee_id,employee_name,manager_id)
(
    --poziom bazowy
    SELECT
        id AS employee_id,
        1 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    --poziom rekurencyjny: pracownicy podlegli przełożonym
    SELECT
        e.id AS employee_id,
        e.name AS employee_name,
        e.manager_id,
        eh.level +1
    FROM employee e
    JOIN employee_hierarchy eh
    ON e.manager_id = eh.employee_id
);
```

- Aktualizowane widoki (materializowane) - przechowuja fizycznie dane w tabelach i mogą być okresowo odświeżane. Używane w dużych i czesto wykonywanych zapytan
```sql
CREATE MATERIALIZE VIEW nazwa_widoku
AS
...
;
REFRESH MATERIALIZED VIEW nazwa_widoku;
``
Aby usunąć widok z zależnościami
```sql
DROP VIEW nazwa_widoku_zaleznego;
DROP VIEW nazwa_widoku_pierwotnego;


DROP VIEW nazwa_widoku CASCADE  -- usuwa odrazu widok pierwotny
```

widoki materializowane mają możliwość automatycznego aktualizoanie, co oznacza ze mozna robic INSERT UPDATE DELEE

warunki dla aktualizowanych widoków:
- oparty na tabeli
- brak: distinct, with, group by, offset, having, limit, union, except, intersect

## Widok edytowalny - pozwala edycje danych
```sql
CREATE VIEW editable_view_customers AS
SELECT id,username,email,balance,is_actibe
FROM accounts
WHERE is_active = TRUE AND balance >0
WITH LOCAL CHECK OPTION;
```
## WIDOK TYLKO DO ODCZYTU
```sql
CREATE VIEW readonly_view_customers AS
SELECT DISTINCT id,username,email,balance,is_actibe
FROM accounts
WHERE balance =0;
```
## WIDOK ZMIATERIALIZOWANY
``
``
# INDEKSY
obiekty fizyczne przyspieszające odczyt danych
- optymalizacja wydajnosci zapytan
- weryfikacja ograniczeń tj. UNIQUE

indeksy można tworzyć na tabeli lub na widoku

Indeks unikalny CREATE UNIQUE INDEX nazwa ON nazwa_tabeli

`index scan` możemy uzyc dzieki indeksowi aby zoptymalizowac wyszukiwanie zamiast wykonywac pelne skanowanie tabeli

plan wykonania `EXPLAIN`  select powoduje wyswietlenie `query plan` w terminalu

TYPY INDEKSÓW
- unikalny
- B-tree (domyślny) drzewo zbilansowane, gdy operacje porównawcze
- Hash Index - do obsługi równości,choć b-tree zwykle spełnia te potrzeby, ale nie są transakcyjnie bezpieczne i nie są replikowane w węzłach slave podczas replikacji.
- GIN (generalized inverted index)-odwrócony, przydatny gdy wiele wartosci zlozonych musi byc mapowanych na jeden wiersz np. tablice, json. Zastosowanie tablice, wyszukiwanie pełnotekstowe
- GiST (generalized search tree) - dla zrównoważonych struktur drzewiastych. Zastosowanie: typy geometryczne, wyszukiwanie pełnotekstowe, wyszukiwanie przestrzenne
- BRIN (Block Range Index) - orzydatny do duzych tabel, gdzie dane uporzadkowane. Jest wolniejszy od b-tree ale jest mniejszu. Zastosowanie: przechowywanie danych na dużą skalę.

Indeksy częściowe
obejmuje tylko podzbiówr danych w tabeli (po where)
taki indeks zmiejsza rozmiar indeksu

indeksy moga byc tworzone na wynikach wyrazen i funkcji.(konwersja typów danych)

