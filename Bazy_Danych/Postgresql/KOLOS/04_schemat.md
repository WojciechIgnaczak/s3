# Schematy

## Tworzenie, usuwanie schematu
```sql
CREATE SCHEMA myschema;
DROP SCHEMA myschema;

```
Aby uzyskać dostęp do obiektów w schemacie, należy wpisać kwalifikowaną nazwę:
`schema.table` lub bardziej ogólną `database.schema.table`

## Tworzenie tabeli na schemacie
```sql
CREATE TABLE myschema.mytable (
 ...
);
```
Aby usunąć schemat z wszystkimi obiektami w nim zawartymi
```sql
DROP SCHEMA myschema CASCADE;
```

Aby utworzyć schemat należący do kogoś innego
```sql
CREATE SCHEMA schema_name AUTHORIZATION user_name;
```

Wykorzystanie schematów:

- kontrola autoryzacji

- organizacja obiektów bazy danych

- utrzymywanie zewnętrznego kodu SQL

Utworzenie schematu dla takiej samej roli (2), w (1) można zmienić na inną rolę
```sql
CREATE SCHEMA car_portal_app AUTHORIZATION car_portal_app 

CREATE SCHEMA AUTHORIZATION car_portal_app 
```
