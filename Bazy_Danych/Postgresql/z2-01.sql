-- funkcja obliczająca powierzchnie prostokąta

CREATE OR REPLACE FUNCTION calculate_rectangle_area(length NUMERIC, width NUMERIC) RETURNS NUMERIC AS $$
BEGIN
    IF length <=0 OR width <=0 THEN
        RETURN NULL;
    ELSE
        RETURN length*width;
    END IF;
END;
$$ LANGUAGE plpgsql;

SELECT calculate_rectangle_area(2,3);



-- zadanie funckja przyjmuje tekst i pojedynczy znak a nastepnie zwraca liczbe wystapien tego znaku w tekscie

CREATE OR REPLACE FUNCTION count_character_occurrences(zdanie TEXT, znak CHAR) RETURNS INT AS $$
DECLARE 
    wynik INT :=0 ;
    i INT;
BEGIN
    FOR i IN 1..length(zdanie) LOOP
        IF SUBSTRING(zdanie, i, 1) = znak THEN
            wynik := wynik + 1;
        END IF;
    END LOOP;
    RETURN wynik;
END;
$$ LANGUAGE plpgsql;

SELECT count_character_occurrences('Ala ma kota.', 'a');


CREATE OR REPLACE FUNCTION count_character_occurrences(zdanie TEXT, znak CHAR) RETURNS INT AS $$
BEGIN;
    RETURN length(zdanie)-length(REPLACE(zdanie,znak,''));
END;
$$ LANGUAGE plpgsql;


-- zadanie funkcja zwaracjąca najdłuższe słowo
CREATE OR REPLACE FUNCTION longest_word(sentence TEXT) RETURNS TEXT AS $$
DECLARE
    words TEXT[] := string_to_array(sentence,' ');
    longest TEXT :='';
    word TEXT;
BEGIN
    FOREACH word IN ARRAY words LOOP
        IF length(word)>length(longest) THEN
            longest=word;
        END IF;
    END LOOP;
    RETURN longest;
END;
$$ LANGUAGE plpgsql;
SELECT longest_word('The quick brown fox jumps over the lazy dog'); -- Wynik: quick


CREATE OR REPLACE FUNCTION longest_word(sentence TEXT) RETURNS TEXT AS $$
DECLARE
    words TEXT[] := string_to_array(sentence,' ');
    longest TEXT :='';
    word TEXT;
BEGIN
    IF 
    FOREACH word IN ARRAY words LOOP
        IF length(word)>length(longest) THEN
            longest=word;
        ELSIF length(word)==length(longest) THEN
            longest := longest || ', ' || word;
        END IF;
    END LOOP;
    RETURN longest;
END;
$$ LANGUAGE plpgsql;


-- Ciąg fibonacci

CREATE OR REPLACE FUNCTION generate_fibonacci(n INT) RETURNS TEXT AS $$
DECLARE
    a INT :=0;
    b INT :=1;
    temp INT;
    result TEXT :='0';
BEGIN
    FOR i IN 2..n LOOP
        temp:= a+b;
        a:=b;
        b:=temp;
        result :=result || ', ' || a;
    END LOOP;
    RETURN result;
END;
$$ LANGUAGE plpgsql;


-- dodanie nowego samochodu do bazy
CREATE OR REPLACE FUNCTION add_account(new_username VARCHAR, new_email TEXT, new_balance NUMERIC, new_is_active BOOLEAN, ) RETURN VOID AS $$
BEGIN
    INSERT INTO cars(model,price) VALUES (new_model,new_price);
END;
$$ LANGUAGE plpgsql;