#include <iostream>
using namespace std;

class ICommand{
public:
    ICommand(){cout<<"Konstruktor klasy ICommand"<<endl;}
    virtual ~ICommand(){cout<<"Destruktor klasy ICommand"<<endl;}
    virtual char getCommand()const=0;
};
class SystemUptime: public ICommand{
public:
    SystemUptime(){cout<<"Konstruktor klasy SystemUptime"<<endl;}
    ~SystemUptime(){cout<<"Destruktor klasy SystemUptime"<<endl;}

    virtual char getCommand()const override{return 'U';}
};
class SystemMemory: public ICommand{
public:
    SystemMemory(){cout<<"Konstruktor klasy SystemUptime"<<endl;}
    ~SystemMemory(){cout<<"Destruktor klasy SystemUptime"<<endl;}
    virtual char getCommand()const override{return 'M';}
};

void printCommand(const ICommand *c)
{
    cout<<c->getCommand()<<endl;
}

int main(){
    ICommand *u=new SystemUptime();
    ICommand *m=new SystemMemory();
    printCommand(u);
    printCommand(m);
    delete u;
    delete m;
    return 0;
}