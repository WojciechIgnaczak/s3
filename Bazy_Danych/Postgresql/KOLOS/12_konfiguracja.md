# Konfiguracja
## Ustawnianie ilości połączeń do bazy dla roli
Tworzenie roli z ograniczeniem liczby jednoczesnych połączeń dla tej roli.
```sql
CREATE ROLE name CONNECTION LIMIT 10;
```

## Ustawianie globalnego limitu połączeń
```sql
SHOW config_file; -- pokazuje ścieżkę do pliku 
-- w pliku postresql.conf zmień
max_connections = 100

```

## Ustawianie limitu połączeń dla bazy danych
```sql
ALTER DATABASE nazwa_bazy CONNECTION LIMIT 50; -- ustawienie limitu dla bazy
SELECT datname, datconnlimit FROM pg_database; -- sprawdzenie bieżącego limitu
```
### Tabele katalogowe *pg_catalog*
Zwykłe tabele na których możemy używać `SELECT`,`UPDATE`,`DELETE`. Nie zaleca się modyfikacji ręcznej, chyba że w wyjątkowych sytuacjach.

```sql
SELECT datconnlimit FROM pg_database WHERE datname="nazwa_bazy";        // wyświetlenie limitu połączeń z bazą danych
ALTER DATABASE nazwa_bazy CONNECTION LIMIT 1                            //zmiana limitu połączeń na 1. -1 dla wszystkich
UPDATE pg_database SET dataconnlimit=-1 WHERE datname='nazwa_bazy';     //nie zalecania zmiana limitu połączeń, ponieważ  przy nieprawidłowej wartości nie wyrzuca błędu np. "-2"
```

# Plik postresql.conf
- można zmienić port - domyślny 5432
- maksywalną liczbę połączeń - domyślnie 100
- adresy IP, na których serwer nasłuchuje połączeń (listen_addresses)
- logowanie i monitorowanie (zbieranie logów, katalog z logami, nazwa plików logów, rejestrowanie zapytań sql)
- zarządzanie transakcjami (domyślny poziom izolacji transakcji)
- bezpieczeństwo (metoda szyfrowanai haseł, włączenie połączeń szyfrowanych)

# Plik pg_hba.conf
- rodzaje połączenia
    -local  - połączenie lokalne
    -host   - połączenie przez TCP/IP
    -hostssl    - połączenie przez TCP/IP wymagające SSL
- adres
    - adres IP klienta lub zakres adresów

- nazwa-bazy
    - all wszystkie bazy

- metoda uwierzetylnienia
    - trust - bez uwierzetylnienia
    - md5   - hasło szyfrowane md5
    - password  -uwierzytelnienie za pomocą hasła w tekście
    - peer  - uwierzytenienie przez porównanie nazwy usera systemowego
    - scram-sha-256 - hasło w formacie sha256
    - reject    - odrzucenie połączenia
    - cert  - certyfikat klienta SSL

# Plik pg_catalog
`pg_catalog` to systemowy schemat w PostgreSQL, który zawiera wbudowane tabele i widoki systemowe. Jest to integralna część bazy danych PostgreSQL i przechowuje metadane dotyczące struktury bazy danych, takie jak informacje o tabelach, kolumnach, indeksach, funkcjach, a także o uprawnieniach i konfiguracjach.

# Ustawnienia PostgreSQL 
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
