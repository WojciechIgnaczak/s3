# Widoki

Widok to nazwana kwerenda lub osłona wokół instrukcji *SELECT*

Widoki są podstawowym elementem relacyjnych baz danych, które można porównać do metod w klasach UML

Jesteśmy wstanie dodawać, usuwać wiersze widoku.

Widoki upraszczają zapytania i zwiększanią modularność kodu

## Korzyśći widoków:
- uproszczenie złożonych zapytań
- poprawa wydajności dzięki buforowaniu wyników
- redukcja ilości kodu SQL
- integracja z językami obiektowymi dzięki widokom aktualizowanym
- zastosowanie mechanizmów autoryzacji na poziomie wiersza
- łatwe prowadzenie zmian bez koniecznosci wdrażania nowego oprogramowania
- implementacja warstwy abstrakcji między bazą danych a aplikacjami wysokopoziomowymi

Różnice od procedów składowanych

ich zależności są utrzymywane w bazie danych. są bardziej wydajne. modyfikacja widoku może być zabroniona z powodu efektu kaskadowych

## Tworzenie widoku
```sql
CREATE [OR REPLACE] [TEMP | TEMPORARY] [RECURSIVE] VIEW nazwa_widoku
AS
```

## Rodzaje widoków

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
CREATE RECURSIVE VIEW employee_hierarchy AS
-- Poziom bazowy: pracownicy bez przełożonych
SELECT id AS employee_id, name AS employee_name, manager_id
FROM employees
WHERE manager_id IS NULL
UNION ALL
-- Poziom rekurencyjny: pracownicy podlegli przełożonym
SELECT e.id AS employee_id, e.name AS employee_name, e.manager_id
FROM employees e
JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id;

```

- Aktualizowane widoki (materializowane) - przechowuja fizycznie dane w tabelach i mogą być okresowo odświeżane. Używane w dużych i czesto wykonywanych zapytan
```sql
CREATE MATERIALIZED VIEW sales_summary AS
SELECT product_id, SUM(quantity) AS total_sales
FROM sales
GROUP BY product_id;

...

REFRESH MATERIALIZED VIEW nazwa_widoku;
```
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
## Widok tylko do odczytu
```sql
CREATE VIEW readonly_view_customers AS
SELECT DISTINCT id,username,email,balance,is_actibe
FROM accounts
WHERE balance =0;
```