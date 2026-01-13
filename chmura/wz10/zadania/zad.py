# Część 1: Rozgrzewka (Setup)

#     Inicjalizacja: Stwórz plik dziekanat.py. Zainicjalizuj aplikację FastAPI z tytułem "E-Dziekanat API" i wersją "2.0".
#     Strona startowa: Stwórz endpoint GET / zwracający JSON: {"uczelnia": "Politechnika Wrocławska", "autor": "Twoje Imię"}.
#     Uruchomienie: Uruchom serwer i sprawdź w przeglądarce, czy pod adresem /docs wyświetla się Swagger UI.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field
from typing import Optional, List
from enum import Enum
app= FastAPI(
    title="E-Dziekanat API",
    version="2.0"
)

@app.get("/",deprecated=True)
def strona_glowna():

    return {"uczelnia":"Politechnika Wrocławska", "autor": "Twoje Imię"}

# Część 2: Modele Danych (Pydantic)

#     Model Studenta: Zdefiniuj klasę Student(BaseModel) zawierającą pola:
#         indeks (int)
#         imie (str)
#         nazwisko (str)
#         kierunek (str)
#         rok_studiow (int)
#     Walidacja: Dodaj walidację do pola rok_studiow – student może być tylko na roku od 1 do 5 (użyj Field(..., ge=1, le=5) z modułu pydantic).
class WartoscOceny(float,Enum):
    NIEDOSTATECZNY = 2.0
    DOSTATECZNY = 3.0
    DOSTATECZNY_PLUS = 3.5
    DOBRY = 4.0
    DOBRY_PLUS = 4.5
    BARDZO_DOBRY = 5.0

class Ocena(BaseModel):
    przedmiot:int
    wartosc:WartoscOceny

class Student(BaseModel):
    indeks:int=Field(...,example=1)
    imie:str=Field(...,example="Wojciech")
    nazwisko:str=Field(...,example="ignaczak")
    kierunek:str=Field(...,example="informatyka")
    rok_studiow:int=Field(..., ge=1, le=5,example=3)
    oceny:List[Ocena]=[]

    model_config = {
        "json_schema_extra": {
            "example": {
                "indeks": 11111,
                "imie": "Jan",
                "nazwisko": "Kowalski",
                "kierunek": "Informatyka",
                "rok_studiow": 3,
                "oceny": []
            }
        }
    }

# Część 3: Operacje na Studentach (CRUD)

#     Dodawanie (CREATE): Stwórz endpoint POST /studenci, który przyjmuje obiekt Student i dodaje go do listy. Zwróć komunikat sukcesu.
#     Wyświetlanie (READ): Stwórz endpoint GET /studenci, który zwraca listę wszystkich studentów.
#     Szczegóły (READ One): Stwórz endpoint GET /studenci/{indeks}, który zwraca dane studenta o konkretnym numerze indeksu.
#     Wyszukiwanie: Zmodyfikuj endpoint GET /studenci tak, aby przyjmował opcjonalny parametr ?kierunek=.... Jeśli podano kierunek, zwróć tylko studentów z tego kierunku.
#     Usuwanie (DELETE): Stwórz endpoint DELETE /studenci/{indeks}, który usuwa studenta z listy.

students: List[Student] = []
@app.post("/studenci",status_code=201,tags=["Studenci"],summary="dodawanie studenta",description="dodawanie studenta do listy wszystkich studentów")
def dodaj_studenta(student:Student):
    indeksy=[]
    for i in students:
        indeksy.append(i.indeks)
    if student.indeks not in indeksy:
        students.append(student)
        return {"message": "Student dodany", "student": student}
    raise HTTPException(status_code=400, detail="Student o tym indeksie już istnieje")

@app.get("/studenci",tags=["Studenci"],summary="wyświetlanie studentów",description="wyświetlanie wszystkich studentów z listy")
def wyswietl__wszystkich_studentow(kierunek:Optional[str]=None):
    if kierunek==None:
        return students
    else:
        return[s for s in students if s.kierunek.lower() == kierunek.lower()]

@app.get("/studenci/{indeks}",tags=["Studenci"],summary="wyświetlanie studenta",description="wyświetlanie pojedynczego studenta na podstawie jego indeksu")
def wyswietl_studenta(indeks:int):
    for i in students:
        if i.indeks==indeks:
            return i
    
    raise HTTPException(status_code=404, detail=f"Nie znaleziono studenta o indeksie {indeks}")
        
@app.delete("/studenci/{indeks}",tags=["Studenci"],summary="usuwanie studenta",description="usuwanie pojedynczego studenta z listy na podstawie indeksu")
def usun_studenta(indeks:int):
    for i in students:
        if i.indeks==indeks:
            students.remove(i)
            return f"Student o indeksie {indeks} usunięty"
    raise HTTPException(status_code=404, detail=f"Nie znaleziono studenta o indeksie {indeks}")

        

# Część 4: Oceny (Relacje i Logika)

#     Model Oceny: Zdefiniuj klasę Ocena(BaseModel) z polami: przedmiot (str), wartosc (float).
#     Dodawanie oceny: Stwórz endpoint POST /studenci/{indeks}/oceny, który pozwala dodać ocenę przypisaną do konkretnego studenta (musisz przechowywać oceny wewnątrz obiektu studenta lub w osobnej liście powiązanej indeksem).
#     Walidacja oceny: Upewnij się, że wartosc oceny to jedna z dopuszczalnych liczb: 2.0, 3.0, 3.5, 4.0, 4.5, 5.0 (skorzystaj z Enum lub walidacji Pydantic).
#     Pobieranie ocen: Stwórz endpoint GET /studenci/{indeks}/oceny, który zwraca listę ocen danego studenta.


@app.post("/studenci/{indeks}/oceny",tags=["Oceny"],status_code=201,summary="dodawanie oceny",description="dodawanie oceny do studenta")
def dodaj_ocene(indeks:int, ocena:Ocena):
    for i in students:
        if i.indeks==indeks:
            i.oceny.append(ocena)
            return f"Ocena {ocena.wartosc} z przedmiotu {ocena.przedmiot} została dodana do studenta o indeksie {indeks}"
    raise HTTPException(status_code=404, detail=f"Nie znaleziono studenta o indeksie {indeks}")

        
@app.get("/studenci/{indeks}/oceny",tags=["Oceny"],summary="wyświetlanie ocen studenta",description="wyświetlanie ocen studenta po indeksie")
def wyswietl_oceny(indeks:int):
    for i in students:
        if i.indeks==indeks:
            return i.oceny
    raise HTTPException(status_code=404, detail=f"Nie znaleziono studenta o indeksie {indeks}")


    #Część 5: Profesjonalizacja (Swagger UI)

    # Tagowanie: Uporządkuj endpointy. Dodaj tags=["Studenci"] do operacji na studentach i tags=["Oceny"] do operacji na ocenach.
    # Status Codes: Skonfiguruj endpoint POST, aby w przypadku sukcesu zwracał kod HTTP 201 Created (zamiast domyślnego 200).
    # Obsługa błędów: Jeśli użytkownik zapyta o studenta, którego nie ma (np. w GET /studenci/{indeks}), zwróć wyjątek HTTPException z kodem 404 Not Found.
    # Opisy: Dodaj parametr summary do każdego endpointu (krótki opis widoczny na belce w Swaggerze) oraz description (dłuższy opis markdown).
    # Przykłady: W modelu Student dodaj klasę Config z przykładowym obiektem (schema_extra), aby w Swaggerze przycisk "Try it out" podpowiadał sensowne dane (np. Jan Kowalski).
    # Deprecated: Oznacz stary endpoint GET / jako deprecated=True, symulując wygaszanie starej wersji API.

