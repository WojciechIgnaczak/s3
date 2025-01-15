#include <iostream>
#include <stdio.h>
#include <cmath>

template <typename T>
class Vector
{    
public:
    Vector(){};
    virtual ~Vector(){};
    virtual double length() const = 0;
    virtual void normalize() = 0;
};

template <typename T>
class Vector2D: public Vector<T>
{
public:
    Vector2D(T _xA, T _yA): x_A(_xA), y_A(_yA){};
    ~Vector2D(){};
    virtual double length() const override
    {
        double result= sqrt(pow(x_A,2)+pow(y_A,2));
        return result;
    }
    virtual void normalize() override // podzielenie składowych przez dlugosc
    {
        double normalize_lenght=length();
        x_A=x_A/normalize_lenght;
        y_A=y_A/normalize_lenght;
    }
    double result_length;
    T x_A;
    T y_A;
};

template <typename T>
class Vector3D: public Vector2D<T>
{   
public:
    Vector3D(T _xA, T _yA, T _zA): Vector2D<T>(_xA, _yA),z_A(_zA){};
    ~Vector3D(){};
    virtual double length() const override
    {
        double result= sqrt(pow(this->x_A,2)+pow(this->y_A,2)+pow(z_A,2));
        return result;
    }

    virtual void normalize() override
    {
        double normalize_lenght=length();
        this->x_A=this->x_A/normalize_lenght;
        this->y_A=this->y_A/normalize_lenght;
        z_A=z_A/normalize_lenght;
    }
    T z_A;

};

template <typename T>
std::ostream& operator<<(std::ostream &os, const Vector2D<T> &obj)
{
    os <<"\nWspółrzędne wektora:";
    os <<obj.x_A<<", "<<obj.y_A<<"\n";
    return os;
}

template <typename T>
std::ostream& operator<<(std::ostream &os, const Vector3D<T> &obj)
{
    os <<"\nWspółrzędne wektora:";
    os <<obj.x_A<<", "<<obj.y_A<<", "<<obj.z_A<<"\n";
    return os;
}

int main()
{
    Vector2D<double> t(1,2);
    std::cout<<t;
    std::cout<<"Długość wektora 2D: "<<t.length()<<std::endl;
    t.normalize();
    std::cout<<t<<std::endl;

    Vector3D<double> t1(1,2,2);
    std::cout<<t1;
    std::cout<<"Długość wektora 3D: "<<t1.length()<<std::endl;
    t1.normalize();
    std::cout<<t1;
    return 0;
}