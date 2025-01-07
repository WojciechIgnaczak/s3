# Typy danych
# Typy numeryczne
| Name            | Storage Size | Description                                | Range                                                |
|-----------------|--------------|--------------------------------------------|------------------------------------------------------|
| smallint        | 2 bytes      | small-range integer                        | -32768 to +32767                                     |
| integer         | 4 bytes      | typical choice for integer                 | -2147483648 to +2147483647                          |
| bigint          | 8 bytes      | large-range integer                        | -9223372036854775808 to +9223372036854775807        |
| decimal         | variable     | user-specified precision, exact            | up to 131072 digits before the decimal point; up to 16383 digits after the decimal point |
| numeric         | variable     | user-specified precision, exact            | up to 131072 digits before the decimal point; up to 16383 digits after the decimal point |
| real            | 4 bytes      | variable-precision, inexact                | 6 decimal digits precision                          |
| double precision| 8 bytes      | variable-precision, inexact                | 15 decimal digits precision                         |
| smallserial     | 2 bytes      | small autoincrementing integer             | 1 to 32767                                           |
| serial          | 4 bytes      | autoincrementing integer                   | 1 to 2147483647                                      |
| bigserial       | 8 bytes      | large autoincrementing integer             | 1 to 9223372036854775807                            |

# Typy monetarne (pieniądze)
| Name            | Storage Size | Description                                | Range                                                |
|-----------------|--------------|--------------------------------------------|------------------------------------------------------|
| money           | 8 bytes      | currency amount                            | -92233720368547758.08 to +92233720368547758.07      |

# Typy tekstowe
| Name                      | Description                          |
|---------------------------|--------------------------------------|
| character varying(n), varchar(n) | variable-length with limit          |
| character(n), char(n), bpchar(n)  | fixed-length, blank-padded          |
| bpchar                    | variable unlimited length, blank-trimmed |
| text                      | variable unlimited length            |

# Typy binarne
| Name   | Storage Size                               | Description                |
|--------|--------------------------------------------|----------------------------|
| bytea  | 1 or 4 bytes plus the actual binary string | variable-length binary string |

# Typy daty/czasu
| Name                                      | Storage Size | Description                                   | Low Value             | High Value            | Resolution      |
|-------------------------------------------|--------------|-----------------------------------------------|-----------------------|-----------------------|-----------------|
| timestamp [ (p) ] [ without time zone ]   | 8 bytes      | both date and time (no time zone)             | 4713 BC               | 294276 AD             | 1 microsecond   |
| timestamp [ (p) ] with time zone          | 8 bytes      | both date and time, with time zone            | 4713 BC               | 294276 AD             | 1 microsecond   |
| date                                      | 4 bytes      | date (no time of day)                         | 4713 BC               | 5874897 AD            | 1 day           |
| time [ (p) ] [ without time zone ]        | 8 bytes      | time of day (no date)                        | 00:00:00              | 24:00:00              | 1 microsecond   |
| time [ (p) ] with time zone               | 12 bytes     | time of day (no date), with time zone         | 00:00:00+1559         | 24:00:00-1559         | 1 microsecond   |
| interval [ fields ] [ (p) ]               | 16 bytes     | time interval                                 | -178000000 years      | 178000000 years       | 1 microsecond   |

# Typy bool'owskie
| Name    | Storage Size | Description               |
|---------|--------------|---------------------------|
| boolean | 1 byte       | state of true or false    |

# Typy enumeryczne
```sql
CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy');
CREATE TABLE person (
    name text,
    current_mood mood
);
INSERT INTO person VALUES ('Moe', 'happy');
SELECT * FROM person WHERE current_mood = 'happy';
 name | current_mood
------+--------------
 Moe  | happy
```
# Typy geometryczne
| Name    | Storage Size       | Description                      | Representation        |
|---------|--------------------|----------------------------------|-----------------------|
| point   | 16 bytes           | Point on a plane                 | (x,y)                 |
| line    | 24 bytes           | Infinite line                    | {A,B,C}               |
| lseg    | 32 bytes           | Finite line segment              | [(x1,y1),(x2,y2)]     |
| box     | 32 bytes           | Rectangular box                  | (x1,y1),(x2,y2)       |
| path    | 16+16n bytes       | Closed path (similar to polygon) | ((x1,y1),...)         |
| path    | 16+16n bytes       | Open path                        | [(x1,y1),...]         |
| polygon | 40+16n bytes       | Polygon (similar to closed path) | ((x1,y1),...)         |
| circle  | 24 bytes           | Circle                           | <(x,y),r> (center point and radius) |

# Typy adresów internetowych
| Name      | Storage Size | Description                        |
|-----------|--------------|------------------------------------|
| cidr      | 7 or 19 bytes| IPv4 and IPv6 networks             |
| inet      | 7 or 19 bytes| IPv4 and IPv6 hosts and networks  |
| macaddr   | 6 bytes      | MAC addresses                      |
| macaddr8  | 8 bytes      | MAC addresses (EUI-64 format)      |

# Typy pozostałe 
- Typy wyszukiwania tekstowego (tsvector, tsquery)
- Typ UUID
- Typ XML
- Typ JSON (string, number, boolean, null)
- Typ tablicowy
```sql
CREATE TABLE sal_emp (
    name            text,
    pay_by_quarter  integer[],
    schedule        text[][]
);
```
