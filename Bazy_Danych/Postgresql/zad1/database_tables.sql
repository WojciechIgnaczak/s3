CREATE ROLE admin WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE car_rental TO admin; 

CREATE DATABASE car_rental;

\c car_rental

CREATE SCHEMA customer;
CREATE SCHEMA vehicle;
CREATE SCHEMA rental;
CREATE SCHEMA employee;

CREATE TABLE customer.customer(
customer_ID SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL,
surname VARCHAR(50) NOT NULL,
address TEXT NOT NULL,
phone_number VARCHAR(15) NOT NULL UNIQUE
);

CREATE TABLE vehicle.car(
car_ID SERIAL PRIMARY KEY,
brand VARCHAR(20) NOT NULL,
model VARCHAR(30) NOT NULL,
year_of_productions INT NOT NULL CHECK (year_of_productions >= 2000),
vin_number CHAR(17) NOT NULL,
category VARCHAR(30) NOT NULL,
rejestration_number VARCHAR(8) NOT NULL,
daily_price DECIMAL(10, 2) NOT NULL,
availability VARCHAR(30) NOT NULL DEFAULT 'available'
);

CREATE TABLE vehicle.maintenance(
maintenance_ID SERIAL PRIMARY KEY,
car_ID INT,
price DECIMAL(10, 2),
service VARCHAR(40),
scope_of_repairs TEXT,
date_from TIMESTAMP,
date_to TIMESTAMP,
FOREIGN KEY (car_ID) REFERENCES vehicle.car(car_ID)
);

CREATE TABLE employee.employee(
employee_ID SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL,
surname VARCHAR(50) NOT NULL,
address TEXT NOT NULL,
phone_number VARCHAR(15) NOT NULL UNIQUE,
salary DECIMAL(10, 2) NOT NULL,
position TEXT NOT NULL DEFAULT 'Pracownik biurowy',
hire_date TIMESTAMP
);

CREATE TABLE rental.reservation(
reservation_ID SERIAL PRIMARY KEY,
car_ID INT,
customer_ID INT,
date_from TIMESTAMP,
date_to TIMESTAMP,
employee_ID INT,
FOREIGN KEY (car_ID) REFERENCES vehicle.car(car_ID),
FOREIGN KEY (customer_ID) REFERENCES customer.customer(customer_ID),
FOREIGN KEY (employee_ID) REFERENCES employee.employee(employee_ID)
);

CREATE TABLE rental.payment(
payment_ID SERIAL PRIMARY KEY,
price DECIMAL(10, 2) NOT NULL,
customer_ID INT,
reservation_ID INT,
FOREIGN KEY (customer_ID) REFERENCES customer.customer(customer_ID),
FOREIGN KEY (reservation_ID) REFERENCES rental.reservation(reservation_ID)
);


CREATE VIEW car_rental.available_cars AS
SELECT * 
FROM vehicle.car
WHERE availability = 'available';


CREATE VIEW car_rental.active_reservations AS
SELECT 
    r.reservation_ID, 
    c.name AS customer_name, 
    c.surname AS customer_surname, 
    car.brand, 
    car.model, 
    r.date_from, 
    r.date_to
FROM rental.reservation r
JOIN customer.customer c ON r.customer_ID = c.customer_ID
JOIN vehicle.car car ON r.car_ID = car.car_ID
WHERE CURRENT_DATE BETWEEN r.date_from AND r.date_to;


INSERT INTO customer.customer (name, surname, address, phone_number) VALUES
('Jan', 'Kowalski', 'ul. Zielona 5, Warszawa', '123456789'),
('Anna', 'Nowak', 'ul. Słoneczna 10, Kraków', '987654321'),
('Piotr', 'Wiśniewski', 'ul. Spacerowa 3, Gdańsk', '555666777'),
('Katarzyna', 'Maj', 'ul. Lipowa 8, Łódź', '111222333'),
('Marek', 'Nowicki', 'ul. Długa 15, Poznań', '444555666'),
('Paulina', 'Lis', 'ul. Krótka 1, Wrocław', '333444555'),
('Tomasz', 'Zieliński', 'ul. Polna 20, Białystok', '777888999'),
('Agnieszka', 'Sobczak', 'ul. Chmielna 12, Szczecin', '222333444'),
('Łukasz', 'Bąk', 'ul. Leśna 7, Lublin', '999000111'),
('Joanna', 'Nowicka', 'ul. Kościuszki 14, Katowice', '666777888');

INSERT INTO vehicle.car (brand, model, year_of_productions, vin_number, category, registration_number, daily_price, availability) VALUES
('Toyota', 'Corolla', 2015, '1HGCM82633A123456', 'Sedan', 'WZ1234A', 150.00, 'available'),
('Ford', 'Focus', 2018, '1HGCM82633A654321', 'Hatchback', 'KR5678B', 170.00, 'rented'),
('BMW', 'X5', 2020, '1HGCM82633A987654', 'SUV', 'GD9101C', 250.00, 'available'),
('Honda', 'Civic', 2017, '1HGCM82633A543210', 'Sedan', 'PO1111D', 140.00, 'available'),
('Mercedes', 'A-Class', 2019, '1HGCM82633A111222', 'Hatchback', 'LU2222E', 200.00, 'rented'),
('Volkswagen', 'Golf', 2016, '1HGCM82633A333444', 'Hatchback', 'WA3333F', 160.00, 'available'),
('Audi', 'A4', 2018, '1HGCM82633A555666', 'Sedan', 'KR4444G', 180.00, 'available'),
('Kia', 'Sportage', 2021, '1HGCM82633A777888', 'SUV', 'PO5555H', 230.00, 'rented'),
('Skoda', 'Octavia', 2017, '1HGCM82633A999000', 'Sedan', 'GD6666I', 150.00, 'available'),
('Hyundai', 'Tucson', 2020, '1HGCM82633A111333', 'SUV', 'LU7777J', 240.00, 'available');

INSERT INTO employee.employee (name, surname, address, phone_number, salary, position, hire_date) VALUES
('Katarzyna', 'Maj', 'ul. Lipowa 8, Łódź', '111222333', 4500.00, 'Manager', '2023-01-15'),
('Marek', 'Nowicki', 'ul. Długa 15, Poznań', '444555666', 3500.00, 'Mechanik', '2022-11-10'),
('Anna', 'Kaczmarek', 'ul. Słowackiego 4, Gdynia', '222444666', 3700.00, 'Księgowy', '2021-07-01'),
('Łukasz', 'Baran', 'ul. Mickiewicza 12, Toruń', '333555777', 3200.00, 'Pracownik biurowy', '2020-03-10'),
('Agnieszka', 'Sobczak', 'ul. Chmielna 12, Szczecin', '555777999', 4000.00, 'Specjalista ds. wynajmu', '2019-08-05'),
('Tomasz', 'Wilk', 'ul. Kościuszki 8, Olsztyn', '666888000', 3400.00, 'Kierownik serwisu', '2023-06-01'),
('Paulina', 'Lis', 'ul. Orzechowa 14, Zielona Góra', '777000999', 3600.00, 'Recepcjonista', '2021-10-20'),
('Joanna', 'Nowicka', 'ul. Kościuszki 14, Katowice', '888111222', 3300.00, 'Pracownik biurowy', '2022-01-15'),
('Piotr', 'Kowal', 'ul. Słoneczna 2, Opole', '999222333', 3100.00, 'Kierowca', '2020-05-15'),
('Michał', 'Wiśniewski', 'ul. Św. Marcin 5, Poznań', '111333555', 4200.00, 'Kierownik oddziału', '2018-09-10');

INSERT INTO rental.reservation (car_ID, customer_ID, date_from, date_to, employee_ID) VALUES
(1, 1, '2024-12-01 10:00:00', '2024-12-05 18:00:00', 1),
(2, 2, '2024-12-03 09:00:00', '2024-12-06 16:00:00', 2),
(3, 3, '2024-12-04 12:00:00', '2024-12-10 12:00:00', 3),
(4, 4, '2024-12-05 08:00:00', '2024-12-07 20:00:00', 4),
(5, 5, '2024-12-02 15:00:00', '2024-12-08 18:00:00', 5),
(6, 6, '2024-12-06 10:00:00', '2024-12-09 15:00:00', 6),
(7, 7, '2024-12-07 14:00:00', '2024-12-12 10:00:00', 7),
(8, 8, '2024-12-08 09:00:00', '2024-12-13 18:00:00', 8),
(9, 9, '2024-12-09 11:00:00', '2024-12-15 14:00:00', 9),
(10, 10, '2024-12-10 08:00:00', '2024-12-14 20:00:00', 10);

INSERT INTO rental.payment (price, customer_ID, reservation_ID) VALUES
(600.00, 1, 1),
(510.00, 2, 2),
(750.00, 3, 3),
(320.00, 4, 4),
(640.00, 5, 5),
(550.00, 6, 6),
(720.00, 7, 7),
(850.00, 8, 8),
(410.00, 9, 9),
(390.00, 10, 10);

INSERT INTO vehicle.maintenance (car_ID, price, service, scope_of_repairs, date_from, date_to) VALUES
(1, 1200.00, 'Warsztat AutoFix', 'Wymiana klocków hamulcowych', '2024-11-20 08:00:00', '2024-11-22 17:00:00'),
(2, 500.00, 'AutoSerwis Plus', 'Wymiana oleju', '2024-11-15 09:00:00', '2024-11-15 15:00:00'),
(3, 1500.00, 'Serwis Pro', 'Naprawa silnika', '2024-10-10 08:00:00', '2024-10-20 18:00:00'),
(4, 200.00, 'Mechanika Samochodowa XYZ', 'Wymiana żarówek', '2024-11-01 10:00:00', '2024-11-01 14:00:00'),
(5, 800.00, 'AutoSerwis Łódź', 'Wymiana amortyzatorów', '2024-09-15 09:00:00', '2024-09-20 17:00:00'),
(6, 700.00, 'CarFixer', 'Naprawa układu wydechowego', '2024-10-05 12:00:00', '2024-10-10 16:00:00'),
(7, 300.00, 'Szybki Serwis', 'Wymiana opon', '2024-11-10 08:00:00', '2024-11-10 12:00:00'),
(8, 250.00, 'Serwis 24h', 'Czyszczenie klimatyzacji', '2024-08-01 09:00:00', '2024-08-01 11:00:00'),
(9, 1000.00, 'Auto Centrum', 'Naprawa zawieszenia', '2024-07-15 08:00:00', '2024-07-20 17:00:00'),
(10, 400.00, 'Naprawy Ekspres', 'Wymiana akumulatora', '2024-06-10 08:00:00', '2024-06-10 14:00:00');
