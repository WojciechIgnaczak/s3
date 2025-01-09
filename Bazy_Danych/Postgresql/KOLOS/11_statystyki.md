# Statystyka
## 1. Wyświetlanie statystyk tabeli
Aby wyświetlić statystyki dla tabeli, można użyć polecenia:

Skopiuj kod
`\d+ nazwa_tabeli`
To polecenie wyświetli dodatkowe informacje o tabeli, w tym statystyki związane z jej kolumnami, takie jak liczba wierszy i indeksów.

## 2. Wyświetlanie statystyk kolumny
Możesz sprawdzić statystyki dla poszczególnych kolumn, np.:

```sql
SELECT * FROM pg_stats WHERE tablename = 'nazwa_tabeli';
```
W wynikach zobaczysz dane dotyczące kolumny, takie jak:

`n_distinct`: szacowana liczba unikalnych wartości w kolumnie.
`most_common_values (MCV)`: najczęściej występujące wartości w kolumnie.
`null_frac`: udział wartości NULL.
`avg_width`: średnia szerokość kolumny.
## 3. Wyświetlanie rozszerzonych statystyk
Aby zobaczyć rozszerzone statystyki, które mogą zawierać informacje o zależnościach między kolumnami, użyj polecenia:

`\dX`
Rozszerzone statystyki mogą obejmować:

`Schema`: Schemat, w którym znajdują się statystyki.
`Name`: Nazwa obiektu rozszerzonych statystyk.
`Definition`: Definicja wyrażenia statystyki.
`Ndistinct`: Liczba unikalnych wartości.
`Dependencies`: Zależności od innych obiektów.
## 4. Zbieranie statystyk
Aby zebrać (lub zaktualizować) statystyki w bazie danych, użyj polecenia:

```sql
ANALYZE
```
To polecenie zbiera statystyki dla wszystkich tabel w bazie danych lub dla pojedynczej tabeli:

```sql
ANALYZE nazwa_tabeli;
```
Proces zbierania statystyk jest używany przez planistę zapytań do optymalizacji wykonania zapytań.

## 5. Podstawowe informacje o statystykach w bazie
Aby wyświetlić ogólne informacje o tabelach, ich statystykach, a także inne szczegóły, możesz skorzystać z zapytania do systemowych tabel, np.:


```sql
SELECT * FROM pg_stat_user_tables;
```
To zapytanie zwróci informacje o statystykach użytkownika, takie jak liczba odczytów i zapisów w tabelach.

## 6. Sprawdzanie wydajności zapytań
Aby zbierać informacje o wydajności zapytań (np. czas wykonania), włącz statystyki zapytań:


```sql
SET track_activities = true;
```
Następnie możesz sprawdzić aktywność zapytań:


```sql
SELECT * FROM pg_stat_activity;
```
## 7. Wyświetlanie statystyk indeksów
Aby uzyskać informacje o indeksach w bazie danych, użyj polecenia:

`\di`
Możesz także zapytać o szczegóły dotyczące indeksów w systemowej tabeli:

```sql
SELECT * FROM pg_indexes WHERE tablename = 'nazwa_tabeli';
```
Te polecenia pozwolą Ci monitorować, analizować i optymalizować wydajność zapytań w PostgreSQL za pomocą statystyk.