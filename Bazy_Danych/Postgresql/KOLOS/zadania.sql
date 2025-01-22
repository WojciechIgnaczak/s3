### **Zadanie 1: System zarządzania projektami**
#### **Cel:**
Utwórz system do zarządzania projektami, który zawiera:
- Tabelę do przechowywania danych o projektach.
- Tabelę do przechowywania danych o zadaniach w projektach.
- Widok pokazujący podsumowanie projektów z liczbą zadań w każdym projekcie.
- Procedurę, która pozwala na dodanie nowego projektu z zadaniami.

#### **Wymagania:**
1. Utwórz tabelę `projects` z kolumnami:
   - `id` (klucz główny, numer seryjny),
   - `name` (nazwa projektu),
   - `created_at` (data utworzenia projektu).

2. Utwórz tabelę `tasks` z kolumnami:
   - `id` (klucz główny, numer seryjny),
   - `project_id` (klucz obcy do `projects`),
   - `task_name` (nazwa zadania),
   - `status` (status zadania, np. TODO, IN_PROGRESS, DONE).

3. Utwórz widok `project_summary`, który pokazuje:
   - `id` projektu,
   - nazwę projektu,
   - liczbę zadań w projekcie,
   - liczbę ukończonych zadań.

4. Utwórz procedurę `add_project_with_tasks`, która:
   - Przyjmuje nazwę projektu i listę zadań.
   - Dodaje projekt i przypisuje do niego zadania.

---


CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    project_id INT REFERENCES projects(id) ON DELETE CASCADE,
    task_name TEXT NOT NULL,
    status TEXT DEFAULT 'TODO'
);

CREATE VIEW project_summary AS
SELECT 
    p.id AS project_id,
    p.name AS project_name,
    COUNT(t.id) AS total_tasks,
    COUNT(CASE WHEN t.status = 'DONE' THEN 1 END) AS completed_tasks
FROM 
    projects p
LEFT JOIN 
    tasks t ON p.id = t.project_id
GROUP BY 
    p.id, p.name;

CREATE PROCEDURE add_project_with_tasks(project_name TEXT, task_list TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    project_id INT;
BEGIN
    INSERT INTO projects(name) VALUES (project_name) RETURNING id INTO project_id;
    FOREACH task_name IN ARRAY task_list LOOP
        INSERT INTO tasks(project_id, task_name) VALUES (project_id, task_name);
    END LOOP;
END;
$$;

### **Zadanie 2: Zarządzanie magazynem**
#### **Cel:**
Utwórz system zarządzania magazynem, który:
- Przechowuje dane o produktach i zamówieniach.
- Zawiera widok pokazujący aktualny stan magazynowy.
- Funkcję do sprawdzania dostępności produktu.
- Procedurę realizującą zamówienia.

#### **Wymagania:**
1. Utwórz tabelę `products` z kolumnami:
   - `id` (klucz główny, numer seryjny),
   - `name` (nazwa produktu),
   - `stock` (ilość w magazynie),
   - `price` (cena produktu).

2. Utwórz tabelę `orders` z kolumnami:
   - `id` (klucz główny, numer seryjny),
   - `product_id` (klucz obcy do `products`),
   - `quantity` (zamówiona ilość),
   - `order_date` (data zamówienia).

3. Utwórz widok `inventory_status`, który pokazuje:
   - ID produktu,
   - nazwę produktu,
   - ilość w magazynie,
   - całkowitą wartość stanu magazynowego (`stock * price`).

4. Utwórz funkcję `check_availability(product_id INT, quantity INT)`, która sprawdza, czy zamówiona ilość produktu jest dostępna w magazynie.

5. Utwórz procedurę `place_order(product_id INT, quantity INT)`, która:
   - Sprawdza dostępność produktu za pomocą funkcji `check_availability`.
   - Dodaje zamówienie do tabeli `orders`.
   - Aktualizuje ilość `stock` w tabeli `products`.

---

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    stock INT NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id) ON DELETE CASCADE,
    quantity INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE VIEW inventory_status AS
SELECT 
    id AS product_id,
    name AS product_name,
    stock,
    stock * price AS total_value
FROM 
    products;


CREATE FUNCTION check_availability(product_id INT, quantity INT) 
RETURNS BOOLEAN AS $$
DECLARE
    available_stock INT;
BEGIN
    SELECT stock INTO available_stock FROM products WHERE id = product_id;
    RETURN available_stock >= quantity;
END;
$$ LANGUAGE plpgsql;



CREATE PROCEDURE place_order(product_id INT, quantity INT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT check_availability(product_id, quantity) THEN
        RAISE EXCEPTION 'Not enough stock for product ID %', product_id;
    END IF;

    INSERT INTO orders(product_id, quantity) VALUES (product_id, quantity);
    UPDATE products SET stock = stock - quantity WHERE id = product_id;
END;
$$;



### **Zadanie 3: System rejestracji użytkowników**
#### **Cel:**
Utwórz system rejestracji użytkowników z:
- Tabelą przechowującą dane użytkowników.
- Widokiem pokazującym aktywnych użytkowników.
- Funkcją sprawdzającą poprawność adresu e-mail.
- Procedurą rejestracji użytkownika.

#### **Wymagania:**
1. Utwórz tabelę `users` z kolumnami:
   - `id` (klucz główny, numer seryjny),
   - `username` (unikalna nazwa użytkownika),
   - `email` (adres e-mail),
   - `is_active` (flaga aktywności: TRUE/FALSE),
   - `created_at` (data utworzenia konta).

2. Utwórz widok `active_users`, który pokazuje:
   - ID użytkownika,
   - nazwę użytkownika,
   - adres e-mail.

3. Utwórz funkcję `validate_email(email TEXT)`, która:
   - Sprawdza, czy adres e-mail zawiera znak `@` i końcówkę domeny (np. `.com`).

4. Utwórz procedurę `register_user(username TEXT, email TEXT)`, która:
   - Waliduje adres e-mail za pomocą funkcji `validate_email`.
   - Dodaje nowego użytkownika do tabeli `users` z `is_active` ustawionym na TRUE.

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE VIEW active_users AS
SELECT 
    id,
    username,
    email
FROM 
    users
WHERE 
    is_active = TRUE;


CREATE FUNCTION validate_email(email TEXT)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$';
END;
$$ LANGUAGE plpgsql;


CREATE PROCEDURE register_user(username TEXT, email TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT validate_email(email) THEN
        RAISE EXCEPTION 'Invalid email format: %', email;
    END IF;

    INSERT INTO users(username, email) VALUES (username, email);
END;
$$;



---

### **Zadanie 4: System raportowania sprzedaży**
#### **Cel:**
Utwórz system raportowania sprzedaży:
- Przechowuj dane o sprzedaży i produktach.
- Utwórz widok pokazujący miesięczne podsumowanie sprzedaży.
- Utwórz funkcję obliczającą całkowitą sprzedaż dla produktu.
- Utwórz procedurę generującą raport sprzedaży.

#### **Wymagania:**
1. Utwórz tabelę `sales` z kolumnami:
   - `id` (klucz główny, numer seryjny),
   - `product_id` (klucz obcy do tabeli `products`),
   - `quantity` (sprzedana ilość),
   - `sale_date` (data sprzedaży).

2. Utwórz widok `monthly_sales_summary`, który pokazuje:
   - Miesiąc,
   - ID produktu,
   - nazwę produktu,
   - sumę sprzedanych jednostek w danym miesiącu.

3. Utwórz funkcję `get_total_sales(product_id INT)`, która oblicza całkowitą ilość sprzedanego produktu.

4. Utwórz procedurę `generate_sales_report(month INT, year INT)`, która generuje raport sprzedaży dla danego miesiąca i roku, zapisując go w nowej tabeli `sales_report`.

---



CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id) ON DELETE CASCADE,
    quantity INT NOT NULL,
    sale_date DATE DEFAULT CURRENT_DATE
);


CREATE VIEW monthly_sales_summary AS
SELECT 
    DATE_TRUNC('month', sale_date) AS month,
    p.id AS product_id,
    p.name AS product_name,
    SUM(s.quantity) AS total_sold
FROM 
    sales s
JOIN 
    products p ON s.product_id = p.id
GROUP BY 
    month, p.id, p.name;

CREATE FUNCTION get_total_sales(product_id INT)
RETURNS INT AS $$
DECLARE
    total_sales INT;
BEGIN
    SELECT SUM(quantity) INTO total_sales FROM sales WHERE product_id = product_id;
    RETURN COALESCE(total_sales, 0);
END;
$$ LANGUAGE plpgsql;

CREATE PROCEDURE generate_sales_report(month INT, year INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO sales_report
    SELECT 
        DATE_TRUNC('month', sale_date) AS report_month,
        p.id AS product_id,
        p.name AS product_name,
        SUM(s.quantity) AS total_sold
    FROM 
        sales s
    JOIN 
        products p ON s.product_id = p.id
    WHERE 
        EXTRACT(MONTH FROM sale_date) = month AND EXTRACT(YEAR FROM sale_date) = year
    GROUP BY 
        report_month, p.id, p.name;
END;
$$;





### **Zadanie 5: Zarządzanie książkami w bibliotece**
#### **Cel:**
Utwórz system do zarządzania książkami i wypożyczeniami:
- Przechowuj dane o książkach i wypożyczeniach.
- Utwórz widok pokazujący dostępne książki.
- Utwórz funkcję obliczającą czas wypożyczenia.
- Utwórz procedurę obsługującą wypożyczenie książki.

#### **Wymagania:**
1. Utwórz tabelę `books` z kolumnami:
   - `id` (klucz główny, numer seryjny),
   - `title` (tytuł książki),
   - `author` (autor),
   - `is_available` (flaga dostępności: TRUE/FALSE).

2. Utwórz tabelę `borrowings` z kolumnami:
   - `id` (klucz główny, numer seryjny),
   - `book_id` (klucz obcy do tabeli `books`),
   - `borrow_date` (data wypożyczenia),
   - `return_date` (data zwrotu).

3. Utwórz widok `available_books`, który pokazuje wszystkie dostępne książki (`is_available = TRUE`).

4. Utwórz funkcję `calculate_borrow_days(borrow_date DATE, return_date DATE)`, która oblicza liczbę dni wypożyczenia.

5. Utwórz procedurę `borrow_book(book_id INT, borrow_date DATE)`, która:
   - Sprawdza, czy książka jest dostępna.
   - Ustawia `is_available = FALSE` w tabeli `books`.
   - Dodaje wpis do tabeli `borrowings`.

   CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    is_available BOOLEAN DEFAULT TRUE
);


CREATE TABLE borrowings (
    id SERIAL PRIMARY KEY,
    book_id INT REFERENCES books(id) ON DELETE CASCADE,
    borrow_date DATE NOT NULL,
    return_date DATE
);


CREATE VIEW available_books AS
SELECT 
    id AS book_id,
    title,
    author
FROM 
    books
WHERE 
    is_available = TRUE;


CREATE FUNCTION calculate_borrow_days(borrow_date DATE, return_date DATE)
RETURNS INT AS $$
BEGIN
    RETURN return_date - borrow_date;
END;
$$ LANGUAGE plpgsql;



CREATE PROCEDURE borrow_book(book_id INT, borrow_date DATE)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT (SELECT is_available FROM books WHERE id = book_id) THEN
        RAISE EXCEPTION 'Book ID % is not available', book_id;
    END IF;

    UPDATE books SET is_available = FALSE WHERE id = book_id;
    INSERT INTO borrowings(book_id, borrow_date) VALUES (book_id, borrow_date);
END;
$$;



