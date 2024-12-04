#include<iostream>
#include<vector>
using namespace std;
class Item{
public:
    virtual void show()=0;
};

class ItemSword: public Item{
public:
    virtual void show() override{cout<<"This is Sword"<<endl;
    }
};

class ItemHammer: public Item{
    public:
virtual void show() override{cout<<"This is Hammer"<<endl;
    }
};

class ItemFactory{
public:
    enum ItemType {Sword, Hammer};
    static Item* createItem(ItemType type){
       // Item *item=nullptr;
            switch (type)
            {
            case Sword: return new ItemSword();
            case Hammer: return new ItemHammer();
            default: return nullptr;
            }
    }
private:
    ItemFactory()=default;
};

int main()
{
vector<Item*> items;
for(int i=0;i<10;i++){
    ItemFactory::ItemType type=(rand()%2)? ItemFactory::ItemType::Sword : ItemFactory::ItemType::Hammer;
    items.push_back(ItemFactory::createItem(type));
}
for(int i=0;i<items.size();i++){
    items[i]->show();
}


return 0;
}