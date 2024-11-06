#include <iostream>

using namespace std;

class Car {
public:
Car(const string &_man, const string& mod,const string &_vin):manufacture(_man),model(mod),vin(_vin){}
void drive(){cout<<"Drive "<<vin<<"\n";}
void setVin(const string &_vin){this->vin=_vin;}
protected:
Car(){};
private:
    string manufacture;
    string model;
    string vin;
};

class PetrolCar : virtual public Car {
public:
PetrolCar(const string &_man, const string& mod,const string &_vin):Car(_man,mod,_vin){}
int getFuelCapacity();
protected:
PetrolCar(){};
};

class ElectricCar : virtual public Car {
public:
ElectricCar(const string &_man, const string& mod,const string &_vin):Car(_man,mod,_vin){}
int getBatteryCapacity();
protected:
ElectricCar(){};
};

class HybridCar : public PetrolCar, public ElectricCar {
    public:
    HybridCar(const string &_man, const string& mod,const string &_vin):Car(_man,mod,_vin){}
};
int main()
{
    HybridCar c("ford","fiesta","aaaa");
    /*PetrolCar p;
    ElectricCar e;*/
    c.drive(); // O
    c.setVin("ccc");
    /*e.setVin("eee");
    p.setVin("ppp");*/
    c.drive();
    /*e.drive();
    p.drive();*/
    return 0;
}