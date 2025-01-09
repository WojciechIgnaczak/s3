# PL/pgSQL Function
PL/pgSQL to proceduralny język programowania umożliwiający rozszerzenie funkcjonalności PostgreSQL poprzez tworzenie funkcji,procedur,wyzwalaczy.

PL/pgSQL umożliwia:
- tworzenie funkcji i procedur z wykorzystaniem logiki proceduralnej
- definiowanie zmiennych lokalnych
- obsługa wyjątków
- użycie pętli, instrukcji warunkowych

## Instalacja PL/pgSQL

```sql
CREATE EXTEMSION IF NOT EXISTS plpgsql;
```

## Elementy funkcji
określa typ zwracanej funkcji
blok kodu z logiką
instrukcja która określa watość zwracaną przez funckje
język w ktorym jest napisana funckja

## Przykładowe funkcje
```sql
CREATE OR REPLACE FUNCTION example_function() RETURNS TEXT AS $$
BEGIN
    RETURN 'HELLO';
END;
$$ LANGUAGE plpgsql;
```

```sql
CREATE OR REPLACE FUNCTION add_number(a INT, b INT) RETURNS INT AS $$
BEGIN
    RETURN a+b;
END;
$$ LANGUAGE plpgsql;

SELECT add_number(10,30);
-- 40
```

```sql
CREATE OR REPLACE FUNCTION get_all_users() RETURNS TABLE(user_id INT, user_name TEXT) AS $$
BEGIN
    RETURN QUERY SELECT id,name FROM users;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_all_users();
```
#### Funkcje z wyjątkami
```sql
CREATE OR REPLACE FUNCTION calcuate_tax(price NUMERIC, tax_rate NUMERIC DEFAULT 23) 
RETURNS NUMERIC AS $$
BEGIN
    IF b=0 THEN
        RETURN NULL;
    ELSE
        RETURN a/b;
    END IF;
END;
$$ LANGUAGE plpgsql;
```

### Best practies
- dokładne określenie typów danych parametrów i wartości zwracanych
- obaługa wyjątków EXCEPTION
- unikanie ciężkich operacji- powinny być zoptymalizowane i unikać długich pętli
- testowanie funkcji z różnymi zestawami danych
- uważać na rekursje 
- uważać na operacje zmieniające dane
- uważać na nieefektywne zapytania w pętlach

# JĘZYKI PLSQL
- SQL       proste operacje,łatwe
- PL/pgSQL  logika,pętle warunki
- C         wymaga kompilacji, wysoka wydajność
- PL/Python ogromne korzyści, numpy,pandas język plpython3u
- PL/Perl   elastyczny do manipulacji tekstu i operacji na ciągach znaków
- PL/Tcl    do wykonywania operacji proceduralnych rzadko używany
- PL/V8 PL/JavaSript    S
- PL/R      do analiz statystycznych i wizualizacji danych

Jakie języki
`SELECT lanname AS language, lanpltrusted AS trusted FROM pg_language;`

Jak zainstalowac

```sql
CREATE EXTENSION plpgsql;
CREATE EXTENSION plpython3u;
```