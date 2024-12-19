-- utworzenie tabeli
CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    balance NUMERIC(10, 2) DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

-- inserty do tabli
INSERT INTO accounts (username, email, balance, is_active, created_at)
VALUES 
('JohnDoe', 'john.doe@example.com', 100.00, TRUE, CURRENT_TIMESTAMP),
('JaneSmith', 'jane.smith@example.com', 0, TRUE, CURRENT_TIMESTAMP - INTERVAL '1 day'),
('AliceJohnson', 'alice.johnson@example.com', 50.00, TRUE, CURRENT_TIMESTAMP - INTERVAL '2 days'),
('BobBrown', 'bob.brown@example.com', 200.00, FALSE, CURRENT_TIMESTAMP - INTERVAL '3 days'),
('CharlieWilliams', 'charlie.williams@example.com', 0, TRUE, CURRENT_TIMESTAMP - INTERVAL '4 days');

-- widok edytowalny
CREATE VIEW editable_account AS
SELECT account_id, username,email,balance,created_at
FROM accounts
WHERE is_active = TRUE AND balance >0
WITH LOCAL CHECK OPTION;
-- widok tylko do odczytu
CREATE VIEW readonly_view AS
SELECT account_id,username,email,balance,is_active
FROM accounts
WHERE balance=0;
-- widok zmaterializowany
CREATE MATERIALIZED VIEW materailized_accounts AS
SELECT account_id, username,email,balance,is_active,created_at
FROM accounts
WHERE is_active = TRUE AND balance >50
WITH DATA;

SELECT * FROM materailized_accounts;

INSERT INTO accounts(username,email,balance,is_active)
VALUES('new_user','new@example.com',100.00,TRUE);

REFRESH MATERIALIZED VIEW materailized_accounts;

--UPDATE NA WIDOKU editable_account
UPDATE editable_account
SET balance=balance-50
WHERE username='JohnDoe';

 -- update ale błąd:        ERROR:  new row violates check option for view "editable_account"           DETAIL:  Failing row contains (1, JohnDoe, john.doe@example.com, 0.00, t, 2024-12-19 08:42:44.139557).
UPDATE editable_account
SET balance=0
WHERE username='JohnDoe';

-- proba modyfikacji danych na widoku readonly : ERROR:  cannot update view "readonly_view" DETAIL:  Views containing DISTINCT are not automatically updatable.     HINT:  To enable updating the view, provide an INSTEAD OF UPDATE trigger or an unconditional ON UPDATE DO INSTEAD rule.

UPDATE readonly_view
SET balance=10
WHERE username='JaneSmith';


-- cykliczne odswierzanie widoku zmaterializowego wykorzystując(CRON w systemie operacyjnym lub PostgreSQL pg_cron)
CREATE MATERIALIZED VIEW materailized_accounts WITH
(
  refresh_interval = '24h',
  grace_period = '5m',
  max_import_duration = '30m'
)AS
SELECT account_id, username,email,balance,is_active,created_at
FROM accounts
WHERE is_active = TRUE AND balance >50
