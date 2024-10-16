#include <iostream>
#include <cstring>

using namespace std;

class Person {
public:
    Person(unsigned int _pesel, const char* _name, const char* _surename): pesel(_pesel),name(strdup(_name)), surename(strdup(_surename)) {};
    ~Person() { 
        free (name);
        free(surename); 
    }; 
    Person(const Person& other)
    {
        pesel=other.pesel;
        name=strdup(other.name);
        surename=strdup(other.surename);
    }
        
    Person& operator=(const Person& other) {
        pesel = other.pesel;
        if(strlen(other.name)>strlen(name)){
            free (name);
            name=strdup(other.name);
        }else{
            strcpy(name,other.name);
        }
        if(strlen(other.surename)>strlen(surename)){
            free (surename);
            surename=strdup(other.surename);
        }else{
            strcpy(surename,other.surename);
        }
        
        return *this;
    }

    void display() const {
        cout << "PESEL: " << pesel << ", Name: " << name << ", Surname: " << surename << endl;
    }
private:
    unsigned int pesel;
    char *name;
    char *surename;
};

int main() {
    Person p(1234567890, "Robert", "Kowalski");
    p.display();
    Person p2(p); /* Konstruktor kopiujący */
    p2.display();

    Person p3(1234567890, "Adamaaaaaa", "Lewandowski");
    p = p3; /* Operator przypisania */
    p.display();

    return 0;
}