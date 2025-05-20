from dane_z_pesel import day_of_birth, month_of_birth_number
from klasy import Pacjent, Wizyta, Recepta, Skierowanie
import json
from pyignite import Client
def dodaj_pacjenta(pacjent_cache, pesel, imie, imie2=None, nazwisko=None, adres=None, telefon=None,
                   wizyty=None, recepty=None, skierowania=None):
    pacjent = Pacjent(
        pesel=pesel,
        imie=imie,
        imie2=imie2,
        nazwisko=nazwisko,
        adres=adres,
        telefon=telefon
    )

    if wizyty:
        for w in wizyty:
            pacjent.dodaj_wizyte(w)
    if recepty:
        for r in recepty:
            pacjent.dodaj_recepte(r)
    if skierowania:
        for s in skierowania:
            pacjent.dodaj_skierowanie(s)

    pacjent_cache.put(pesel, json.dumps(pacjent.to_dict(), ensure_ascii=False))


def odczytaj_pacjenta(pacjent_cache, pesel):
    json_data = pacjent_cache.get(pesel)

    if json_data is not None:
        data = json.loads(json_data)

        print(f"\nImię: {data['imie']}")
        print(f"Imię drugie: {data['imie2']}")
        print(f"Nazwisko: {data['nazwisko']}")
        print(f"Data urodzenia: {data['data_urodzenia']}")
        print(f"Płeć: {data['plec']}")
        print(f"Adres: {data['adres']}")
        print(f"Telefon: {data['telefon']}")
        print(f"Pesel: {data['pesel']}")

        print("\nWizyty:")
        if data["wizyty"]:
            for visit in data["wizyty"]:
                print(f"- Data: {visit.get('data')}, Lekarz: {visit.get('lekarz')}, Opis: {visit.get('opis')}")
                if visit.get("zalecenia"):
                    print(f"  Zalecenia: {visit.get('zalecenia')}")
                else:
                    print("  Brak zaleceń")
        else:
            print("Brak wizyt")

        print("\nRecepty:")
        if data["recepty"]:
            for prescription in data["recepty"]:
                print(f"- Data: {prescription.get('data')}, Lekarz: {prescription.get('lekarz_id')}, Leki: {prescription.get('leki')}")
        else:
            print("Brak recept")

        print("\nSkierowania:")
        if data["skierowania"]:
            for s in data["skierowania"]:
                print(f"- Data: {s.get('data')}, Badanie: {s.get('badanie')}")
        else:
            print("Brak skierowań")
    else:
        print("\nBrak informacji o pacjencie.")
