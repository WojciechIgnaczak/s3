#include <iostream>
using namespace std;
class Animal{
public:
    Animal(const string &_name, int _age): name(_name), age(_age), id(++counter){};
    Animal(const Animal &source){
        name=source.name;
        age=source.age;
        id=++counter;
    }
    virtual string move()=0;
    virtual string name_of_animal()=0;
    virtual ~Animal(){};
    Animal& operator=(const Animal& source){
        age=source.age;
        return *this;
    }
    Animal& operator++(int)
    {
        age++;
        return *this;
    }
    string name;
    int age;
    int getId(){
        return id;
    }
    const void show(){

    }
    private:
    int id;
    static unsigned int counter;

};

unsigned int Animal::counter=0;


class Elephant:public Animal{
public:
    Elephant(const string &_name, int _age,int _trunk_lenght):Animal(_name,_age),trunk_length(_trunk_lenght){};
    virtual string move() override{
        return("Slow\n");
    }
    virtual string name_of_animal() override{
        return name;
    }
    
    ~Elephant(){};
    void set_trunk_lenght(int _trunk_lenght)
    {
        trunk_length=_trunk_lenght;
    }
    const void show(){
        cout<<name<<" , "<<age<<" , "<<trunk_length<<endl;
    }
private:
int trunk_length;
friend ostream& operator<<(ostream &os, const Elephant &obj);

};


class Snake:public Animal{
public:
    Snake(const string &_name,int _age,int _lenght):Animal(_name,_age), lenght(_lenght){};
    ~Snake(){};

    virtual string move() override{
        return ("Fast\n");
    }
    virtual string name_of_animal() override{
        return name;
    }
    void set_lenght(int _lenght)
    {
        lenght=_lenght;
    }
    const void show(){
        cout<<name<<" , "<<age<<" , "<<lenght<<endl;
    }
private:
int lenght;
friend ostream& operator<<(ostream &os, const Snake &obj);
};

ostream& operator<<(ostream &os, const Elephant &obj){
    os<<"nazwa: "<<obj.name<<", wiek: "<<obj.age<<", długość trąby: "<<obj.trunk_length<<" m"<<endl;
    return os;
}
ostream& operator<<(ostream &os, const Snake &obj){
    os<<"Nazwa: "<<obj.name<<", wiek: "<<obj.age<<", długość: "<<obj.lenght<<" m"<<endl;
    return os;
}


int main(){
    Snake s("wąż",29,1);
    Snake s1("wąż",20,1);
    s1.show();
    s=s1;
    s1.show();
    s.show();
    s++;
    s.show();
    Snake s2(s1);
    Snake *a=new Snake("wąż4",10,10);
    a->show();
return 0;
}