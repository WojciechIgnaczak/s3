#include <stdexcept>
#include <iostream>
double mydiv(double a,double b)
{
    if (b==0){ throw std::invalid_argument("BOOM!");}
    else{return a/b;}
}

int main()
{
    try
    {
        mydiv(5,0);
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }
    
}