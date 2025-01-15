# Klasy i obiekty, konstruktory i destruktory
**Tworzenie klasy,  kosntruktora,  konstruktora kopiującego,  desktruktora**
```
class A{
    public:
    A(int _wiek,int _rozmiar, string _nazwa): wiek(_wiek),rozmiar(new int(_rozmiar)),nazwa(_nazwa){}; //konstruktor
    
    A(const A& other) { // konstruktor kopiujący
    wiek = other.wiek; 
    rozmiar = new int(*other.rozmiar); 
    nazwa = other.nazwa; 
    }

    ~A(){delete rozmiar;} // destruktor
    int get_wiek(){return wiek;} //metoda
    private:
    int wiek;
    int *rozmiar;
    string nazwa;
};
```
**Tworzenie obiektów**
```
int main()
{
    A a(1,2,"a");           // tworzenie obiektu a
    A b(a);                 // tworzenie obiektu b, z konstruktorem kopiującym klasy A
    A *c=new A(3,4,"c");    // tworzenie dynamiczne obiektu c
    delete c;
    B pochodna;
    A *bazowa=&pochodna;    // polimorfizm dynamiczny
    return 0;
}
```
# Metody i zmienne (również statyczne)
## Metody to funkcje w klasie.
```
class A {
public:
int get_age(){
    return age;
}
private:
int age;
};
```
## Metody statyczne - należą do klasy a nie do obiektu klasy
```
class Counter {
private:
    static int count;  // Statyczna zmienna członkowska
public:
    Counter() {
        count++;
    }
    ~Counter() {
        count--;
    }
    // Statyczna metoda, która zwraca bieżący stan zmiennej count
    static int getCount() {
        return count;
    }
};
// Inicjalizacja statycznej zmiennej członkowskiej poza klasą
int Counter::count = 0;
```
## Zmienne
```
class A {
public:
int size;
string name;
private:
int age;
string description;
};
```
## Statyczne zmienne (dostępne dla wszystkich instancji klasy)
```
class A {
public:
void doSomething() { ... lastUpdate = getTimestamp(); }.
private:
static int lastUpdate;
};
int A::lastUpdate = 0;
```
# Dostęp `public`, `protected`, `private`
`Public`: dostęp w klasie, klasach pochodnych, poza klasami
`Protected`: dostęp klasie i klasach pochodnych
`Private`: dostęp tylko w obrębie klasy
```
class A{
    private:
        int a;
    protected:
        int b;
    public:
        int c;
};
```
# Przeciążanie operatorów
## Przeciążenie operatora `<<`
```
std::ostream& operator<<(std::ostream &os, const IntArray &obj)
{
    os << obj.get(i);
    return os;
}

```
## Przeciążenei operatora `<<` (friend)
```
Class A{
private:
int i;
public:
    friend std::ostream& operator<<(std::ostream &os, const IntArray &obj);
};

std::ostream& operator<<(std::ostream &os, const IntArray &obj)
{
    os << obj.i;
    return os;
}
```
## Przeciążenie oparatora `=`
```
Nazwa_klasy operator=(Nazwa_klasy& source){
    i=source.i;
    size=source.size;
    return *this;
}
```
## Przeciążenie oparatora `++`
```
Nazwa_klasy operator++(){
    age++;
    return *this;
}
```
## Przeciążenie oparatora `+`
```
Nazwa_klasy operator+(Nazwa_klasy& source){
    return Nazwa_klasy(size+source.size,age+source.age);
}
```
# Funkcje zaprzyjaźnione
```
class A {
public:
int get_age(){
    return age;
}
friend void set_size(A& a,int s);
private:
int age;
int size;
};
void set_size(A& a,int s){
    a.size=s;
};
```
# Kompozycja
```
#include <iostream>
using namespace std;

class Kolo {
public:
    void opisz() {
        cout << "To jest kolo." << endl;
    }
};

class Samochod {
private:
    Kolo kolo1;
    Kolo kolo2;
    Kolo kolo3;
    Kolo kolo4;

public:
    void opisz() {
        cout << "Samochod ma cztery kola:" << endl;
        kolo1.opisz();
        kolo2.opisz();
        kolo3.opisz();
        kolo4.opisz();
    }
};

int main() {
    Samochod samochod;
    samochod.opisz(); // Wywołanie metody opisującej samochód
    return 0;algorytmy np. sortowanie babelkowe

}

```
# Dziedziczenie
## Dziedzienie dzieli się na: `public`,`protected`,`private`
### Dziedziczenie `public`:
Wszystkie zmienne publiczne klasy bazowej stają się publiczne w klasie pochodnej.

Wszystkie zmienne protected klasy bazowej stają się protected w klasie pochodnej.

Wszystkie zmienne prywatne  klasy bazowej nie dziedziczą się do klasy pochodnej.
```
class Bazowa{};
class Pochodna: public Bazowa{};
```
### Dziedziczenie `protected`:
Wszystkie zmienne publiczne klasy bazowej stają się protected w klasie pochodnej.

Wszystkie zmienne protected klasy bazowej stają się protected w klasie pochodnej.

Wszystkie zmienne prywatne  klasy bazowej nie dziedziczą się do klasy pochodnej.

```
class Bazowa{};
class Pochodna: protected Bazowa{};
```
### Dziedziczenie `private`:
Wszystkie zmienne publiczne klasy bazowej stają się prywatne w klasie pochodnej.

Wszystkie zmienne publiczne klasy bazowej stają się protected w klasie pochodnej.

Wszystkie zmienne prywatne  klasy bazowej nie dziedziczą się do klasy pochodnej.

```
class Bazowa{};
class Pochodna: private Bazowa{};

class Bazowa1{};
class Pochodna1: Bazowa{};
```
# Klasy abstrakcyjne
Klasa abstrakcyjna to klasa, która ma co najmniej jedną funckję w pełni wirtualną
```
class A{
    A(int _a):a(_a){};
    virtual ~A(){};
    virtual void display()=0;
    int a;
    
};
class B: public A{ 
    B(int _a,int _c):A(_a), c(new int(_c)){};
    int *c;
    virtual void display()override{
        cout<<a<<c<<endl;
    }
    ~B(){
        delete c;
    }
};
```
# Constness
Pokazanie, że dana funckja nie zmienia stanu obiektu
```
void print() const; // OK
int getValue() const; // OK
void setValue(int); // tutaj już coś modyfikujemy
```

szablonj
wyjatki rzucic wychwycic
algorytmy np. sortowanie babelkowe
