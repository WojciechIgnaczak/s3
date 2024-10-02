#include <iostream>
#include <cstring>
using namespace std;

class Product
{
public:
    // Konstruktor
    Product(const char *_name, unsigned int price){
        count++;
        this->name = new char[strlen(_name) + 1]; // alokacja z miejscem na \0
        strcpy(this->name, _name); // kopiowanie nazwy
        cout << "konstruktor " << count << " " << this->name << "\n";
        //this->price = price;
    }
    
    // Destruktor
    ~Product(){
        cout << "destruktor " << count << " " << this->name << "\n";
        delete[] name; // zwolnienie pamięci
        count--;
    }

    const char* getName(){
        return this->name;
    }
    
private:
    char *name;
    unsigned int price;
    static size_t count;
    
};

size_t Product::count = 0;
Product *laptop0 = new Product("Dell statyczny", 1222);

int main()
{
    Product laptop1("Dellmain", 1222);
    {
        Product laptop2("Dellinternal1", 1222);
        Product laptop3("Dellinternal2", 1222);
    } // laptop2 i laptop3 zostaną zniszczone tutaj (wywołanie destruktorów)
    
    Product *laptop4 = Product("DellDynamiczny", 1222);
    //delete laptop4;
    return 0;
}
