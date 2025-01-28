# Templates Generyczność
1. Definicja szablonu funkcji (Function Template)

Szablon funkcji umożliwia pisanie funkcji, które mogą działać na różnych typach danych.

Składnia:
```cpp
template <typename T>
T funkcja(T a, T b) {
    return a + b;
}

int wynik = funkcja<int>(5, 10); // Wynik: 15
double wynik2 = funkcja<double>(5.5, 10.1); // Wynik: 15.6
```
2. Definicja szablonu klasy (Class Template)

Szablon klasy umożliwia tworzenie klas dla różnych typów danych.

Składnia:
```cpp
template <typename T>
class Klasa {
private:
    T dane;
public:
    Klasa(T dane): dane(dane) {}
    T getDane() { return dane; }
};

Klasa<int> klasaInt(10);
Klasa<double> klasaDouble(3.14);

std::cout << klasaInt.getDane(); // 10
std::cout << klasaDouble.getDane(); // 3.14

```

3. Szablon z wieloma typami

Składnia:
```cpp
template <typename T, typename U>
class Para {
public:
    T pierwszy;
    U drugi;

    Para(T p, U d): pierwszy(p), drugi(d) {}
};
Para<int, double> para(1, 3.14);
std::cout << para.pierwszy << ", " << para.drugi; // 1, 3.14

```

4. Szablony z domyślnymi typami

Składnia:
```cpp
template <typename T = int>
class Klasa {
public:
    T dane;
    Klasa(T dane): dane(dane) {}
};

Klasa<> domyslny(10); // T to int
Klasa<double> inny(3.14);

```

# STL

## Pair: Przechowuje parę danych.
```cpp
#include <utility>
// Tworzenie pary
std::pair<T1, T2> para; // T1 typ pierwszej wartości(first), T2 typ drugiej wartości(second)
std::pair<int, std::string> para(42, "Hello");
std::pair<int, double> para(1, 3.14);
// Tworzenie pary makepair
auto para = std::make_pair(10, "World");
std::cout << para.first << ", " << para.second;  // 10, World

// Wyswietlenie
std::cout << "Pierwsza wartość: " << para.first << "\n";   // 1
std::cout << "Druga wartość: " << para.second << "\n";    // 3.14

// Zamiana wartości
#include <iostream>
#include <utility>

int main() {
    std::pair<int, std::string> para(1, "Ala");

    // Zamiana wartości w obrębie jednej pary
    para.first = 2;
    para.second = "Ola";

    std::cout << para.first << " - " <<

```


## Tuple: Przechowuje różne typy danych.ple
```cpp
#include <tuple>
std::tuple<int, double, std::string> t(1, 3.14, "hello"); //tworzenie
std::get<0>(t) = 2;  // Zmiana wartości na indeksie 0
std::get<1>(t) = 2.71; // Zmiana wartości na indeksie 1

//Dodawanie:  Nie można dodać elementu bezpośrednio. std::tuple ma stały rozmiar.

//Usuwanie:   Nie można usunąć elementu bezpośrednio. std::tuple ma stały rozmiar.

// Rozmiar
std::tuple<int, double> t;
std::cout << std::tuple_size<decltype(t)>::value; // 2

// Odwoływanie
std::tuple<int, double, std::string> t(1, 3.14, "hello");
std::cout << std::get<0>(t) << std::endl; // Odwołanie do pierwszego elementu (int)
std::cout << std::get<1>(t) << std::endl; // Odwołanie do drugiego elementu (double)
```
## Vector: Dynamiczna tablica
```cpp
// Include the vector library
#include <vector>
// Create a vector called cars that will store strings
vector<string> cars;
vector<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Print vector elements
for (string car : cars) {
  cout << car << "\n";
}
// Get the n element
cout << cars[n];  // Outputs Volvostd::cerr << e.what() << '\n';
// Get the first element
cout << cars.front();

// Get the last element
cout << cars.back();

// Change the value of the first element
cars[0] = "Opel";

//Add Vector Elements
cars.push_back("Tesla");

//Remove Vector Elements
cars.pop_back();

//Vector size
cout << cars.size();  // Outputs 4

cout << cars.empty();  // Outputs 1 (The vector is empty)
```
## Array: Stała tablica o określonym rozmiarze
```cpp
#include <array>
// Tworzenie
std::array<int, 5> arr = {1, 2, 3, 4, 5};

//Zmiana
arr[0] = 10; // Zmiana elementu na indeksie 0
arr.at(1) = 20; // Zmiana elementu na indeksie 1

// Dodawanie i usuwanie: NIE MOŻNA

// Rozmiar
std::cout << arr.size();  // 5

// Odwoływanie
std::array<int, 5> arr = {1, 2, 3, 4, 5};
std::cout << arr[0] << std::endl; // Odwołanie do pierwszego elementu (index 0)
std::cout << arr.at(1) << std::endl; // Odwołanie do drugiego elementu (index 1)

```
## List: Lista powiązana.
```cpp
 // Include the list library
#include <list>

// Create a list called cars that will store strings
list<string> cars;

// Create a list called cars that will store strings
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Print list elements
for (string car : cars) {
  cout << car << "\n";
}

// Get the first element
cout << cars.front();  // Outputs Volvo

// Get the last element
cout << cars.back();  // Outputs Mazda

// Change the value of the first element
cars.front() = "Opel";

// Change the value of the last element
cars.back() = "Toyota";

// Add an element at the beginning
cars.push_front("Tesla");

// Add an element at the end
cars.push_back("VW");

// Remove the first element
cars.pop_front();

// Remove the last element
cars.pop_back();

// List size
cout << cars.size();  // Outputs 4

// Is empty
list<string> cars;
cout << cars.empty();  // Outputs 1 (The list is empty)


```
## Forward List
```cpp
#include<forward_list>
// Tworzenie
std::forward_list<int> fl = {1, 2, 3};

// Zmiana
*fl.begin() = 10; // Zmiana pierwszego elementu

// dodawanie
fl.push_front(0);  // Dodanie na początek
fl.insert_after(fl.begin(), 5); // Dodanie za pierwszym elementem

//usuwanie
fl.pop_front(); // Usunięcie pierwszego elementu
fl.erase_after(fl.begin()); // Usunięcie elementu po pierwszym

// Rozmiar
std::cout << std::distance(fl.begin(), fl.end()); // Rozmiar listy

// Odwoływanie
std::forward_list<int> fl = {1, 2, 3};
auto it = fl.begin();
std::cout << *it << std::endl; // Odwołanie do pierwszego elementu

```
## Queue: Kolejka (FIFO).
```cpp
#include<queue>
// Tworzenie
std::queue<int> q;

//Zmiana NIE DA SIĘ

// dodawanie
q.push(10);  // Dodanie elementu na koniec

//usuwanie
q.pop(); // Usunięcie elementu z początku

//rozmiar
std::cout << q.size(); // Rozmiar kolejki

// Odwoływanie
std::queue<int> q;
q.push(10);
q.push(20);
std::cout << q.front() << std::endl; // Odwołanie do pierwszego elementu
std::cout << q.back() << std::endl;  // Odwołanie do ostatniego elementu

```
## Stack: Stos (LIFO).
```cpp
// Include the stack library
#include <stack>

// Create a stack of strings called cars
stack<string> cars;

stack<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Add elements to the stack
cars.push("Volvo");

// Access the top element
cout << cars.top(); 

//Change the Top Element
cars.top() = "Tesla";

// Remove the last added element (Mazda)
cars.pop();

// Size stack
 cout << cars.size();

// Is empty
cout << cars.empty(); 


```
## Priority queue: Kolejka z priorytetem
```cpp
#include <queue>
// Tworzenie
std::priority_queue<int> pq;

//Zmiana NIE MOŻNA

// dodawanie
pq.push(10);  // Dodanie elementu (wstawiany w odpowiedniej kolejności)

//usuwanie
pq.pop(); // Usunięcie elementu o najwyższym priorytecie

//rozmiar
std::cout << pq.size(); // Rozmiar kolejki

// Odwoływanie
std::priority_queue<int> pq;
pq.push(10);
pq.push(20);
std::cout << pq.top() << std::endl; // Odwołanie do elementu o najwyższym priorytecie

```
## Set: Zbiór unikalnych elementów
```cpp
#include<set>
// Tworzenie
std::set<int> s = {1, 2, 3, 4};

//Zmiana NIE DA SIE

// dodawanie
s.insert(5);  // Dodanie elementu

//usuwanie
s.erase(3); // Usunięcie elementu

//rozmiar
std::cout << s.size();  // Rozmiar zbioru

// Odwoływanie
std::set<int> s = {1, 2, 3, 4};
for (auto it = s.begin(); it != s.end(); ++it) {
    std::cout << *it << std::endl; // Odwołanie do każdego elementu w zbiorze
}

```
## Multiset: Zbiór, który pozwala na duplikaty
```cpp
#include<set>

// Tworzenie
std::multiset<int> ms = {1, 2, 2, 3, 3, 3};

//Zmiana NIE DA SIE

// dodawanie
ms.insert(2);  // Dodanie elementu (można dodać duplikaty)

//usuwanie
ms.erase(2); // Usunięcie wszystkich wystąpień 2

//rozmiar
std::cout << ms.size();  // Rozmiar multizbioru

// Odwoływanie
std::multiset<int> ms = {1, 2, 2, 3, 3, 3};
for (auto it = ms.begin(); it != ms.end(); ++it) {
    std::cout << *it << std::endl; // Odwołanie do każdego elementu w multizbiorze
}

```
## Unordered set: Zbiór bez zachowania kolejności
```cpp
#include<unordered_set>

// Tworzenie
std::unordered_set<int> us = {1, 2, 3, 4};

//Zmiana NIE DA SIE

// dodawanie
us.insert(5);  // Dodanie elementu

//usuwanie
us.erase(3); // Usunięcie elementu

//rozmiar
std::cout << us.size();  // Rozmiar zbioru

// Odwoływanie
std::unordered_set<int> us = {1, 2, 3, 4};
for (auto it = us.begin(); it != us.end(); ++it) {
    std::cout << *it << std::endl; // Odwołanie do każdego elementu w zbiorze
}

```
## Map: Mapa klucz-wartość
```cpp
#include<map>

// Tworzenie
std::map<int, std::string> m = {{1, "Ala"}, {2, "Ola"}};

//Zmiana
m[1] = "Kasia";  // Zmiana wartości dla klucza 1

// dodawanie
m.insert({3, "Ela"});  // Dodanie pary klucz-wartość

//usuwanie
m.erase(2);  // Usunięcie elementu o kluczu 2

//rozmiar
std::cout << m.size();  // Rozmiar mapy

// Odwoływanie
std::map<int, std::string> m = {{1, "Ala"}, {2, "Ola"}};
std::cout << m[1] << std::endl;  // Odwołanie do wartości dla klucza 1
stack<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Add elements to the stack
cars.push("Volvo");

// Access the top element
cout << cars.top(); 

//Change the Top Element
cars.top() = "Tesla";

// Remove the last added element (Mazda)
std::unordered_map<int, std::string> um = {{1, "Ala"}, {2, "Ola"}};

//Zmiana
um[1] = "Kasia";  // Zmiana wartości dla klucza 1

// dodawanie
um.insert({3, "Ela"});  // Dodanie pary klucz-wartość

//usuwanie
um.erase(2);  // Usunięcie elementu o kluczu 2

//rozmiar
std::cout << um.size();  // Rozmiar mapy

// Odwoływanie
std::unordered_map<int, std::string> um = {{1, "Ala"}, {2, "Ola"}};
std::cout << um[1] << std::endl;  // Odwołanie do wartości dla klucza 1
std::cout << um.at(2) << std::endl; // Odwołanie do wartości dla klucza 2

```

# Wyjątki
```cpp
#include <stdexcept>
#include <iostream>

double mydiv(int a, int b) {
    if (b == 0) {
        throw std::invalid_argument("BOOM!");
    }
    return a / static_cast<double>(b);
}

int main() {
    try {
         mydiv(5,0);
    } catch(const std::exception& e) {
        std::cerr << e.what() << '\n';
        std::cout << "Złapano wyjątek: " << e.what() << std::endl;
    } catch(const std::exception& e) {
        std::cerr << e.what() << '\n';
        std::cout << "Złapano wyjątek: " << e.what() << std::endl;
    }



    std::cout << "Kontynuacja programu\n";
    return 0;
}
```
Rodzaje wyjątków:
- std::exception  – Bazowa klasa dla wszystkich wyjątków.
- std::runtime_error – Błędy wykonania programu
- std::logic_error – Błędy logiczne, np. złe użycie programu
- std::bad_alloc – Błąd przydzielania pamięci
- std::out_of_range – Błąd indeksu poza zakresem
- std::invalid_argument – Nieprawidłowy argument

# Iterator