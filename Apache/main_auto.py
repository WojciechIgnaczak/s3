from pyignite import Client
from dane_z_pesel import day_of_birth, month_of_birth_number,sex, year_of_birth
from klasy import Pacjent, Wizyta, Recepta, Skierowanie,odbuduj_pacjenta
from zapis_odczyt import dodaj_pacjenta, odczytaj_pacjenta
import json
from datetime import datetime
import sys
client = Client()
client.connect('127.0.0.1', 10800)
pacjent_cache = client.get_or_create_cache('pacjentCache')

    ############################################## Dodanie pacjenta
while True:
    print("Co chcesz zrobić?")
    print("1. Dodaj pacjenta")
    print("2. Dodaj wizytę")
    print("3. Dodaj receptę")
    print("4. Dodaj skierowanie")
    print("5. Odczytaj pacjenta")
    print("6. Wyjdź")
    choice = input("Wybierz opcję (1-6): ")

    if choice == '6':
        print("Koniec programu.")
        client.close()
        sys.exit()
    elif choice not in ['1', '2', '3', '4', '5']:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        continue
    ############################################## Dodanie pacjenta
    if choice == '1':
        pesel = input("Podaj PESEL pacjenta: ")
        imie = input("Podaj imię pacjenta: ")
        imie2 = input("Podaj drugie imię pacjenta: ")
        nazwisko =  input("Podaj nazwisko pacjenta: ")
        adres =     input("Podaj adres pacjenta: ")
        telefon =   input("Podaj telefon pacjenta: ")
        dodaj_pacjenta(pacjent_cache, pesel, imie, imie2, nazwisko, adres, telefon)

    ############################################## Dodanie wizyty
    if choice == '2':
        pesel = input("Podaj PESEL pacjenta: ")
        json_data = pacjent_cache.get(pesel)
        if json_data is None:
            print("Pacjent o podanym PESEL nie istnieje.")
            continue

        pacjent_data = json.loads(json_data)
        data_wizyty = datetime.now().strftime("%d-%m-%Y")
        lekarz = input("Podaj lekarza: ")
        opis = input("Podaj opis wizyty: ")
        zalecenia = input("Podaj zalecenia: ")
        wizyta = Wizyta(data_wizyty, lekarz, opis, zalecenia)
        pacjent = odbuduj_pacjenta(pacjent_data)

        pacjent.dodaj_wizyte(wizyta)
        pacjent_cache.put(pesel, json.dumps(pacjent.to_dict(), ensure_ascii=False))

        ############################################## Dodanie recepty
    if choice == '3':
        pesel = input("Podaj PESEL pacjenta: ")
        json_data = pacjent_cache.get(pesel)
        if json_data is None:
            print("Pacjent o podanym PESEL nie istnieje.")
            continue

        pacjent_data = json.loads(json_data)
        data_recepty = datetime.now().strftime("%d-%m-%Y")
        lekarz = input("Podaj lekarza: ")
        leki = input("Podaj leki (oddzielone przecinkiem): ").split(",")
        recepta = Recepta(data_recepty,lekarz, leki)
        pacjent = odbuduj_pacjenta(pacjent_data)

        pacjent.dodaj_recepte(recepta)
        pacjent_cache.put(pesel, json.dumps(pacjent.to_dict(), ensure_ascii=False))

        ############################################## Dodanie skierowania do pacjenta
    if choice == '4':
        pesel = input("Podaj PESEL pacjenta: ")
        json_data = pacjent_cache.get(pesel)
        if json_data is None:
            print("Pacjent o podanym PESEL nie istnieje.")
            continue
        pacjent_data = json.loads(json_data)
        data_skierowania = datetime.now().strftime("%d-%m-%Y")
        lekarz = input("Podaj lekarza: ")
        opis = input("Podaj opis skierowania: ")
        skierowanie = Skierowanie(data_skierowania,lekarz, opis)
        pacjent = odbuduj_pacjenta(pacjent_data)

        pacjent.dodaj_skierowanie(skierowanie)
        pacjent_cache.put(pesel, json.dumps(pacjent.to_dict(), ensure_ascii=False))
        
        ############################################### Odczyt pacjenta i wypisanie
    if choice == '5':
        print("\nOdczyt pacjenta z cache:")
        pesel = input("Podaj PESEL pacjenta: ")
        if json_data is None:
            print("Pacjent o podanym PESEL nie istnieje.")
            continue
        odczytaj_pacjenta(pacjent_cache, pesel)
    