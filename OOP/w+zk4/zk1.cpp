#include<iostream>
using namespace std;

class Computer {
    private:
        string manufacturer;
        string model;
        string cpu;
        unsigned int ramMemory;
        unsigned int diskMemory;

    public:
        Computer(string _manufacturer, string _model, string _cpu, unsigned int _ramMemory, unsigned int _diskMemory): manufacturer(_manufacturer),model(_model),cpu(_cpu),ramMemory(_ramMemory),diskMemory(_diskMemory){};
       

        void print()const{
            cout<<manufacturer<<" / "<<model<<" / "<<cpu<<" / "<<ramMemory<<" GB RAM /"<<diskMemory<<" GB DISK"<<endl;
        }
        void setManufacturer(string _manufacturer){
            manufacturer=_manufacturer;
        }
        void setModel(string _model){
            model=_model;
        }
        void setCpu(string _cpu){
            cpu=_cpu;
        }
        void setRamMemory(unsigned int _ramMemory){
            ramMemory=_ramMemory;
        }
        void setDiskMemory(unsigned int _diskMemory){
            diskMemory=_diskMemory;
        }
};

class Laptop: public Computer {
    private:
        unsigned int screen;
        unsigned int battery;
    public:
        Laptop(string _manufacturer, string _model, string _cpu, unsigned int _ramMemory, unsigned int _diskMemory, unsigned int _screen, unsigned int _battery)
        : Computer(_manufacturer, _model, _cpu, _ramMemory, _diskMemory), screen(_screen), battery(_battery) {}
        
        Laptop(const Computer& comp, unsigned int _screen, unsigned int _battery)
        : Computer(comp), screen(_screen), battery(_battery) {}
        void print()const{
            Computer::print();
            cout<<screen<<" / "<<battery<<" WH"<<endl;
        }

        void setScreen(unsigned int _screen){
            screen=_screen;
        }
        
        void setBattery(unsigned int _battery){
            battery=_battery;
        }
};

class Desktop: public Computer{
    protected:
        string formFactor;
        string psu;
    public:
        Desktop(string _manufacturer, string _model, string _cpu, unsigned int _ramMemory, unsigned int _diskMemory, string _formFactor,string _psu)
        : Computer(_manufacturer, _model, _cpu, _ramMemory, _diskMemory), formFactor(_formFactor), psu(_psu) {}
        
        Desktop(const Computer& comp, string _formFactor,string _psu)
        : Computer(comp), formFactor(_formFactor), psu(_psu) {}
        void print()const{
            Computer::print();
            cout<<formFactor<<" / "<<psu<<endl;
        }

        void setFormFormator(string _formFormator){
            formFactor=_formFormator;
        }
        
        void setPsu(string _psu){
            psu=_psu;
        }        

};
void show(const Computer &computer) {
    computer.print();
}

int main()
{
    Computer c("SNSV", "Longitude 555", "i11-1234X", 16, 512);
    Laptop l(c, 15, 50);
    Desktop d("Optimus", "PW-000", "i13-4321X", 96, 4096, "SFF", "550W 80 Plus Gold");
    cout << "Specyfikacja komputera:" <<endl;
    c.print();

    cout << "Specyfikacja laptopa:" <<endl;
    l.print();

    cout << "Specyfikacja desktopa:" <<endl;
    d.print();
    show(c);
    show(l);
    show(d);
    return 0;
}