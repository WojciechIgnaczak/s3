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