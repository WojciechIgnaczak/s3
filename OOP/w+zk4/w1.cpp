#include<iostream>
using namespace std;

class Bazowa {
public:
    virtual void wirtualna(){
        cout<<"metoda wirtualna w klasie bazowej (A)\n";
        }

    void normalna(){
        cout<<"metoda normalna w klasie bazowej (A)\n";
    }
};

class Pochodna : public Bazowa {
public:
    void wirtualna(){
        cout<<"metoda wirtualna w klasie pochodnej (B)\n";
        }
    void normalna(){
        cout<<"metoda normalna w klasie pochodnej (B)\n";
        }
};

int main()
{
Pochodna p;
Bazowa &ref = p;
p.wirtualna();//wirtualna w pochodnej
p.normalna();// normalna w pochodnej
ref.wirtualna();//wirtualna w pochodnej
ref.normalna();//normalna w bazowej
return 0;
}