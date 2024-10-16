
/*Podstawy dziedziczenia
-bazowe
-pochodne
Nowe klasy dziedziczą metody i dane klasy bazowej

class Bazowa {...};

class Pochodna : Bazowa {...}; //dziedziczenie klasy Bazowa
*/
/*
#include <iostream>
using namespace std;

class Bazowa{
    public:
        Bazowa(){
            cout<<"Konstruktor bazowy\n";
        };
        ~Bazowa(){
            cout<<"Desktruktor bazowy\n";
        };

};

class Pochodna : Bazowa{
    public:
        Pochodna(){
            cout<<"Konstruktor pochodny\n";
        };
        ~Pochodna(){
        cout<<"destruktor pochodny\n"; 
        };

};

class Pochodna2 : Pochodna{
    public:
        Pochodna2(){
            cout<<"Konstruktor pochodny2\n";
        };
        ~Pochodna2(){
            cout<<"destruktor pochodny2\n"; 
        };

};

int main()
{
    Pochodna2 p2;
    return 0;
}*/


#include <iostream>
#include <string>

class Person {
public:
    Person(unsigned int _pesel,
           const std::string &_name,
           const std::string &_surname)
        : pesel(_pesel), name(_name), surname(_surname) {};
protected:
    unsigned int pesel;
    std::string name;
    std::string surname;
};

class Employee : public Person {
public:
    Employee(unsigned int _pesel,
             const std::string &_name,
             const std::string &_surname,
             unsigned int _id,
             unsigned int _salary)
        : Person(_pesel, _name, _surname),
          id(_id),
          salary(_salary) {};

    Employee(const Person &_p,
             unsigned int _id,
             unsigned int _salary)
        : Person(_p),
          id(_id),
          salary(_salary) {};
protected:
    unsigned int id;
    unsigned int salary;
};

class Programmer : public Employee {
    public:
        Programmer(const Employee &_e): Employee(_e){};
        void program();
        void debug();
        void writeDocumentaction();
};
class Tester : public Employee {};
class Manager : public Employee {};

int main()
{
    Person p(122, "Jan", "Nowal");
    Employee e(123457890, "Adam", "Kowalski", 123, 6666);
    Employee e2(p, 123, 6666);
    return 0;
}


