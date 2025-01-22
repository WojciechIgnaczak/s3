Teoria transakcji
Transakcje to fundamentalny mechanizm baz danych umożliwiający wykonywanie zestawu operacji jako jednej, niepodzielnej całości. W PostgreSQL transakcje są zgodne z modelem ACID:

Atomicity (Atomowość): Wszystkie operacje w transakcji są wykonywane albo w całości, albo wcale.
Consistency (Spójność): Po zakończeniu transakcji baza danych pozostaje w stanie spójnym.
Isolation (Izolacja): Operacje jednej transakcji są izolowane od innych, nawet jeśli są wykonywane równocześnie.
Durability (Trwałość): Po zatwierdzeniu transakcji jej efekty są trwałe, nawet w przypadku awarii systemu.
Komendy transakcyjne w PostgreSQL
BEGIN: Rozpoczyna transakcję.
COMMIT: Zatwierdza zmiany wykonane w transakcji.
ROLLBACK: Wycofuje zmiany wykonane w transakcji.
SAVEPOINT: Tworzy punkt kontrolny w obrębie transakcji, do którego można wrócić.
ROLLBACK TO SAVEPOINT: Wycofuje zmiany do wskazanego punktu kontrolnego.
END: Tożsame z COMMIT.
Podstawowe przykłady transakcji
Przykład 1: Prosta transakcja
sql
Kopiuj
Edytuj
BEGIN;

INSERT INTO accounts (id, balance) VALUES (1, 1000);
UPDATE accounts SET balance = balance - 200 WHERE id = 1;
INSERT INTO transactions (account_id, amount) VALUES (1, -200);

COMMIT;
Opis:

Transakcja dodaje nowe konto, zmniejsza jego saldo i rejestruje transakcję w dzienniku.
Jeśli jedna z operacji się nie powiedzie, zmiany zostaną anulowane.
Przykład 2: Wycofanie transakcji
sql
Kopiuj
Edytuj
BEGIN;

INSERT INTO accounts (id, balance) VALUES (2, 500);
UPDATE accounts SET balance = balance - 600 WHERE id = 2; -- powoduje błąd, brak wystarczających środków

ROLLBACK;
Opis:

Operacja aktualizacji salda powoduje błąd, dlatego cała transakcja jest wycofywana.
Przykład 3: Punkt kontrolny w transakcji
sql
Kopiuj
Edytuj
BEGIN;

INSERT INTO accounts (id, balance) VALUES (3, 1000);

SAVEPOINT sp1;

UPDATE accounts SET balance = balance - 300 WHERE id = 3;

ROLLBACK TO SAVEPOINT sp1;

COMMIT;
Opis:

Punkt kontrolny pozwala cofnąć część zmian, bez anulowania całej transakcji.
Zaawansowane zastosowania
1. Obsługa równoczesnych transakcji
PostgreSQL obsługuje izolację transakcji na czterech poziomach:

Read Uncommitted
Read Committed (domyślny w PostgreSQL)
Repeatable Read
Serializable
sql
Kopiuj
Edytuj
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

BEGIN;

SELECT balance FROM accounts WHERE id = 1;

-- W międzyczasie inna transakcja zmienia saldo

COMMIT;
Opis:

Poziom izolacji REPEATABLE READ gwarantuje, że wynik zapytania nie zmieni się w ramach jednej transakcji, nawet jeśli inna transakcja modyfikuje dane.
2. Użycie transakcji w procedurach
sql
Kopiuj
Edytuj
CREATE OR REPLACE FUNCTION transfer_funds(from_account INT, to_account INT, amount NUMERIC)
RETURNS VOID AS $$
BEGIN
    BEGIN;

    UPDATE accounts SET balance = balance - amount WHERE id = from_account;
    UPDATE accounts SET balance = balance + amount WHERE id = to_account;

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE NOTICE 'Transfer failed';
END;
$$ LANGUAGE plpgsql;
Opis:

Funkcja transferuje środki między kontami, korzystając z transakcji, aby zapewnić spójność.