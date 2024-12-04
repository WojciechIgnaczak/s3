CREATE DATABASE car_rental;

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
year_of_productions INT NOT NULL CHECK (year_of_productions >= 1990),
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
SELECT * FROM vehicle.car
WHERE status = 'available';

CREATE VIEW car_rental.active_reservations AS
SELECT r.reservation_id, c.first_name, c.last_name, car.make, car.model, r.pickup_date, r.return_date
FROM car_rental.reservations r
JOIN car_rental.customers c ON r.customer_id = c.customer_id
JOIN car_rental.cars car ON r.car_id = car.car_id
WHERE CURRENT_DATE BETWEEN r.pickup_date AND r.return_date;
