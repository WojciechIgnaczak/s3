CREATE TABLE customers(
customer_ID SERIAL PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
phone_number VARCHAR(15) NOT NULL UNIQUE,
address TEXT NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customers (first_name, last_name, email, phone_number, address, created_at)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St', CURRENT_TIMESTAMP),
('Jane', 'Smith', 'jane.smith@example.com', '9876543210', '456 Elm St', CURRENT_TIMESTAMP - INTERVAL '1 day'),
('Alice', 'Johnson', 'alice.johnson@example.com', '5678901234', '789 Oak Ave', CURRENT_TIMESTAMP - INTERVAL '2 days'),
('Bob', 'Brown', 'bob.brown@example.com', '2345678901', '321 Pine Dr', CURRENT_TIMESTAMP - INTERVAL '3 days'),
('Charlie', 'Williams', 'charlie.williams@example.com', '3456789012', '654 Maple Ln', CURRENT_TIMESTAMP - INTERVAL '4 days'),
('Diana', 'Taylor', 'diana.taylor@example.com', '4567890123', '987 Birch Ct', CURRENT_TIMESTAMP - INTERVAL '5 days'),
('Ethan', 'Harris', 'ethan.harris@example.com', '5678901134', '159 Cherry Pl', CURRENT_TIMESTAMP - INTERVAL '6 days'),
('Fiona', 'Martin', 'fiona.martin@example.com', '6789012345', '753 Walnut Rd', CURRENT_TIMESTAMP - INTERVAL '7 days'),
('George', 'Thompson', 'george.thompson@example.com', '7890123456', '852 Cedar Way', CURRENT_TIMESTAMP - INTERVAL '8 days'),
('Hannah', 'Clark', 'hannah.clark@example.com', '8901234567', '951 Aspen Blvd', CURRENT_TIMESTAMP - INTERVAL '9 days');

--brak klucza głównego powoduje że baza nie może znaleźć unikalności
CREATE TABLE customers2(
name VARCHAR(50) NOT NULL,
surname VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
address TEXT NOT NULL,
phone_number VARCHAR(15) NOT NULL UNIQUE,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- widok customer/user
CREATE TEMP VIEW temp_user_view AS
SELECT
    customer_ID,
    first_name,
    last_name,
    email
FROM
    customers;