#include <iostream>
#include <cstring>

class Product {
public:
    Product(const char   *_name,
            unsigned int  _price)
    {
        count++; // alternatywnie: Product::count++;

        this->name = new char[strlen(_name)+1];
        this->price = _price;
        sprintf(this->name, "%s", _name);
        this->id = count;

        std::cout << "Konstruktor: Allokujemy pamięć dla obiektu "
                  << this->name << " (" << this->id << ")\n";
    }

    ~Product()
    {
        std::cout << "Destruktor: Zwalniamy pamięć obiektu "
                  << this->name << " (" << this->id << ")\n";
        delete [] name;
    }
    void set_c(double c){
        this->c=c;
    }
    void display()const{
        std::cout<<price<<name<<c<<std::endl;
    }
private:
    char *name;
    unsigned int price;
    static size_t count;
    size_t id;
    double c;
};

size_t Product::count = 0;

int main()
{
    Product laptop1("DellMain", 1234);
    laptop1.set_c(3.5);
    laptop1.display();
    return 0;
}

