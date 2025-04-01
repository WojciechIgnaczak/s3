#include <iostream>

class Foo{
public:
    int x_;
    Foo(int x):x_(x){
        std::cout<<"HELLO\n";
    }
    ~Foo(){
        std::cout<<"DEL\n";
    }
};

int main()
{
    Foo f=Foo(123);
    
    int x=2,y=0;
    std::cout<<(x/y)<<std::endl;
    return 0;
}