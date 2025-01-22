riggery w PostgreSQL – Kompletne wprowadzenie
Triggery (wyzwalacze) w PostgreSQL to mechanizmy, które automatycznie wykonują określoną akcję w reakcji na zdarzenia związane z modyfikacją danych w tabelach lub widokach. Mogą być wykorzystywane do zapewnienia integralności danych, automatyzacji pewnych działań lub audytowania zmian.

Cechy triggerów
Zdarzenia: Triggery można uruchamiać na zdarzeniach takich jak:
INSERT – gdy wiersz jest wstawiany do tabeli.
UPDATE – gdy wiersz jest modyfikowany.
DELETE – gdy wiersz jest usuwany.
Czas uruchomienia:
BEFORE – przed wykonaniem operacji (możliwość zmiany wiersza).
AFTER – po wykonaniu operacji.
INSTEAD OF – zamiast wykonania operacji (stosowane dla widoków).
Zakres: Można określić, czy trigger działa na:
KAŻDY WIERSZ (FOR EACH ROW) – uruchamiany dla każdego wiersza zmienionego przez zdarzenie.
CAŁĄ OPERACJĘ (FOR EACH STATEMENT) – uruchamiany raz dla całego polecenia.
Tworzenie triggera
Aby stworzyć trigger, konieczne są dwa kroki:

Utworzenie funkcji, którą trigger będzie wywoływał.
Utworzenie samego triggera przypisanego do tabeli lub widoku.
Przykład 1: Logowanie zmian w tabeli
Krok 1: Tworzenie funkcji PL/pgSQL
sql
Kopiuj
Edytuj
```sql
CREATE OR REPLACE FUNCTION log_changes()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO logs (table_name, operation, changed_at)
  VALUES (TG_TABLE_NAME, TG_OP, CURRENT_TIMESTAMP);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```
Krok 2: Tworzenie triggera
sql
Kopiuj
Edytuj
```sql
CREATE TRIGGER after_update_trigger
AFTER INSERT OR UPDATE OR DELETE
ON my_table
FOR EACH ROW
EXECUTE FUNCTION log_changes();
```
Dostępne zmienne w triggerach
Podczas działania triggera dostępne są specjalne zmienne:

NEW – nowa wartość wiersza (dostępna w INSERT i UPDATE).
OLD – poprzednia wartość wiersza (dostępna w UPDATE i DELETE).
TG_TABLE_NAME – nazwa tabeli, na której działa trigger.
TG_OP – operacja, która uruchomiła trigger (INSERT, UPDATE, DELETE).
Przykłady zaawansowane
1. Automatyczna aktualizacja znacznika czasu (updated_at)
sql
Kopiuj
Edytuj
```sql
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_updated_at
BEFORE UPDATE
ON my_table
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

```
2. Zapobieganie usunięciu ważnych danych
sql
Kopiuj
Edytuj
```sql
CREATE OR REPLACE FUNCTION prevent_deletion()
RETURNS TRIGGER AS $$
BEGIN
  IF OLD.is_important THEN
    RAISE EXCEPTION 'Nie można usunąć ważnego rekordu!';
  END IF;
  RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER no_delete_important
BEFORE DELETE
ON my_table
FOR EACH ROW
EXECUTE FUNCTION prevent_deletion();
```
Modyfikacja i usuwanie triggerów
Modyfikacja funkcji: Funkcji przypisanej do triggera nie można zmienić. Należy usunąć i ponownie stworzyć trigger.
Usuwanie triggera:
sql
Kopiuj
Edytuj
```sql
DROP TRIGGER trigger_name ON table_name;
sql