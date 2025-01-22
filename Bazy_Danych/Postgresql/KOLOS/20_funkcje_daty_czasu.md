PostgreSQL oferuje szereg funkcji i operatorów związanych z datą i czasem. Oto niektóre z nich:

1. Aktualna data i czas
CURRENT_DATE – zwraca bieżącą datę (bez godziny).
CURRENT_TIME – zwraca bieżący czas (bez daty).
CURRENT_TIMESTAMP lub NOW() – zwraca bieżącą datę i czas.
LOCALTIME – zwraca bieżący czas w lokalnej strefie czasowej.
LOCALTIMESTAMP – zwraca bieżącą datę i czas w lokalnej strefie czasowej.
2. Formatowanie daty i czasu
TO_CHAR(date, format) – formatuje datę lub czas na podstawie określonego wzorca.
Przykład: TO_CHAR(NOW(), 'YYYY-MM-DD HH24:MI:SS') zwraca bieżącą datę i czas w formacie YYYY-MM-DD HH:MM:SS.
3. Obliczenia z datami i czasami
Dodawanie i odejmowanie:
date + interval '1 day' – dodaje jeden dzień do daty.
date - interval '1 hour' – odejmuje jedną godzinę od daty.
date1 - date2 – oblicza różnicę między dwiema datami.
AGE(timestamp) – oblicza różnicę między bieżącym czasem a podanym czasem.
Przykład: AGE('2025-01-01') zwróci różnicę między dzisiejszą datą a 1 stycznia 2025.
4. Manipulowanie datą
DATE_TRUNC('field', date) – obcina datę do określonego poziomu precyzji (np. dzień, miesiąc, rok).
Przykład: DATE_TRUNC('month', NOW()) zwróci pierwszy dzień bieżącego miesiąca.
5. Różne funkcje i operatory
EXTRACT(field FROM timestamp) – wyciąga określoną część daty lub czasu (np. rok, miesiąc, dzień).
Przykład: EXTRACT(YEAR FROM NOW()) zwróci bieżący rok.
DATE_PART(field, timestamp) – podobne do EXTRACT(), ale z innym formatem.
6. Operatory porównań i zakresów
BETWEEN – sprawdza, czy wartość daty mieści się w danym przedziale.
Przykład: date BETWEEN '2024-01-01' AND '2024-12-31'.
7. Konwersja i formatowanie
CAST(expression AS type) – konwertuje dane do innego typu.
Przykład: CAST('2025-01-01' AS DATE) konwertuje tekst na datę.
8. Funkcje związane z czasem strefowym
AT TIME ZONE – zmienia strefę czasową dla daty lub czasu.
Przykład: NOW() AT TIME ZONE 'UTC' konwertuje bieżący czas na czas UTC.
9. Interval
Możliwość definiowania przedziałów czasowych, np. interval '2 days', interval '3 hours'.
Przykład: NOW() + interval '3 days' – dodaje 3 dni do bieżącej daty i czasu.
PostgreSQL oferuje również pełną dokumentację, gdzie znajdziesz szczegóły dla każdego z tych typów funkcji i operatorów.







Powiedziałeś(-aś):
wycinanie dnia, miesiaca, roku z daty
ChatGPT powiedział:
ChatGPT
Aby wyciąć dzień, miesiąc lub rok z daty w PostgreSQL, możesz użyć funkcji EXTRACT lub DATE_PART. Oto jak to zrobić:

1. Wydobywanie dnia
sql
Kopiuj
Edytuj
SELECT EXTRACT(DAY FROM CURRENT_DATE);
Lub:

sql
Kopiuj
Edytuj
SELECT DATE_PART('day', CURRENT_DATE);
Obie zapytania zwrócą dzień bieżącej daty.

2. Wydobywanie miesiąca
sql
Kopiuj
Edytuj
SELECT EXTRACT(MONTH FROM CURRENT_DATE);
Lub:

sql
Kopiuj
Edytuj
SELECT DATE_PART('month', CURRENT_DATE);
Obie zapytania zwrócą miesiąc bieżącej daty.

3. Wydobywanie roku
sql
Kopiuj
Edytuj
SELECT EXTRACT(YEAR FROM CURRENT_DATE);
Lub:

sql
Kopiuj
Edytuj
SELECT DATE_PART('year', CURRENT_DATE);
Obie zapytania zwrócą rok bieżącej daty.

Przykłady z konkretnymi datami:
Wydobycie dnia z daty 2025-01-22:

sql
Kopiuj
Edytuj
SELECT EXTRACT(DAY FROM DATE '2025-01-22');
Wynik: 22

Wydobycie miesiąca z daty 2025-01-22:

sql
Kopiuj
Edytuj
SELECT EXTRACT(MONTH FROM DATE '2025-01-22');
Wynik: 1

Wydobycie roku z daty 2025-01-22:

sql
Kopiuj
Edytuj
SELECT EXTRACT(YEAR FROM DATE '2025-01-22');
Wynik: 2025
















W PostgreSQL istnieje wiele funkcji i operatorów służących do pracy z czasem. Oto najważniejsze z nich:

1. Wydobywanie poszczególnych części czasu
Można użyć funkcji EXTRACT lub DATE_PART, aby wyciągnąć poszczególne składowe czasu (godzina, minuta, sekunda).

Wydobycie godziny:

sql
Kopiuj
Edytuj
SELECT EXTRACT(HOUR FROM CURRENT_TIME);
Wynik: godzina bieżącego czasu.

Wydobycie minuty:

sql
Kopiuj
Edytuj
SELECT EXTRACT(MINUTE FROM CURRENT_TIME);
Wynik: minuta bieżącego czasu.

Wydobycie sekundy:

sql
Kopiuj
Edytuj
SELECT EXTRACT(SECOND FROM CURRENT_TIME);
Wynik: sekunda bieżącego czasu.

Przykład z użyciem DATE_PART:

sql
Kopiuj
Edytuj
SELECT DATE_PART('hour', CURRENT_TIME);
SELECT DATE_PART('minute', CURRENT_TIME);
SELECT DATE_PART('second', CURRENT_TIME);
2. Obliczenia z czasem
PostgreSQL umożliwia dodawanie lub odejmowanie czasu za pomocą operatorów + i -.

Dodanie godzin, minut lub sekund do czasu:

sql
Kopiuj
Edytuj
SELECT CURRENT_TIME + INTERVAL '2 hours';  -- Dodanie 2 godzin
SELECT CURRENT_TIME + INTERVAL '30 minutes';  -- Dodanie 30 minut
SELECT CURRENT_TIME + INTERVAL '45 seconds';  -- Dodanie 45 sekund
Odejmowanie godzin, minut lub sekund od czasu:

sql
Kopiuj
Edytuj
SELECT CURRENT_TIME - INTERVAL '2 hours';  -- Odjęcie 2 godzin
SELECT CURRENT_TIME - INTERVAL '30 minutes';  -- Odjęcie 30 minut
SELECT CURRENT_TIME - INTERVAL '45 seconds';  -- Odjęcie 45 sekund
3. Aktualny czas
Aktualny czas:

sql
Kopiuj
Edytuj
SELECT CURRENT_TIME;
Aktualny znacznik czasu (data i czas):

sql
Kopiuj
Edytuj
SELECT CURRENT_TIMESTAMP;
Czas w lokalnej strefie czasowej:

sql
Kopiuj
Edytuj
SELECT LOCALTIME;
4. Operacje z Interwałami
PostgreSQL obsługuje interwały czasowe, które pozwalają na wykonywanie obliczeń między czasem a datami.

Przykład dodania interwału do czasu:

sql
Kopiuj
Edytuj
SELECT CURRENT_TIME + INTERVAL '1 day';  -- Dodaje jeden dzień do bieżącego czasu
SELECT CURRENT_TIME + INTERVAL '5 minutes';  -- Dodaje 5 minut do bieżącego czasu
Obliczanie różnicy między dwoma czasami (operacja -):

sql
Kopiuj
Edytuj
SELECT (CURRENT_TIME - '10:00:00'::time);  -- Zwraca różnicę między bieżącym czasem a 10:00:00
5. Przekształcanie czasów i daty
Można konwertować między różnymi typami czasów lub dat.

Konwertowanie czasu na datę (jeśli chcesz połączyć datę z czasem):

sql
Kopiuj
Edytuj
SELECT CURRENT_DATE + CURRENT_TIME;
Zmienianie strefy czasowej:

sql
Kopiuj
Edytuj
SELECT CURRENT_TIME AT TIME ZONE 'UTC';  -- Konwertuje bieżący czas na strefę czasową UTC
6. Zwracanie pełnego czasu
Jeśli potrzebujesz pełnej precyzji z godziną, minutą, sekundą i mikrosekundą:

sql
Kopiuj
Edytuj
SELECT NOW();  -- Zwraca pełny znacznik czasu (data + czas)
Konwersja na konkretne formaty (z użyciem TO_CHAR):
sql
Kopiuj
Edytuj
SELECT TO_CHAR(CURRENT_TIME, 'HH24:MI:SS');  -- Formatuje czas w godzinach, minutach i sekundach
7. Obliczenia z czasem (INTERVAL)
Można dodać lub odjąć całe okresy czasu:

Dodanie dni, godzin, minut do czasu:

sql
Kopiuj
Edytuj
SELECT CURRENT_TIME + INTERVAL '2 hours 15 minutes';  -- Dodaje 2 godziny i 15 minut
Użycie stałych INTERVAL:

sql
Kopiuj
Edytuj
SELECT CURRENT_TIME + INTERVAL '1 hour 30 minutes';  -- Dodaje 1 godzinę i 30 minu