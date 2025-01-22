# Funkcje tekstowe
| Funkcja/Operator                                               | Opis                                                                                                 | Przykład użycia                                                    |
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| `text \|\| text → text`                                          | Łączy dwa ciągi znaków.                                                                               | `'Post' \|\| 'greSQL' → PostgreSQL`                                  |
| `text \|\| anynonarray → text`                                    | Łączy ciąg znaków z innym typem danych, który zostaje przekonwertowany na tekst.                     | `'Value: ' \|\| 42 → Value: 42`                                      |
| `btrim ( string text [, characters text ] ) → text`            | Usuwa najdłuższy ciąg zawierający tylko znaki z `characters` (domyślnie spacje) z początku i końca ciągu. | `btrim('xyxtrimyyx', 'xyz') → trim`                                |
| `text IS [NOT] [form] NORMALIZED → boolean`                    | Sprawdza, czy ciąg jest w określonym formacie normalizacji Unicode.                                   | `U&'\0061\0308bc' IS NFD NORMALIZED → t`                            |
| `bit_length ( text ) → integer`                                | Zwraca liczbę bitów w ciągu (8 razy długość w oktetach).                                              | `bit_length('jose') → 32`                                          |
| `char_length ( text ) → integer`                               | Zwraca liczbę znaków w ciągu.                                                                          | `char_length('josé') → 4`                                          |
| `lower ( text ) → text`                                        | Konwertuje ciąg na małe litery, zgodnie z regułami lokalizacji bazy danych.                          | `lower('TOM') → tom`                                               |
| `lpad ( string text, length integer [, fill text ] ) → text`    | Rozszerza ciąg do długości `length`, dodając `fill` (domyślnie spacje) z lewej strony. Jeśli ciąg jest dłuższy, zostaje przycięty. | `lpad('hi', 5, 'xy') → xyxhi`                                      |
| `ltrim ( string text [, characters text ] ) → text`            | Usuwa najdłuższy ciąg zawierający tylko znaki z `characters` (domyślnie spacje) z początku ciągu.     | `ltrim('zzzytest', 'xyz') → test`                                  |
| `normalize ( text [, form ] ) → text`                          | Konwertuje ciąg do określonej formy normalizacji Unicode.                                             | `normalize(U&'\0061\0308bc', NFC) → U&'\00E4bc'`                    |
| `octet_length ( text ) → integer`                              | Zwraca liczbę bajtów w ciągu.                                                                          | `octet_length('josé') → 5 (jeśli kodowanie serwera to UTF8)`        |
| `octet_length ( character ) → integer`                         | Zwraca liczbę bajtów w ciągu, nie usuwając trailing spaces.                                            | `octet_length('abc '::character(4)) → 4`                            |
| `overlay ( string text PLACING newsubstring text FROM start integer [ FOR count integer ] ) → text` | Zastępuje część ciągu, zaczynając od `start`-tej pozycji i długości `count`, nowym ciągiem.           | `overlay('Txxxxas' placing 'hom' from 2 for 4) → Thomas`            |
| `position ( substring text IN string text ) → integer`         | Zwraca pierwszy indeks wystąpienia `substring` w `string`, lub 0, jeśli nie jest obecny.             | `position('om' in 'Thomas') → 3`                                    |
| `rpad ( string text, length integer [, fill text ] ) → text`    | Rozszerza ciąg do długości `length`, dodając `fill` (domyślnie spacje) z prawej strony. Jeśli ciąg jest dłuższy, zostaje przycięty. | `rpad('hi', 5, 'xy') → hixyx`                                      |
| `rtrim ( string text [, characters text ] ) → text`            | Usuwa najdłuższy ciąg zawierający tylko znaki z `characters` (domyślnie spacje) z końca ciągu.        | `rtrim('testxxzx', 'xyz') → test`                                  |
| `substring ( string text [ FROM start integer ] [ FOR count integer ] ) → text` | Wyciąga podciąg z `string`, zaczynając od `start`-tej pozycji i kończąc po `count` znakach.            | `substring('Thomas' from 2 for 3) → hom`                             |
| `substring ( string text FROM pattern text ) → text`           | Wyciąga pierwszy podciąg pasujący do wzorca POSIX regular expression.                                 | `substring('Thomas' from '...$') → mas`                              |
| `substring ( string text SIMILAR pattern text ESCAPE escape text ) → text` | Wyciąga pierwszy podciąg pasujący do wzorca SQL regular expression.                                   | `substring('Thomas' similar '%#"o_a#"_' escape '#') → oma`           |
| `trim ( [ LEADING \| TRAILING \| BOTH ] [ characters text ] FROM string text ) → text` | Usuwa najdłuższy ciąg znaków z początku, końca lub obu stron `string` zawierający tylko znaki z `characters` (domyślnie spacje). | `trim(both 'xyz' from 'yxTomxx') → Tom`                              |
| `unicode_assigned ( text ) → boolean`                          | Zwraca `true`, jeśli wszystkie znaki w ciągu mają przypisane kody Unicode.                             | `unicode_assigned('abc') → true`                                     |
| `upper ( text ) → text`                                        | Konwertuje ciąg na wielkie litery, zgodnie z regułami lokalizacji bazy danych.                        | `upper('tom') → TOM`                                                |





1. LENGTH(string)
Zwraca długość łańcucha znaków.

sql
Kopiuj
Edytuj
SELECT LENGTH('Hello World');  -- Zwraca 11
2. UPPER(string)
Zamienia wszystkie litery w łańcuchu na wielkie litery.

sql
Kopiuj
Edytuj
SELECT UPPER('hello');  -- Zwraca 'HELLO'
3. LOWER(string)
Zamienia wszystkie litery w łańcuchu na małe litery.

sql
Kopiuj
Edytuj
SELECT LOWER('HELLO');  -- Zwraca 'hello'
4. TRIM([LEADING | TRAILING | BOTH] FROM string)
Usuwa białe znaki z początku, końca lub z obu stron łańcucha.

sql
Kopiuj
Edytuj
SELECT TRIM(BOTH FROM '  Hello  ');  -- Zwraca 'Hello'
5. BOTH | LEADING | TRAILING
Parametry do funkcji TRIM, które pozwalają określić, z której strony usuwane są białe znaki:

LEADING – usuwa białe znaki tylko z początku.
TRAILING – usuwa białe znaki tylko z końca.
BOTH – usuwa białe znaki z obu stron.
6. CONCAT(string1, string2, ...)
Łączy kilka łańcuchów znaków w jeden.

sql
Kopiuj
Edytuj
SELECT CONCAT('Hello', ' ', 'World');  -- Zwraca 'Hello World'
7. SUBSTRING(string FROM start FOR length)
Zwraca część łańcucha zaczynając od pozycji start i mając długość length.

sql
Kopiuj
Edytuj
SELECT SUBSTRING('Hello World' FROM 1 FOR 5);  -- Zwraca 'Hello'
8. POSITION(substring IN string)
Zwraca pozycję pierwszego wystąpienia substring w łańcuchu string.

sql
Kopiuj
Edytuj
SELECT POSITION('World' IN 'Hello World');  -- Zwraca 7
9. REPLACE(string, old_substring, new_substring)
Zastępuje wszystkie wystąpienia old_substring w string na new_substring.

sql
Kopiuj
Edytuj
SELECT REPLACE('Hello World', 'World', 'PostgreSQL');  -- Zwraca 'Hello PostgreSQL'
10. REGEXP_REPLACE(string, pattern, replacement)
Zastępuje tekst, który pasuje do wyrażenia regularnego.

sql
Kopiuj
Edytuj
SELECT REGEXP_REPLACE('abc123', '\d', 'X', 'g');  -- Zwraca 'abcXXX'
11. REGEXP_MATCHES(string, pattern)
Sprawdza, czy łańcuch pasuje do wyrażenia regularnego i zwraca wynik.

sql
Kopiuj
Edytuj
SELECT REGEXP_MATCHES('123abc', '^\d+');  -- Zwraca {'123'}
12. STRING_AGG(expression, delimiter)
Łączy wartości z wielu wierszy w jeden łańcuch z określonym separatorem.

sql
Kopiuj
Edytuj
SELECT STRING_AGG(name, ', ') FROM users;  -- Zwraca np. 'Alice, Bob, Carol'
13. TO_CHAR(value, format)
Konwertuje wartość na łańcuch, stosując określony format (np. do konwersji daty lub liczby na tekst).

sql
Kopiuj
Edytuj
SELECT TO_CHAR(current_date, 'YYYY-MM-DD');  -- Zwraca '2025-01-22'
14. INITCAP(string)
Zmienia pierwszą literę każdego wyrazu na wielką, a pozostałe na małe.

sql
Kopiuj
Edytuj
SELECT INITCAP('hello world');  -- Zwraca 'Hello World'
15. LEFT(string, n)
Zwraca pierwsze n znaków łańcucha.

sql
Kopiuj
Edytuj
SELECT LEFT('Hello World', 5);  -- Zwraca 'Hello'
16. RIGHT(string, n)
Zwraca ostatnie n znaków łańcucha.

sql
Kopiuj
Edytuj
SELECT RIGHT('Hello World', 5);  -- Zwraca 'World'
17. CONCAT_WS(separator, string1, string2, ...)
Łączy wartości w jeden łańcuch z określonym separatorem.

sql
Kopiuj
Edytuj
SELECT CONCAT_WS('-', '2025', '01', '22');  -- Zwraca '2025-01-22'
18. CHR(integer)
Zwraca znak odpowiadający kodowi ASCII.

sql
Kopiuj
Edytuj
SELECT CHR(65);  -- Zwraca 'A'
19. ASCII(string)
Zwraca kod ASCII pierwszego znaku w łańcuchu.

sql
Kopiuj
Edytuj
SELECT ASCII('A');  -- Zwraca 65
20. MD5(string)
Zwraca hash MD5 łańcucha znaków.

sql
Kopiuj
Edytuj
SELECT MD5('Hello');  -- Zwraca '8b1a9953c4611296a827abf8c47804d7'
21. ENCODE(bytea, format)
Koduje dane typu bytea w formacie tekstowym.

sql
Kopiuj
Edytuj
SELECT ENCODE('Hello'::bytea, 'base64');  -- Zwraca 'SGVsbG8='
22. DECODE(string, format)
Dekoduje dane z formatu tekstowego na bytea.

sql
Kopiuj
Edytuj
SELECT DECODE('SGVsbG8=', 'base64');  -- Zwraca 'Hello'
23. SIMILAR TO
Umożliwia dopasowanie łańcucha do wzorca z użyciem wyrażeń regularnych (bardziej elastyczne niż LIKE).

sql
Kopiuj
Edytuj
SELECT 'abc' SIMILAR TO 'a.c';  -- Zwraca true
24. LIKE i ILIKE
LIKE - dopasowuje łańcuchy z użyciem wzorca, uwzględniając wielkość liter.
ILIKE - dopasowuje łańcuchy bez uwzględnienia wielkości liter.
sql
Kopiuj
Edytuj
SELECT 'Hello' LIKE 'H%';  -- Zwraca true
SELECT 'Hello' ILIKE 'h%';  -- Zwraca true