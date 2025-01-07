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