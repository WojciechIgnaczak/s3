#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

class Item
{
public:
    const std::string& getName(){return name;}  
    unsigned int getID(){return id;}       
    static unsigned int getCount(){return counter;} 

protected:
    Item(const std::string &_name): name(_name), id(++counter){}; 

private:
    string name;
    unsigned int id;
    static unsigned int counter;
};
unsigned int Item::counter=0;


class Weapon : public Item
{
public:
    Weapon(const std::string &name) : Item(name) {};
    virtual ~Weapon(){};
    virtual float getDamage() = 0;
    virtual bool isBroken() = 0;
    virtual void use() = 0;
    virtual void repair() = 0;
    void print(); 
};

void Weapon::print()
{
    if (isBroken()==false)
    {
    cout<<"Weapon "<<getName()<<" "<<getID()<<" results in "<<getDamage()<<" of damage points"<<endl;
    }else{
    cout<<"Weapon "<<getName()<<" "<<getID()<<" cannot be used, as it is broken"<<endl;
    }
}



class Sword : public Weapon
{
public:
    Sword() : Weapon("Sword") {};
    ~Sword() { std::cout << "Sword object is being destroyed..." << getID()<<std::endl; };
    virtual float getDamage() override {return baseDamage * sharpness;} 
    virtual bool isBroken() override {
        if (sharpness>0){return false;}
        else {return true;}
        }  
    virtual void use() override {
        print();
        sharpness=sharpness-0.1;
        }   

    virtual void repair() override {
        if (sharpness*1.1<= 1){
            sharpness*=1.1;
        }else{sharpness=1;}
    } 

private:
    const float baseDamage = 8.125;
    float sharpness = 0.5;
};



class Hammer : public Weapon
{
public:
    Hammer() : Weapon("Hammer") {};
    ~Hammer() { std::cout << "Hammer object is being destroyed... "<<getID() << std::endl; };

    virtual float getDamage() override
    {
        if (durability>0){return damage;}  
        return 0;
    } 

    virtual bool isBroken() override{
        if (durability==0){return true;}
        else{return false;}
    } 

    virtual void use() override{
        print();
        durability--;
    }     
    virtual void repair() override{
        durability=defaultDurability;
    }  

private:
    static const unsigned int defaultDurability = 4;
    const float damage = 3.5;
    unsigned int durability = defaultDurability;
};



int main()
{
srand(time(NULL));

Weapon *equipment[5] = {
    new Sword,
    new Hammer,
    new Sword,
    new Hammer,
    new Sword
};
size_t len=sizeof(equipment)/sizeof(equipment[0]);
bool broken=true;

while (broken) 
{
    for(int i=0;i<len;i++)
    {
    broken=false;
        if(equipment[i]->isBroken()==false)
        {
        broken=true;
        }
    }      
    for (int j = 0; j < len; ++j) {
        if (equipment[j]->isBroken() == false) {
            equipment[j]->use();
            bool shouldRepair = (rand() % 10) == 0;
            if (shouldRepair) {
                equipment[j]->repair();
            }
        }
    }
}

    for (int j = 0; j < len; ++j) {
        delete equipment[j];
    }

/*while (equipment[0]->isBroken() == false || equipment[1]->isBroken() == false || equipment[2]->isBroken() == false ||equipment[3]->isBroken() == false) 
{
    for (int j = 0; j < 4; ++j) {
        if (equipment[j]->isBroken() == false) {
            equipment[j]->use();
            bool shouldRepair = (rand() % 20) == 0;
            if (shouldRepair) {
                equipment[j]->repair();
            }
        }
    }
}

    for (int j = 0; j < 4; ++j) {
        delete equipment[j];
    }
*/
    return 0;
}