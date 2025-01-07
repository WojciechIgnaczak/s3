# INDEKSY
obiekty fizyczne przyspieszające odczyt danych
- optymalizacja wydajnosci zapytan
- weryfikacja ograniczeń tj. UNIQUE

indeksy można tworzyć na tabeli lub na widoku

Indeks unikalny CREATE UNIQUE INDEX nazwa ON nazwa_tabeli

`index scan` możemy uzyc dzieki indeksowi aby zoptymalizowac wyszukiwanie zamiast wykonywac pelne skanowanie tabeli

plan wykonania `EXPLAIN`  select powoduje wyswietlenie `query plan` w terminalu

TYPY INDEKSÓW
- unikalny Indeks zapewniający unikalność wartości w kolumnach.	Zapewnienie unikalności danych w kolumnach, często używane dla kolumn PRIMARY KEY i UNIQUE.

```sql
CREATE UNIQUE INDEX idx_unique_example ON tabela_name (kolumna_name);

```
- B-tree (domyślny) drzewo zbilansowane, gdy operacje porównawcze. Zapytania z operatorami porównania (np. =, <, >, <=, >=, BETWEEN, IN). Idealny do indeksowania liczb, dat i tekstów.
```sql
CREATE INDEX idx_btree_example ON tabela_name (kolumna_name);

```

- Hash Index - Indeks oparty na funkcji skrótu (hash).	do obsługi równości,choć b-tree zwykle spełnia te potrzeby, ale nie są transakcyjnie bezpieczne i nie są replikowane w węzłach slave podczas replikacji.
```sql
CREATE INDEX idx_hash_example ON tabela_name USING HASH (kolumna_name);

```

- GIN (generalized inverted index)-Indeks odwrócony, używany do złożonych struktur danych (tablice, JSONB).	, przydatny gdy wiele wartosci zlozonych musi byc mapowanych na jeden wiersz np. tablice, json. Zastosowanie tablice, wyszukiwanie pełnotekstowe.
```sql
CREATE INDEX idx_gin_example ON tabela_name USING GIN (kolumna_name);

```

- GiST (generalized search tree) - dla zrównoważonych struktur drzewiastych. Zastosowanie: typy geometryczne, wyszukiwanie pełnotekstowe, wyszukiwanie przestrzenne
```sql
CREATE INDEX idx_gist_example ON tabela_name USING GiST (kolumna_name);

```

- BRIN (Block Range Index) - przydatny do duzych tabel, gdzie dane uporzadkowane. Indeks na zakresach bloków danych. Jest wolniejszy od b-tree ale jest mniejszu. Zastosowanie: przechowywanie danych na dużą skalę.
```sql
CREATE INDEX idx_brin_example ON tabela_name USING BRIN (kolumna_name);

```

- SP-GiST -Indeks podzielony przestrzennie, przeznaczony do danych przestrzennych.	Indeksowanie danych, które są podzielone przestrzennie (np. punkty w przestrzeni). Idealny dla danych o rozproszonej strukturze.
```sql
CREATE INDEX idx_spgist_example ON tabela_name USING SPGiST (kolumna_name);

```
- Partial Index -Indeks na wybranych danych, spełniających określony warunek. Indeksowanie tylko części danych w tabeli, które spełniają określony warunek (np. tylko wartości większe niż 100).
```sql
CREATE INDEX idx_partial_example ON tabela_name (kolumna_name) WHERE kolumna_name > 100;

```

- Expression Index- Indeks tworzony na wyrażeniu lub funkcji.Przyspiesza zapytania, które operują na funkcjach lub wyrażeniach (np. LOWER(my_column)), a nie na samej kolumnie.
```sql
CREATE INDEX idx_expression_example ON tabela_name (LOWER(kolumna_name));

```

- Foreign Key Index- Indeks tworzony dla kolumny klucza obcego.Używany do poprawy wydajności operacji JOIN oraz zapewnienia integralności referencyjnej między tabelami.
```sql
CREATE INDEX idx_fk_example ON tabela_name (kolumna_name);

```