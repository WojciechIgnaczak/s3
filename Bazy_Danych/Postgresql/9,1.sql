CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE users_logs(
    id SERIAL PRIMARY KEY,
    action VARCHAR(10) NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    change_time TIMESTAMP 
);


CREATE OR REPLACE FUNCTION log_user_changes()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP ='INSERT' THEN
        INSERT INTO users_logs(action,username,email,change_time)
        VALUES ('INSERT', NEW.username,NEW.email,CURRENT_TIMESTAMP);
    ELSIF TG_OP ='UPDATE' THEN
        INSERT INTO users_logs(action,username,email,change_time)
        VALUES ('UPDATE', NEW.username,NEW.email,CURRENT_TIMESTAMP);
    ELSIF TG_OP ='DELETE' THEN
        INSERT INTO users_logs(action,username,email,change_time)
        VALUES ('DELETE', OLD.username,OLD.email,CURRENT_TIMESTAMP);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER user_change_trigger
AFTER INSERT OR UPDATE OR DELETE
ON users
FOR EACH ROW
EXECUTE FUNCTION log_user_changes();



CREATE OR REPLACE VIEW user_view AS
SELECT id, username, email FROM users_logs;

CREATE OR REPLACE FUNCTION handle_view_changes()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP='INSERT' THEN
        INSERT INTO users(username,email) VALUES (NEW.username, NEW.email);
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER instead_of_trigger
INSTEAD OF INSERT
ON user_view
FOR EACH ROW

EXECUTE FUNCTION handle_view_changes();



CREATE OR REPLACE FUNCTION log_trunate()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO users_log(action,change_time) VALUES ('TRUNCATE', CURRENT_TIMESTAMP);
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;






-- zadanie
CREATE TABLE products(
    id serial PRIMARY KEY,
    name VARCHAR(100),
    price numeric,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products_logs(
    id serial PRIMARY KEY,
    action VARCHAR(15),
    product_name VARCHAR(100),
    price numeric,
    change_time TIMESTAMP
    CHECK (action IN ('INSERT', 'UPDATE','DELETE','TRUNCATE'))
);


CREATE OR REPLACE FUNCTION log_products()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP='INSERT' THEN
        INSERT INTO products_logs(id,action,product_name,price,change_time) VALUES (NEW.id,'INSERT',NEW.name,NEW.price, CURRENT_TIMESTAMP);
    ELSIF TG_OP='UPDATE' THEN
        INSERT INTO products_logs(id,action,product_name,price,change_time) VALUES (NEW.id,'UPDATE',NEW.name,NEW.price, CURRENT_TIMESTAMP);
    ELSIF TG_OP='DELETE' THEN
        INSERT INTO products_logs(id,action,product_name,price,change_time) VALUES (OLD.id,'DELETE',OLD.name,OLD.price, CURRENT_TIMESTAMP);
    RETURN NULL
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER products_to_log_trigger
AFTER OF INSERT OR UPDATE OR DELETE
ON products
FOR EACH ROW
EXECUTE FUNCTION log_products();

