#include <iostream>
using namespace std;

class Complex{
    public:
        Complex(double _re,double _im): re(_re), im(_im){};
        Complex(double _re):re(_re),im(0){};

    double real()const{return re;};
    double imag()const{return im;};
    Complex operator+(const Complex &c);
    Complex operator-(const Complex &c);
    Complex& operator+=(const Complex &c);
    Complex& operator-=(const Complex &c);
    Complex operator-(); //unarny jednoargumentowy
    Complex operator*(double x);
    Complex operator*(const Complex &c);

    private:
        double re,im;
};


Complex Complex::operator+(const Complex &c){
    return Complex(re+c.re,im+c.im);
}

Complex Complex::operator-(const Complex &c){
    return Complex(re-c.re,im-c.im);
}

Complex &Complex::operator+=(const Complex &c){
    re+=c.re;
    im+=c.im;
    return *this;
}

Complex &Complex::operator-=(const Complex &c){
    re-=c.re;
    im-=c.im;
    return *this; 
}

Complex Complex::operator-(){
    return Complex(-re,-im);
}

Complex Complex::operator*(double x){
    return Complex(re*x,im*x);
}

Complex Complex::operator*(const Complex &c)
{
    return Complex(re*c.re+im*c.im*(-1),re*c.im+im*c.re);
}

ostream& operator<<(ostream &os, const Complex &obj) {
    if (obj.imag()>=0)
    {
        os << obj.real() << "+" << obj.imag() << "i";
    }
    else
    {
        os << obj.real() <<obj.imag() << "i";
    }
    return os;
};

int main()
{
Complex c1(1,1);
Complex c2(2,2);
cout<<c1*c2<<endl;
return 0;
}