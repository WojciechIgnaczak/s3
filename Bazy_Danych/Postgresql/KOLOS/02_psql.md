
# Podstawa
### Logowanie do postgreSQL
```
sudo -i -u user_name
```
### Wylogowanie z postgreSQL
```
exit
```
### Wejście do psql
```
psql

psql -U user_name -d nazwa_bazy -h host -p port   

psql -U użytkownik -d baza_danych -h 192.168.1.100 -p 5432

```
Host domyślnie **localhost**

Port domyślnie **5432**

Nie trzeba wykorzystywać wszystkich parametrów jeśli są domyślne


# Polecenia w terminalu (nie w psql)

### Usuwanie istniejącej bazy danych PostgreSQL
```
dropdb nazwa_bazy;
```

### Tworzenie nowej  bazy danych PostgreSQL
```
createdb nazwa_bazy;
```

### Usuwanie usera
```
dropuser name
```
### Tworzenie usera
```
createuser name
```

### Tworzy ponownie indeksy
```
reindexdb
```

# PostgreSQL `psql` Commands

## General Commands
| Command                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| \bind [PARAM]...         | Ustawienie parametrów zapytania                                                     |
| \copyright               | Wyświetlenie warunków użytkowania i dystrybucji PostgreSQL                               |
| \crosstabview [COLUMNS]  | Wykonanie zapytania i wyświetlenie wyników w formie tabeli przestawnej                               |
| \errverbose              | Wyświetlenie ostatniego komunikatu o błędzie z maksymalną szczegółowością                      |
| \g [(OPTIONS)] [FILE]    | Wykonaj zapytanie (i wyślij wynik do pliku lub \|pipe); \g bez argumentów jest równoważne średnikowi |
| \gdesc                   | Opisanie wyniku zapytania bez jego wykonania                             |
| \gexec                   | Wykonanie zapytania, a następnie wykonanie każdego wyniku z tego zapytania                     |
| \gset [PREFIX]           | Wykonanie zapytania i zapisanie wyniku w zmiennych psql                          |
| \gx [(OPTIONS)] [FILE]   | Jak \g, ale wymusza rozszerzony tryb wyjściowy                                    |
| \q                       | Zakończenie sesji psql                                                             |
| \watch [[i=]SEC] [c=N]   | Wykonanie zapytania co SEC sekund, do N razy                           |

## Help Commands
| Command                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| \\? [commands]            | Wyświetlenie pomocy dla komend backslash, pokazuje wszystkie komendy po \\   |
| \\? options               | Wyświetlenie pomocy dla opcji wiersza poleceń psql                                       |
| \\? variables             | 	Wyświetlenie pomocy dla zmiennych specjalnych                                         |
| \\h [NAME]                | Pomoc dotycząca składni komend SQL, * dla wszystkich komend                        |

## Query Buffer Commands
| Command                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| \e [FILE] [LINE]         | Edytowanie bufora zapytania (lub pliku) za pomocą zewnętrznego edytora                        |
| \ef [FUNCNAME [LINE]]    | Edytowanie definicji funkcji za pomocą zewnętrznego edytora                               |
| \ev [VIEWNAME [LINE]]    | Edytowanie definicji widoku za pomocą zewnętrznego edytora                                   |
| \p                       | Wyświetlenie zawartości bufora zapytania                                       |
| \r                       | Zresetowanie (wyczyszczenie) bufora zapytania                                              |
| \s [FILE]                | Wyświetlenie historii lub zapisanie jej do pliku                                        |
| \w FILE                  | Zapisanie bufora zapytania do pliku                                                |

## Input/Output Commands
| Command                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| \copy ...                | Wykonanie komendy SQL COPY z danymi przesyłanymi do klienta                         |
| \echo [-n] [STRING]      | Zapisanie ciągu znaków do standardowego wyjścia (-n dla braku nowej linii)                        |
| \i FILE                  | Wykonanie komend z pliku                                                  |
| \ir FILE                 | Jak \i, ale w odniesieniu do lokalizacji bieżącego skryptu                           |
| \o [FILE]                | Wysłanie wyników zapytania do pliku lub \p                                      |
| \qecho [-n] [STRING]     | Zapisanie ciągu znaków do strumienia \o (-n dla braku nowej linii)                        |
| \warn [-n] [STRING]      | Zapisanie ciągu znaków do standardowego błędu (-n dla braku nowej linii)                       |

## Conditional Commands
| Command                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| \if EXPR                 | Rozpoczęcie bloku warunkowego                                                     |
| \elif EXPR               | Alternatywa w bieżącym bloku warunkowym                                 |
| \else                    | Ostatnia alternatywa w bieżącym bloku warunkowym                           |
| \endif                   | Zakończenie bloku warunkowego                                                       |

## Informational Commands
| Command                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| \d[S+]                   | Wyświetl tabelę, widok, sekwencję                                           |
| \d[S+]  NAME             | Opis tabeli, widoku, sekwencji lub indeksu                                    |
| \da[S]  [PATTERN]        | Wyświetl agregaty                                                             |
| \dA[+]  [PATTERN]        | Wyświetl metody dostępu                                                         |
| \dAc[+] [AMPTRN [TYPEPTRN]] | Wyświetl klasy operatorów                                                   |
| \dAf[+] [AMPTRN [TYPEPTRN]] | Wyświetl rodziny operatorów                                                   |
| \dAo[+] [AMPTRN [OPFPTRN]]  | Wyświetl operatory rodzin operatorów                                      |
| \dAp[+] [AMPTRN [OPFPTRN]]  | Wyświetl funkcje wspierające rodziny operatorów                               |
| \db[+]  [PATTERN]        | Wyświetl przestrzenie tabel                                                           |
| \dc[S+] [PATTERN]        | Wyświetl konwersje                                                           |
| \dconfig[+] [PATTERN]    | Wyświetl parametry konfiguracyjneameters                                              |
| \dC[+]  [PATTERN]        | Wyświetl rzutowania                                                                  |
| \dd[S]  [PATTERN]        | Wyświetl opisy obiektów, które nie są wyświetlane w innych miejscach                            |
| \dD[S+] [PATTERN]        | Wyświetl domeny                                                               |
| \ddp    [PATTERN]        | Wyświetl domyślne uprawnienia                                                    |
| \dE[S+] [PATTERN]        | Wyświetl tabele zewnętrzne                                                        |
| \des[+] [PATTERN]        | Wyświetl serwery zewnętrzne                                                       |
| \det[+] [PATTERN]        | Wyświetl tabele zewnętrzne                                                        |
| \deu[+] [PATTERN]        | Wyświetl mapowania użytkowników                                                         |
| \dew[+] [PATTERN]        | Wyświetl opakowania danych zewnętrznych                                                 |
| \df[anptw][S+] [FUNCPTRN [TYPEPTRN ...]] | Wyświetl funkcje (agregatowe, normalne, procedury, wyzwalacze, okna).          |
| \dF[+]  [PATTERN]        | Wyświetl konfiguracje wyszukiwania tekstu                                            |
| \dFd[+] [PATTERN]        | Wyświetl słowniki wyszukiwania tekstu                                               |
| \dFp[+] [PATTERN]        | Wyświetl analizatory wyszukiwania tekstu                                                   |
| \dFt[+] [PATTERN]        | Wyświetl szablony wyszukiwania tekstu                                                 |
| \dg[S+] [PATTERN]        | Wyświetl role.                                                                  |
| \di[S+] [PATTERN]        | Wyświetl indeksy                                                                |
| \dl[+]                   | Wyświetl obiekty duże, takie jak w \lo_list                                      |
| \dL[S+] [PATTERN]        | Wyświetl języki proceduralne                                                  |
| \dm[S+] [PATTERN]        | Wyświetl widoki materializowane                                                    |
| \dn[S+] [PATTERN]        | Wyświetl schematy                                                                |
| \do[S+] [OPPTRN [TYPEPTRN [TYPEPTRN]]] | Wyświetl operatory                                                      |
| \dO[S+] [PATTERN]        | Wy swietl zestawienia                                                            |
| \dp[S]  [PATTERN]        | Wyświetl uprawnienia dostępu do tabel, widoków i sekwencji                           |
| \dP[itn+] [PATTERN]      | Wyświetl [tylko indeksy/tabele] zagnieżdżone w partycjach [n=nested]                    |
| \drds [ROLEPTRN [DBPTRN]]| Wyświetl ustawienia ról dla bazy danych                                            |
| \drg[S] [PATTERN]        | Wyświetl przyznane uprawnienia do ról                                                           |
| \dRp[+] [PATTERN]        |  Wyświetl publikacje replikacji                                              |
| \dRs[+] [PATTERN]        | Wyświetl subskrypcje replikacji                                             |
| \ds[S+] [PATTERN]        | Wyświetl sekwencje                                                             |
| \dt[S+] [PATTERN]        | Wyświetl tabele                                                                |
| \dT[S+] [PATTERN]        | Wyświetl typy danych                                                            |
| \du[S+] [PATTERN]        | Wyświetl role                                                                  |
| \dv[S+] [PATTERN]        | Wyświetl widoki                                                                  |
| \dx[+]  [PATTERN]        | Wyświetl rozszerzenia                                                             |
| \dX     [PATTERN]        | Wyświetl statystyki rozszerzone                                                   |
| \dy[+]  [PATTERN]        | Wyświetl wyzwalacze zdarzeń triggers                                                        |
| \l[+]   [PATTERN]        | Wyświetl bazy danych                                                             |
| \sf[+]  FUNCNAME         | Wyświetl definicję funkcji                                                |
| \sv[+]  VIEWNAME         | Wyświetl definicję widoku                                                   |
| \z[S]   [PATTERN]        | To samo, co \dp (uprawnienia dostępu).                                                            |

## Large Objects Commands
| Command                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| \lo_export LOBOID FILE   | Zapisz duży obiekt do pliku                                                  |
| \lo_import FILE [COMMENT]| Wczytaj duży obiekt z pliku                                                 |
| \lo_list[+]              | Wyświetl duże obiekty                                                          |
| \lo_unlink LOBOID        | Usuń duży obiekt                                                       |

## Formatting Commands
| Command                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| \a                       | Przełącz między wyjściem w formacie niezsynchronizowanym i zsynchronizowanym                                |
| \C [STRING]              | Ustaw tytuł tabeli lub usuń, jeśli brak                                           |
| \f [STRING]              | Ustaw lub wyświetl separator pól w wyjściu niezsynchronizowanym                     |
| \H                       | Przełącz tryb wyjścia w formacie HTML                                     |
| \pset [NAME [VALUE]]     | Ustaw opcje wyjścia tabeli (np. granice, kolumny, format CSV).|
| \t [on\|off]              | Pokaż tylko wiersze (domyślnie wyłączone).                                             |
| \T [STRING]              | Ustaw atrybuty znacznika HTML \<table\>, lub wyłącz je, jeśli nie są ustawione                          |
| \x [on\|off\|auto]         | Przełącz rozszerzone wyjście. (domyślnie wyłączone)                                      |

## Connection Commands
| Command                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| \c[onnect] {[DBNAME\|- USER\|- HOST\|- PORT\|-] \| conninfo} | Połączenie z nową bazą danych (domyślnie "postgres") |
| \conninfo                | Wyświetlenie informacji o bieżącym połączeniu                                |
| \encoding [ENCODING]     | Pokazanie lub ustawienie kodowania klienta                                                 |
| \password [USERNAME]     | Zmiana hasła użytkownika w sposób bezpieczny                                      |

## Operating System Commands
| Command                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| \cd [DIR]                | Zmiana bieżącego katalogu roboczego                                        |
| \getenv PSQLVAR ENVVAR   | Pobranie zmiennej środowiskowej                                                   |
| \setenv NAME [VALUE]     | Ustawienie lub usunięcie zmiennej środowiskowej                                           |
| \timing [on\|off]         | Przełączanie wyświetlania czasu wykonania komend (obecnie wyłączone)                                   |
| \! [COMMAND]             | Wykonanie polecenia w powłoce lub uruchomienie interaktywnej powłoki                    |

## Variable Commands
| Command                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| \prompt [TEXT] NAME      | Monitoruj użytkownika o ustawienie zmiennej wewnętrznej                                        |
| \set [NAME [VALUE]]      | Ustaw zmienną wewnętrzną lub wypisz wszystkie, jeśli nie ma parametrów                          |
| \unset NAME              | usuń zmienną wewnętrzną                                            |

```sql
\set nazwa_wartosci 'wartosc' -- tworzenie zmiennej
SELECT * FROM users WHERE username = :'nazwa_wartosci'; -- użycie w zapytaniu

```

## Aliases
```sql
\alias ll \! ls -l

\alias mytables \dt public.*
```
alias **ll** - wyświela nam wszystkie pliki

alias **mytables** - wyświetla nam wszystkie tabele w schemacie

