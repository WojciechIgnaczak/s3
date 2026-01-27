from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# klasa dziedzicząca po BaseModel - przepis na wygląd danych
class NowyProdukt(BaseModel):
    nazwa:str
    cena:float
    opis: Optional[str] = None
    dostepny: bool=True


app= FastAPI(
    title="Sklep API",
    description="To jest APIdo zarządzania magazynem. Pozwala dodawać i szukać produktów.",
    version="1.5.0"
)

@app.get("/")
def strona_glowna():

    return {"powitanie":"Cześć! To moje pierwsze API"}


# {id} w ścieżce oznaczan zmienna
# Argument funkcji id:int   mówi FastAPI , że musi być liczba
@app.get("/produkty/{id}")
def pobierz_produkt(id:int):
    return {
            "produkt_id":id,
            "nazwa": "Jakiś produkt"
            }

# Endpoint POST do dodawania danych
@app.post("/produkty",
          tags=["Produkty"],#grupowanie endpointów w sekcje
          summary="Dodaj nowy towar",#krótki tytuł w labelce
          description="Ten endpoint przyjmuje JSON z produktem i zapisuje go w bazie",#długi opis
          status_code=201 # zwraca kod 201 (Created)
          )

def dodaj_produkt(produkt:NowyProdukt):
    # PARAMETR 'PRODUKT MA TYP NOWYPRODUKT'
    # FASTAPI AUTOMATYCZNIE TWORZY:
    #odczyta json z body zapytania
    #sprawdzi czy pola się zgadzają
    #utowrzy produkt z którego mozesz skorzystać
    calkowita_cena=produkt.cena*1.23
    return{
        "status":"Ok",
        "cena_brutto":calkowita_cena,
        "cena_netto":produkt.cena,
        "dane":produkt    }



@app.get("/szukaj/")
def szukaj(q:str, limit:int=10):
    # q-jest wymagane bo nie ma wartosci domyślnej
    # limit opcjonalne
    return {
        "wynik":f"Szukaj frazy {q}. Pokażę maksymalnie {limit} wyników"
    }

if __name__ == "__main__":
    pass