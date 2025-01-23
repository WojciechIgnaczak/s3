// Shape
# include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <exception>
template <typename T>
class Shape{
public:
    Shape(){};
    virtual ~Shape(){};
    virtual T area()const =0;
};

template <typename T>
class Rectangle: public Shape<T>{ // prostokąt
public:
    Rectangle(T _a, T _b): a(_a),b(_b){
        if(a == 0 || b==0)
        {
            throw std::invalid_argument("BOK NIE MOŻE BYĆ ZERO");

        }
    };
    ~Rectangle(){};
    virtual T area()const override
    {
        return a*b;
    }
    T a;
    T b;
};

template <typename T>
class Square: public Shape<T>{ //kwadrat
public:
    Square(T _a): a(_a){
        if(a == 0)
        {
            throw std::invalid_argument("BOK NIE MOŻE BYĆ ZERO");

        }
    };
    ~Square(){};
    virtual T area()const override
    {
        return a*a;
    }
    T a;
    
};
int main()
{
    try {
        Rectangle<int> r1(2,11);
        std::cout<<"Powierzchnia rectangle int:"<<r1.area()<<std::endl;
        Rectangle<double> r2(2.0,1.0);
        std::cout<<"Powierzchnia rectangle double:"<<r2.area()<<std::endl;
        
        Square<int> s1(2);
        std::cout<<"Powierzchnia square int:"<<s1.area()<<std::endl;
        Square<double> s2(1.3);
        std::cout<<"Powierzchnia square double:"<<s2.area()<<std::endl;
        

    } catch(const std::exception& e) {
        std::cout << "Złapano wyjątek: " << e.what() << std::endl;}
    

    return 0;
}