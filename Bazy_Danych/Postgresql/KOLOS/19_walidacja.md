Aby przeprowadzić walidację w PostgreSQL dla różnych danych, takich jak PESEL, email, hasło i login, można użyć różnych metod, takich jak wyrażenia regularne lub ograniczenia (CHECK), aby upewnić się, że dane spełniają odpowiednie kryteria. Oto przykłady:

1. PESEL:
PESEL składa się z 11 cyfr i ma określoną strukturę, którą można sprawdzić za pomocą wyrażenia regularnego. Można go walidować w PostgreSQL za pomocą CHECK z wyrażeniem regularnym.

sql
Kopiuj
Edytuj
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    pesel CHAR(11),
    CONSTRAINT valid_pesel CHECK (pesel ~ '^\d{11}$')
);
To wyrażenie sprawdza, czy PESEL składa się dokładnie z 11 cyfr.

2. Email:
Aby zwalidować poprawność adresu e-mail, używa się wyrażenia regularnego, które sprawdza, czy e-mail ma odpowiednią strukturę.

sql
Kopiuj
Edytuj
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);
Wyrażenie regularne sprawdza, czy e-mail zawiera litery, cyfry, znak @, oraz domenę z rozszerzeniem.

3. Hasło:
Aby walidować hasło, np. sprawdzając, czy zawiera co najmniej 8 znaków, przynajmniej jedną cyfrę, dużą literę oraz znak specjalny, użyj wyrażenia regularnego:

sql
Kopiuj
Edytuj
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    password VARCHAR(255),
    CONSTRAINT valid_password CHECK (password ~* '^(?=.*\d)(?=.*[A-Z])(?=.*[\W_]).{8,}$')
);
To wyrażenie zapewnia, że hasło będzie miało co najmniej 8 znaków, jedną cyfrę, jedną dużą literę oraz jeden znak specjalny.

4. Login:
Login może zawierać tylko litery i cyfry i mieć długość od 3 do 20 znaków. Można to sprawdzić następująco:

sql
Kopiuj
Edytuj
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    login VARCHAR(20),
    CONSTRAINT valid_login CHECK (login ~ '^[A-Za-z0-9]{3,20}$')
);