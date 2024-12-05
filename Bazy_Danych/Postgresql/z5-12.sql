-- CREATE ROLE admin WITH LOGIN PASSWORD 'admin';
-- GRANT ALL PRIVILEGES ON DATABASE pw_4_psql TO admin
-- CREATE DATABASE db_car OWNER admin;

CREATE TABLE account(
    account_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL CHECK(first_name NOT LIKE '% %'),
    last_name VARCHAR(50) NOT NULL CHECK(last_name NOT LIKE '% %'),
    email TEXT NOT NULL UNIQUE CHECK(email ~* '^\w+@\w+[.]\w+$') ,
    password TEXT NOT NULL CHECK(LENGTH(password)>=8)
);

--insert into account(first_name,last_name,email,password) values ('wojtel', 'igancz', 'kakexqple@op.pl', 'haddgg123');


CREATE TABLE seller_account(
    seller_account_id SERIAL PRIMARY KEY,
    account_id INT UNIQUE NOT NULL REFERENCES account(account_id),
    number_of_advert INT DEFAULT 0,
    user_ranking FLOAT,
    total FLOAT
);