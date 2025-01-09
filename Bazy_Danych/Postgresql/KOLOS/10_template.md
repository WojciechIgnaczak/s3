# Template
# Template 0
`Template0` to specjalny szablon, który zawiera minimalną konfigurację bazy danych, bez dodatkowych rozszerzeń i zmian, które mogłyby być dodane do `template1`.
- Cel: template0 zapewnia czystą bazę danych, bez żadnych rozszerzeń ani dodatkowych obiektów.
- Zakaz modyfikacji: Nie można zmieniać zawartości template0. Jest to czysta baza danych, której zawartość jest stała.
- Przeznaczenie: Używa się jej, gdy chcesz, aby nowa baza danych była absolutnie czysta, bez żadnych rozszerzeń, które mogą być obecne w template1.

Przykład utworzenia bazy danych na  podstawie template0
```sql
CREATE DATABASE nowa_baza TEMPLATE template0;
```

template0:

- Zawiera minimalną konfigurację.
- Nie zawiera rozszerzeń ani dodatkowych obiektów.
- Jest w pełni czysta i niezmieniana po zainstalowaniu PostgreSQL.


# Template 1
`Template1` to standardowy szablon, który zawiera wszystkie rozszerzenia i modyfikacje, które zostały dodane do systemu przez administratorów lub przez samego użytkownika.

- Cel: `template1` jest domyślnym szablonem do tworzenia nowych baz danych. Zawiera ona domyślną konfigurację, rozszerzenia i inne zmiany, które zostały wprowadzone po instalacji PostgreSQL.
- Modyfikacja: Można wprowadzać zmiany w `template1`. Na przykład, instalowanie rozszerzeń w `template1` spowoduje, że te rozszerzenia będą również obecne w nowych bazach danych tworzonych na jej podstawie.
- Przeznaczenie: Jeśli chcesz, aby nowa baza zawierała te same rozszerzenia i konfiguracje co `template1`, to jest to odpowiedni wybór.

Przykład utworzenia bazy danych na  podstawie `template1`
```sql
CREATE DATABASE nowa_baza;

```
`Template1` jest używana domyślnie, jeśli nie podasz jawnie szablonu podczas tworzenia nowej bazy danych.

template1:

- Zawiera rozszerzenia, takie jak pg_stat_statements i inne, które mogą być dodane przez administratorów.
- Jest modyfikowana przez użytkowników, którzy chcą, aby wszystkie nowe bazy danych dziedziczyły te zmiany.
- Jest używana jako domyślny szablon dla nowych baz danych.

Kiedy wprowadzisz zmiany do bazy `template1`, na przykład zainstalujesz nowe rozszerzenie, nowe bazy danych utworzone na podstawie `template1` będą miały te zmiany.

