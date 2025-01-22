Podstawowa składnia obsługi wyjątków
sql
Kopiuj
Edytuj
BEGIN
    -- Kod, który może powodować wyjątki
EXCEPTION
    WHEN <typ wyjątku> THEN
        -- Kod obsługujący wyjątek
END;
Typowe wyjątki:

WHEN OTHERS – obsługuje wszystkie błędy.
WHEN unique_violation – łapie błędy związane z unikalnymi ograniczeniami (UNIQUE).
WHEN foreign_key_violation – łapie błędy naruszenia klucza obcego.
WHEN division_by_zero – łapie błędy dzielenia przez zero.

```sql
CREATE PROCEDURE wstaw_klienta(imie TEXT, nazwisko TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    BEGIN
        INSERT INTO klienci (imie, nazwisko) VALUES (imie, nazwisko);
    EXCEPTION
        WHEN unique_violation THEN
            RAISE NOTICE 'Klient o nazwisku % już istnieje!', nazwisko;
    END;
END;
$$;

CALL wstaw_klienta('Jan', 'Kowalski');


```



```sql
Wycofywanie transakcji przy błędzie
sql
Kopiuj
Edytuj
CREATE PROCEDURE przetworz_transakcje(imie TEXT, nazwisko TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    BEGIN
        -- Rozpocznij transakcję
        INSERT INTO klienci (imie, nazwisko) VALUES (imie, nazwisko);
        INSERT INTO zamowienia (klient_id, wartosc) 
        VALUES (currval('klienci_id_seq'), 100);
        COMMIT;
    EXCEPTION
        WHEN OTHERS THEN
            ROLLBACK;
            RAISE NOTICE 'Transakcja została wycofana: %', SQLERRM;
    END;
END;
$$;

CALL przetworz_transakcje('Jan', 'Kowalski');

```


. Obsługa konkretnego wyjątku i jego przechwycenie
Możesz przechwycić konkretne wyjątki i podjąć różne działania.
```sql

CREATE PROCEDURE podziel_liczby(a NUMERIC, b NUMERIC, OUT wynik NUMERIC)
LANGUAGE plpgsql
AS $$
BEGIN
    BEGIN
        wynik := a / b;
    EXCEPTION
        WHEN division_by_zero THEN
            RAISE NOTICE 'Nie można dzielić przez zero.';
            wynik := NULL; -- Możesz przypisać wartość domyślną
    END;
END;
$$;
CALL podziel_liczby(10, 0, wynik);
-- Wynik: NULL

```