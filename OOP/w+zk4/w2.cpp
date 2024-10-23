#include<iostream>
#include<cmath>
using namespace std;

class Shape {
public:
    virtual ~Shape(){};
    virtual double circum() = 0;
    virtual double area() = 0;
};

class Rectangular : public Shape {
public:
    Rectangular(double w, double h) : width(w), height(h) {};
    double circum(){return width*2+height*2;}
    double area(){return width*height;}
private:
    double width, height;
};

class Circle : public Shape {
public:
    Circle(double r) : radius(r) {};
    double circum(){return 2*M_PI*radius;}
    double area(){return M_PI*radius*radius;}
private:
    double radius;
};

void print(Shape &s)
{
cout<<"Obwód "<<s.circum()<<"  pole "<<s.area()<<endl;
}

int main()
{
Rectangular rect(20,10);
print(rect);
Circle cir(2);
print(cir);
return 0;
}