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
_https://www.postgresql.org/docs/current/role-attributes.html_

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


Ustawienia są zawarte w  *pg_settings*

Paramentry ustwawień
- Boolean(wartości logiczne)

- Integer (wartość całkowita)

- Enum (wartości wyliczeniowe)

- Floating Point (wartości zmiennoprzecinkowe)

- String (ciąg znaków) np. ścieżka

Ustwanienia kontekstu
w jaki sposób będziemy zmieniać wartości

- Internal(wewnętrzy) Nie można zmieniać bezpośrednio

- Postmaster        Zmiana parametrów wiąże się z restartem postgres

- Sighup            Trzeba wysłać sygnał po zmianie do procesu

- Backend           Nie wymaga restartu i od razu powinny działać

- Superuser         Przez komendę set, będą działać cały czas 

- User              W trakcie działanie bieżącej sesji

```SET``` i ```SHOW``` służą do zmiany i sprawdzania wartości parametrów ustawień

Zmiana w *postgresql.conf* ma efekt globalny

Przeładowanie konfiguracji ```SELECT pg_reload_conf();```
