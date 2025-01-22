# Procedury (ang. Procedures) w PostgreSQL to funkcje, które umożliwiają wykonywanie zadań bezpośrednio na serwerze, często w kontekście modyfikacji danych. Są one wprowadzone od wersji PostgreSQL 11 jako rozszerzenie funkcjonalności w stosunku do funkcji (functions). Główna różnica między procedurami a funkcjami polega na tym, że procedury mogą wykonywać transakcje, a funkcje nie.

```sql

CREATE PROCEDURE nazwa_procedury (parametry)
LANGUAGE język
AS $$
-- ciało procedury
$$;
```
nazwa_procedury – nazwa procedury.
parametry – lista parametrów, np. param_name typ [IN | OUT | INOUT].
IN: Domyślny typ, parametr wejściowy.
OUT: Parametr wyjściowy.
INOUT: Parametr wejściowo-wyjściowy.
język – język, w którym procedura jest napisana (np. plpgsql, sql).


1. Prosta procedura bez parametrów
sql
Kopiuj
Edytuj
```sql
CREATE PROCEDURE bez_parametrow()
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE 'To jest prosta procedura bez parametrów.';
END;
$$;
CALL bez_parametrow();

```
2. Procedura z parametrami wejściowymi


```sql
CREATE PROCEDURE wstaw_klienta(imie TEXT, nazwisko TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO klienci (imie, nazwisko) VALUES (imie, nazwisko);
    RAISE NOTICE 'Dodano klienta: % %', imie, nazwisko;
END;
$$;
CALL wstaw_klienta('Jan', 'Kowalski');

```


3. Procedura z parametrem wyjściowym

```sql
CREATE PROCEDURE pobierz_sume_zamowien(IN klient_id INT, OUT suma NUMERIC)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT SUM(kwota) INTO suma
    FROM zamowienia
    WHERE klient_id = klient_id;
END;
$$;
CALL pobierz_sume_zamowien(1, suma);
-- zmienna suma przechowuje wynik

```


Transakcje w procedurach: Procedury mogą zarządzać transakcjami (np. za pomocą COMMIT lub ROLLBACK), co jest ich główną przewagą nad funkcjami.

Przykład:
```sql
CREATE PROCEDURE zarzadzaj_transakcjami()
LANGUAGE plpgsql
AS $$
BEGIN
    BEGIN
        INSERT INTO produkty (nazwa) VALUES ('Produkt A');
        COMMIT;
    EXCEPTION WHEN OTHERS THEN
        ROLLBACK;
    END;
END;
$$;

```