# Podstawa
# Tworzenie bazy danych
```sql
CREATE ROLE car_portal_role LOGIN;

CREATE DATABASE car_portal
    WITH 
    ENCODING 'UTF8'
    LC_COLLATE 'en_US.UTF-8'
    LC_CTYPE 'en_US.UTF-8'
    OWNER car_portal_role;
```

# Tabele
`CREATE TABLE`

Mają 4 różne typy. Są dedykowane do konkretnych zadań. Jest możliwość klonowania zadań.

Materializacja wyników przez `SELECT`.

Tabele trwałe - zwykłe tabele, cykl od utworzenia do usunięcia
```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100)
);

```

Tabele tymczasowe - tabele, cykl życia to sesja użytkownika.
```sql
CREATE TEMPORARY TABLE temp_employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100)
);

```
Tabele bez logowanie *unlogged* - szybsze niż tabele trwałe, dane nie są zapisywane do plików WAL. Nie są odporne na awarie i nie mogą być replikowane na węzeł podrzędny
```sql
CREATE UNLOGGED TABLE my_unlogged_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

```
Tabele podrzędne - tabela, która dziedziczy jedną lub więcej tabel. Dziedzizenie jest często używane z wykluczeniem ograniczeń (constraint exclusion) w celu fizycznego partycjonowania danych na dysku twardym.W PostgreSQL można utworzyć tabelę nadrzędną (partycjonowaną) i następnie utworzyć tabele podrzędne.

```sql
-- Tabela nadrzędna (partycjonowana):
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    sale_date DATE,
    amount DECIMAL
) PARTITION BY RANGE (sale_date);

-- Tabele podrzędne
CREATE TABLE sales_2020 PARTITION OF sales
    FOR VALUES FROM ('2020-01-01') TO ('2020-12-31');

CREATE TABLE sales_2021 PARTITION OF sales
    FOR VALUES FROM ('2021-01-01') TO ('2021-12-31');

```


1. CHECK Constraint:
Constraint CHECK w PostgreSQL pozwala na ograniczenie wartości w tabeli, na przykład do zakresu, określonego wzorca lub spełniającego określony warunek. Można go stosować do jednej lub wielu kolumn.

Przykład: CHECK dla zakresu wartości
Załóżmy, że masz tabelę z danymi o pracownikach i chcesz upewnić się, że pensja nie przekracza określonego limitu (np. 10000):



CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    salary NUMERIC CHECK (salary >= 3000 AND salary <= 10000)
);
Przykład: CHECK z wyrażeniem regularnym
Walidacja numeru telefonu w formacie (XXX) XXX-XXXX:




CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    CONSTRAINT valid_phone CHECK (phone ~ '^\(\d{3}\) \d{3}-\d{4}$')
);
Przykład: CHECK z wieloma warunkami
Złożony warunek, który sprawdza, czy wiek osoby jest w określonym zakresie (np. między 18 a 65):




CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    CONSTRAINT valid_age CHECK (age BETWEEN 18 AND 65)
);

2. ENUM Types:
Typ ENUM w PostgreSQL pozwala na stworzenie typu danych, który ma ograniczoną liczbę dozwolonych wartości. Jest to przydatne, gdy masz kolumnę, która przyjmuje tylko kilka określonych wartości (np. statusy, role).

Przykład: Tworzenie typu ENUM
Stwórzmy typ status, który przyjmuje wartości 'active', 'inactive', 'suspended':

sql
Kopiuj
Edytuj
CREATE TYPE status AS ENUM ('active', 'inactive', 'suspended');