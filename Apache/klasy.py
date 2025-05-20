from dane_z_pesel import day_of_birth, month_of_birth_number,sex, year_of_birth

class Pacjent:
    def __init__(self, pesel, imie, imie2=None, nazwisko=None, adres=None, telefon=None):
        self.pesel = pesel
        self.imie = imie
        self.imie2 = imie2
        self.nazwisko = nazwisko
        self.data_urodzenia = f"{day_of_birth(pesel)}-{month_of_birth_number(pesel)}-{year_of_birth(pesel)}"
        self.plec = sex(pesel)
        self.adres = adres
        self.telefon = telefon
        self.wizyty = []
        self.recepty = []
        self.skierowania = []

    def dodaj_wizyte(self, wizyta):
        self.wizyty.append(wizyta.__dict__)  # dodajemy wizytę jako słownik a nie jako obiekt

    def dodaj_recepte(self, recepta):
        self.recepty.append(recepta.__dict__)

    def dodaj_skierowanie(self, skierowanie):
        self.skierowania.append(skierowanie.__dict__)

    def to_dict(self):
        return {
            "pesel": self.pesel,
            "imie": self.imie,
            "imie2": self.imie2,
            "nazwisko": self.nazwisko,
            "data_urodzenia": self.data_urodzenia,
            "plec": self.plec,
            "adres": self.adres,
            "telefon": self.telefon,
            "wizyty": self.wizyty,
            "recepty": self.recepty,
            "skierowania": self.skierowania,
        }

class Wizyta:
    def __init__(self, data, lekarz, opis=None, zalecenia=None):
        self.data = data
        self.lekarz = lekarz
        self.opis = opis
        self.zalecenia = zalecenia

class Recepta:
    def __init__(self, data, lekarz, leki=None):
        self.data = data
        self.lekarz = lekarz
        self.leki = leki if leki else []

class Skierowanie:
    def __init__(self, data, lekarz,badanie):
        self.data = data
        self.lekarz = lekarz
        self.badanie = badanie

def odbuduj_pacjenta(pacjent_data):
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
    return pacjent
