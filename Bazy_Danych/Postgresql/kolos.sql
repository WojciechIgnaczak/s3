
CREATE DATABASE hotel_management;
-- \c hotel_management
-- jest wbudowany CREATE SCHEMA public; -- tabele



CREATE SCHEMA IF NOT EXISTS views_shema; -- widoki

CREATE SCHEMA IF NOT EXISTS procedures_schema; -- funkcje i procedury



CREATE ROLE order_user;
-- uprawnienia do dodawania rezerwacji i sprawdzenia dostepnosci
GRANT CREATE, USAGE ON SCHEMA public TO order_user;
GRANT CREATE, USAGE ON SCHEMA views_shema TO order_user;
GRANT CREATE, USAGE ON SCHEMA procedures_schema TO order_user;




CREATE ROLE stats_user;
-- uprawnienia do statystyki
GRANT USAGE ON SCHEMA public TO stats_user;
GRANT USAGE ON SCHEMA views_shema TO stats_user;
GRANT USAGE ON SCHEMA procedures_schema TO stats_user;








CREATE TABLE IF NOT EXISTS public.guests(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    surename TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE, 
    phone_number TEXT NOT NULL UNIQUE,
    add_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);










CREATE TABLE IF NOT EXISTS public.rooms(
    id SERIAL PRIMARY KEY,
    number INT NOT NULL UNIQUE CHECK(number >0) ,
    type TEXT NOT NULL CHECK(type IN ('Single', 'Double', 'Suite')),
    price NUMERIC(10,2) NOT NULL,
    availability BOOLEAN DEFAULT true
);








CREATE TABLE IF NOT EXISTS  public.reservations(
    id SERIAL PRIMARY KEY,
    id_guest INT NOT NULL REFERENCES public.guests(id),
    id_room INT NOT NULL REFERENCES public.rooms(id),
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
    end_date TIMESTAMP CHECK ( start_date < end_date),
    cost NUMERIC(10,2) NOT NULL,
    add_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);










CREATE OR REPLACE VIEW views_shema.available_rooms AS
    SELECT id, number, type, price FROM rooms
    WHERE availability=true;








CREATE OR REPLACE VIEW views_shema.reservations_details AS
SELECT 
    r.id AS room_id,
    CONCAT(g.name, ' ', g.surename) AS guests_name_surname,
    r.number,
    r.type,
    r.price
FROM 
    public.rooms r
JOIN 
    public.guests g ON r.id = g.id
JOIN 
    public.reservations re ON g.id = re.id_guest;








-- widok zmaterializowany agreguje srednie ceny pokoi wedlug typow

CREATE MATERIALIZED VIEW IF NOT EXISTS views_shema.room_type_statistic AS
SELECT 
    type,
    AVG(price) AS avg_price
FROM 
    public.rooms
GROUP BY 
    type;





CREATE INDEX IF NOT EXISTS mail_index ON public.guests(email);

CREATE INDEX IF NOT EXISTS room_type_index ON public.rooms(type);

CREATE INDEX IF NOT EXISTS start_date_index ON public.reservations(start_date);

CREATE INDEX IF NOT EXISTS end_date_index ON public.reservations(end_date);








-- funkcja ktora oblicz laczny koszt rezerwacji na podstawie id pokojum dat zameldowania i wymeldowania
CREATE OR REPLACE FUNCTION procedures_schema.calculate_reservation_cost(id_room INT, start_date TIMESTAMP, end_date TIMESTAMP)
RETURNS NUMERIC(10, 2) AS $$
DECLARE
    price_per_day NUMERIC(10, 2);
    number_of_days INT;
    total_cost NUMERIC(10, 2);
BEGIN
    SELECT price INTO price_per_day
    FROM public.rooms
    WHERE id = id_room;

    number_of_days := (end_date::DATE - start_date::DATE);

    total_cost := price_per_day * number_of_days;

    RETURN total_cost;
END;
$$ LANGUAGE plpgsql;












--- procedure ktora tworzy nową rezerwacje i aktualizuje status dostepnosc pokoju

CREATE OR REPLACE PROCEDURE procedures_schema.create_reservation(
    id_guest INT,
    id_room INT,
    start_date TIMESTAMP,
    end_date TIMESTAMP
)
LANGUAGE plpgsql AS $$
DECLARE
    total_cost NUMERIC(10, 2);
BEGIN
    IF NOT EXISTS (SELECT * FROM public.rooms WHERE id = id_room AND availability = true) THEN
        RAISE EXCEPTION 'Room  not available';
    END IF;

    total_cost := procedures_schema.calculate_reservation_cost(id_room, start_date, end_date);

    INSERT INTO public.reservations(id_guest, id_room, start_date, end_date, cost)
    VALUES (id_guest, id_room, start_date, end_date, total_cost);

    UPDATE public.rooms
    SET availability = false
    WHERE id = id_room;
END;
$$;










CREATE OR REPLACE FUNCTION procedures_schema.update_room_availability()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE public.rooms
    SET availability = TRUE
    WHERE id = OLD.id_room;

    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER after_reservation_delete
AFTER DELETE ON public.reservations
FOR EACH ROW
EXECUTE FUNCTION procedures_schema.update_room_availability();





-- DODAC REPLACE DODAC IF NOT EXISTS ZROBIONE

-- PRZENIESC INSERY I WYWOŁANIA NA KONIEC ZROBIONE



--INSERTY
INSERT INTO public.guests (name, surename, email, phone_number)
VALUES 
('A', 'B', 'ab@gmail.com', '123456789'),
('C', 'D', 'cd@gmail.com', '987655432'),
('E', 'F', 'ef@gmail.com', '567890123'),
('G', 'H', 'gh@gmail.com', '456123789'),
('I', 'J', 'ij@gmail.com', '789012345'),
('K', 'L', 'kl@gmail.com', '345678901');



INSERT INTO public.rooms (number, type, price, availability)
VALUES 
(101, 'Single', 100.00, true),
(112, 'Single', 120.00, true),
(209, 'Double', 150.00, true),
(202, 'Double', 170.00, false),
(321, 'Suite', 250.00, true),
(382, 'Suite', 300.00, true),
(451, 'Single', 110.00, false);


INSERT INTO public.reservations (id_guest, id_room, start_date, end_date, cost)
VALUES 
(1, 6, '2025-01-01 14:00:00', '2025-01-05 11:00:00', 400.00),
(2, 5, '2025-01-02 14:00:00', '2025-01-06 11:00:00', 480.00),
(3, 4, '2025-01-03 14:00:00', '2025-01-08 11:00:00', 750.00),
(4, 3, '2025-01-04 14:00:00', '2025-01-09 11:00:00', 1250.00);



-- WIDOKI
SELECT * FROM views_shema.available_rooms;

SELECT * FROM views_shema.reservations_details;

REFRESH MATERIALIZED VIEW views_shema.room_type_statistic;
SELECT * FROM views_shema.room_type_statistic;


-- FUNKCJE I PROCEDURY
SELECT procedures_schema.calculate_reservation_cost(1,'2025-01-06 17:00:00','2025-01-08 11:00:00');

CALL procedures_schema.create_reservation(1,6,'2025-01-06 17:00:00','2025-01-08 11:00:00' );

-- TRIGGER
DELETE FROM public.reservations 
WHERE id=9;