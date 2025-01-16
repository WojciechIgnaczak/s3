-- tabela do przechowywania danych o  projektach projects
-- id (klucz, serial), name, created_at
CREATE TABLE projects(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



INSERT INTO projects (name) VALUES ('Project A');

INSERT INTO projects (name) VALUES 
('Website Redesign'),
('Mobile App Development'),
('Marketing Campaign'),
('Data Migration Project'),
('E-commerce Platform Upgrade');



-- tabela do przechowywania danych o zadaniach w projektach tasks
-- id, project_id(klucz do project), task name, statuus (todo,inprogress,done)
CREATE TABLE tasks(
    id SERIAL PRIMARY KEY,
    project_id INT NOT NULL references projects(id),
    task_name TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('TODO','IN_PROGRESS','DONE'))
);



INSERT INTO tasks (project_id, task_name, status) 
VALUES (1, 'Task 1', 'TODO');

INSERT INTO tasks (project_id, task_name, status) VALUES 
(1, 'Gather requirements', 'TODO'),
(1, 'Create wireframes', 'IN_PROGRESS'),
(1, 'Develop frontend', 'TODO'),
(2, 'Setup project repository', 'DONE'),
(2, 'Create API documentation', 'IN_PROGRESS'),
(2, 'Integrate payment gateway', 'TODO'),
(3, 'Define marketing goals', 'DONE'),
(3, 'Prepare social media posts', 'TODO'),
(4, 'Backup old database', 'DONE'),
(4, 'Setup new database server', 'IN_PROGRESS'),
(4, 'Migrate data to new server', 'TODO'),
(5, 'Update product catalog', 'TODO'),
(5, 'Optimize checkout flow', 'IN_PROGRESS'),
(5, 'Perform load testing', 'TODO');



--widok pokazujący podsumowanie projektów z liczbą zadań w każdym projekcie project_summary
-- id projektu, nnazwe projektu, liczba zadan w projekcie, liczba ukonczonych zadan
CREATE OR REPLACE VIEW project_summary AS(
    SELECT 
    p.id, 
    p.name as "project name", 
    COUNT(t.id) as "number of tasks", 
    SUM(CASE WHEN t.status='DONE' THEN 1 ELSE 0 END) as "number of done tasks"
    FROM projects p 
    JOIN tasks t ON t.project_id = p.id
    GROUP BY p.id
    ORDER BY p.id
);



-- procedure ktora pozwala na dodanie nowego projektu z zadaniami-- przyjmuje nazwe projektu i liste zadan, dodaje projekt i przypisuje do niego zadania. add_project_with_tasks
CREATE OR REPLACE PROCEDURE add_project_with_tasks (project_name TEXT, task_list TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
project_id INT;
task_name TEXT;
BEGIN
    INSERT INTO projects(name) VALUES (project_name) RETURNING id INTO project_id;

    FOREACH task_name IN ARRAY task_list
    LOOP
        INSERT INTO tasks(task_name, project_id,status) VALUES (task_name,project_id,'TODO');
    END LOOP;
END;
$$;

CALL add_project_with_tasks('Projekt1', ARRAY['zadanie1','zadanie2']);








-- ZADANIE 2    ZARZĄDZANIE MAGAZYNEM   
-- przechowuje dane o produktach i zamowieniach
-- zawiera widok pokazujacy aktualny stan magazynowy
-- funkcj asprawdzanie dostepnosc produktu
-- procedura realizujaca zamowieniach

-- tabela  products(id serial key, name, stock, price)
CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    stock INT NOT NULL CHECK (stock >0),
    price NUMERIC NOT NULL CHECK (price >0)
);

INSERT INTO products (name, stock, price) VALUES
('Laptop', 50, 4500.00),
('Smartphone', 100, 1500.00),
('Headphones', 200, 200.00),
('Keyboard', 150, 100.00),
('Monitor', 75, 800.00);

-- tabela orders(id, product_id, quantity, orderdate)
CREATE TABLE orders(
    id SERIAL PRIMARY KEY,
(4, 10), -- Keyboard, 10 sztuk
(5, 3),  -- Monitor, 3 sztuki
(1, 1),  -- Laptop, 1 sztuka
(3, 2),  -- Headphones, 2 sztuki
(2, 4),  -- Smartphone, 4 sztuki
(4, 6),  -- Keyboard, 6 sztuk
(5, 2);  -- Monitor, 2 sztuki

-- widok inventory_status(id produktu, nazwa produktu, ilosc w magazynie, całkowit a wartosc stanu magazynowego stock*price)
CREATE VIEW inventory_status AS
(
    SELECT p.id, p.name, p.stock, p.stock*p.price AS "wartosc" FROM products p
);

-- funkcja check_availability(product_id INT, quantity INT), która sprawdza czy zamówiona ilość jest dostępna w magazynie
CREATE OR REPLACE FUNCTION check_availability(product_id INT, quantity INT) 
RETURNS BOOLEAN AS $$
DECLARE
    stock_ INT;
BEGIN
    SELECT stock INTO stock_ FROM products WHERE id = product_id;
    
    IF stock_ >= quantity THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- procedura place_order(product_id INT, quantity INT), która sprawdza dostępność produktu za pomocą funckji check_availability, dodaje zamówienie do tabeli orders, aktualizuje stock w tabeli products
CREATE OR REPLACE PROCEDURE place_order(product1_id INT, quantity1 INT)
LANGUAGE plpgsql
AS $$
DECLARE 
    available boolean;
BEGIN
    available:= check_availability(product1_id,quantity1);
    IF available THEN
        INSERT INTO orders(product_id, quantity) VALUES
        (product1_id, quantity1);
        UPDATE products SET stock= stock-quantity1 WHERE id=product1_id;
    ELSE
    END IF;
END;
$$;

CALL place_order(1, 1);  
