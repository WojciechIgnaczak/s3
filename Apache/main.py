from pyignite import Client
from dane_z_pesel import day_of_birth, month_of_birth_number,sex, year_of_birth
from klasy import Pacjent, Wizyta, Recepta, Skierowanie
from zapis_odczyt import dodaj_pacjenta, odczytaj_pacjenta
import json

client = Client()
client.connect('127.0.0.1', 10800)
pacjent_cache = client.get_or_create_cache('pacjentCache')

############################################## Dodanie pacjenta
pesel = "04241004933"
imie = "Anna"
imie2 = "Maria"
nazwisko = "Nowak"
adres = "Jakas 1 Płock"
telefon = "600123456"

dodaj_pacjenta(pacjent_cache, pesel, imie, imie2, nazwisko, adres, telefon)


############################################## Dodanie wizyty
json_data = pacjent_cache.get(pesel)
pacjent_data = json.loads(json_data)

data_wizyty = "2025-05-17"
lekarz = "Dr Kowalski"
opis = "Badanie krwi"
zalecenia = "Powtórzyć za 2 tygodnie"
wizyta = Wizyta(data_wizyty, lekarz, opis, zalecenia)

pacjent = Pacjent(
    pesel=pacjent_data["pesel"],
    imie=pacjent_data["imie"],
    imie2=pacjent_data.get("imie2"),
    nazwisko=pacjent_data.get("nazwisko"),
    adres=pacjent_data.get("adres"),
    telefon=pacjent_data.get("telefon")
)

# Dodajemy zapisane już wizyty, recepty i skierowania, jeśli są
pacjent.wizyty = pacjent_data.get("wizyty", [])
pacjent.recepty = pacjent_data.get("recepty", [])
pacjent.skierowania = pacjent_data.get("skierowania", [])

pacjent.dodaj_wizyte(wizyta)

pacjent_cache.put(pesel, json.dumps(pacjent.to_dict(), ensure_ascii=False))


############################################## Dodanie recepty
json_data = pacjent_cache.get(pesel)
pacjent_data = json.loads(json_data)

data_recepty = "2025-05-17"
lekarz = "Dr Kowalski"
leki = ["Paracetamol", "Ibuprofen"]
recepta = Recepta(data_recepty,lekarz, leki)

pacjent = Pacjent(
    pesel=pacjent_data["pesel"],
    imie=pacjent_data["imie"],
    imie2=pacjent_data.get("imie2"),
    nazwisko=pacjent_data.get("nazwisko"),
    adres=pacjent_data.get("adres"),
    telefon=pacjent_data.get("telefon")
)

pacjent.wizyty = pacjent_data.get("wizyty", [])
pacjent.recepty = pacjent_data.get("recepty", [])
pacjent.skierowania = pacjent_data.get("skierowania", [])

pacjent.dodaj_recepte(wizyta)

pacjent_cache.put(pesel, json.dumps(pacjent.to_dict(), ensure_ascii=False))


############################################## Dodanie skierowania do pacjenta
pesel = "04241004933"
json_data = pacjent_cache.get(pesel)
pacjent_data = json.loads(json_data)

data_skierowania = "2025-05-17"
lekarz = "Dr Kowalski"
opis = "Badanie krwi"
skierowanie = Skierowanie(data_skierowania,lekarz, opis)


pacjent = Pacjent(
    pesel=pacjent_data["pesel"],
    imie=pacjent_data["imie"],
    imie2=pacjent_data.get("imie2"),
    nazwisko=pacjent_data.get("nazwisko"),
    adres=pacjent_data.get("adres"),
    telefon=pacjent_data.get("telefon")
)

# Dodajemy zapisane już wizyty, recepty i skierowania, jeśli są
pacjent.wizyty = pacjent_data.get("wizyty", [])
pacjent.recepty = pacjent_data.get("recepty", [])
pacjent.skierowania = pacjent_data.get("skierowania", [])

pacjent.dodaj_skierowanie(wizyta)
# Zapis do cache
pacjent_cache.put(pesel, json.dumps(pacjent.to_dict(), ensure_ascii=False))




############################################### Odczyt pacjenta i wypisanie
print("\nOdczyt pacjenta z cache:")
pesel = "04241004933"
odczytaj_pacjenta(pacjent_cache, pesel)

client.close()
