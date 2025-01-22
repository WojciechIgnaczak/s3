1. ABS(number)
Zwraca wartość bezwzględną liczby.

sql
Kopiuj
Edytuj
SELECT ABS(-5);  -- Zwraca 5
2. CEIL(number) lub CEILING(number)
Zwraca najmniejszą liczbę całkowitą większą lub równą danej liczbie.

sql
Kopiuj
Edytuj
SELECT CEIL(4.3);  -- Zwraca 5
3. FLOOR(number)
Zwraca największą liczbę całkowitą mniejszą lub równą danej liczbie.

sql
Kopiuj
Edytuj
SELECT FLOOR(4.7);  -- Zwraca 4
4. ROUND(number, digits)
Zaokrągla liczbę do określonej liczby miejsc po przecinku.

sql
Kopiuj
Edytuj
SELECT ROUND(123.4567, 2);  -- Zwraca 123.46
5. RANDOM()
Zwraca losową liczbę zmiennoprzecinkową z zakresu od 0 do 1.

sql
Kopiuj
Edytuj
SELECT RANDOM();  -- Zwraca losową liczbę np. 0.658
6. SETSEED(seed)
Ustawia nasiono dla funkcji losowych. Może być użyteczne, jeśli chcesz uzyskać powtarzalne wyniki z funkcji RANDOM().

sql
Kopiuj
Edytuj
SELECT SETSEED(0.5);
SELECT RANDOM();  -- Zwraca określoną losową liczbę w zależności od nasienia
7. POWER(base, exponent)
Zwraca wynik podniesienia liczby base do potęgi exponent.

sql
Kopiuj
Edytuj
SELECT POWER(2, 3);  -- Zwraca 8
8. SQRT(number)
Zwraca pierwiastek kwadratowy z liczby.

sql
Kopiuj
Edytuj
SELECT SQRT(9);  -- Zwraca 3
9. EXP(number)
Zwraca wartość e (podstawy logarytmu naturalnego) podniesioną do potęgi number.

sql
Kopiuj
Edytuj
SELECT EXP(1);  -- Zwraca około 2.71828
10. LN(number)
Zwraca logarytm naturalny liczby (logarytm o podstawie e).

sql
Kopiuj
Edytuj
SELECT LN(10);  -- Zwraca około 2.30259
11. LOG(base, number)
Zwraca logarytm liczby number o podstawie base.

sql
Kopiuj
Edytuj
SELECT LOG(10, 100);  -- Zwraca 2 (log10(100))
12. MOD(number, divisor)
Zwraca resztę z dzielenia liczby number przez divisor.

sql
Kopiuj
Edytuj
SELECT MOD(10, 3);  -- Zwraca 1
13. GCD(number1, number2)
Zwraca największy wspólny dzielnik (GCD) dwóch liczb.

sql
Kopiuj
Edytuj
SELECT GCD(12, 15);  -- Zwraca 3
14. PI()
Zwraca wartość liczby π (pi), która wynosi około 3.14159.

sql
Kopiuj
Edytuj
SELECT PI();  -- Zwraca 3.14159265358979
15. SIGN(number)
Zwraca znak liczby: 1 dla liczb dodatnich, -1 dla liczb ujemnych i 0 dla zera.

sql
Kopiuj
Edytuj
SELECT SIGN(-10);  -- Zwraca -1
16. RADIANS(number)
Przekształca liczbę z stopni na radiany.

sql
Kopiuj
Edytuj
SELECT RADIANS(180);  -- Zwraca 3.14159
17. DEGREES(number)
Przekształca liczbę z radianów na stopnie.

sql
Kopiuj
Edytuj
SELECT DEGREES(PI());  -- Zwraca 180
18. TRUNC(number, digits)
Usuwa część dziesiętną liczby, zaokrąglając ją w dół do określonej liczby miejsc po przecinku.

sql
Kopiuj
Edytuj
SELECT TRUNC(123.4567, 2);  -- Zwraca 123.45
19. SIN(number)
Zwraca sinus liczby, która jest w radianach.

sql
Kopiuj
Edytuj
SELECT SIN(PI()/2);  -- Zwraca 1
20. COS(number)
Zwraca cosinus liczby, która jest w radianach.

sql
Kopiuj
Edytuj
SELECT COS(PI());  -- Zwraca -1
21. TAN(number)
Zwraca tangens liczby, która jest w radianach.

sql
Kopiuj
Edytuj
SELECT TAN(PI()/4);  -- Zwraca 1
22. COT(number)
Zwraca kotangens liczby, która jest w radianach.

sql
Kopiuj
Edytuj
SELECT COT(PI()/4);  -- Zwraca 1
23. ACOS(number)
Zwraca arcus cosinus (odwrotność funkcji COS), czyli kąt w radianach.

sql
Kopiuj
Edytuj
SELECT ACOS(1);  -- Zwraca 0
24. ASIN(number)
Zwraca arcus sinus (odwrotność funkcji SIN), czyli kąt w radianach.

sql
Kopiuj
Edytuj
SELECT ASIN(1);  -- Zwraca PI()/2
25. ATAN(number)
Zwraca arcus tangens (odwrotność funkcji TAN), czyli kąt w radianach.

sql
Kopiuj
Edytuj
SELECT ATAN(1);  -- Zwraca PI()/4
26. ATAN2(y, x)
Zwraca arcus tangens dwóch zmiennych y i x, dając kąt w radianach.

sql
Kopiuj
Edytuj
SELECT ATAN2(1, 1);  -- Zwraca PI()/4
27. BETWEEN
Używane w porównaniach, sprawdza, czy liczba mieści się w określonym zakresie.

sql
Kopiuj
Edytuj
SELECT 10 BETWEEN 5 AND 15;  -- Zwraca true