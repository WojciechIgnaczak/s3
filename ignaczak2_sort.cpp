//Sorter
# include <iostream>
#include <cstdlib>
#include <stdio.h>
#include<vector>
#include<exception>


template <typename T>
class Sorter{
public:
    Sorter(){};
    virtual ~Sorter(){};
    virtual void sort(bool descending)=0;//descening true -> malejąco
};


template <typename T>
class BubbleSorter: public Sorter<T>
{
public:
    std::vector<T>&v;
    BubbleSorter(std::vector<T>&_v):v(_v){}; //O(n^2)
    ~BubbleSorter(){};
    virtual void sort(bool descending) override{ //descening true -> malejąco
        if(v.size()==0){throw std::invalid_argument("WEKTOR NIE MOŻE BYĆ PUSTY");}
        if(descending==false){
            for (size_t i = 0; i < v.size() - 1; ++i) {
                for (size_t j = 0; j < v.size() - i - 1; ++j) {
                    if (v[j] > v[j + 1]) {
                        std::swap(v[j], v[j + 1]);
                    }
                }
            }
        }
        if(descending==true){
            
            for (size_t i = 0; i < v.size() - 1; ++i) {
                for (size_t j = 0; j < v.size() - i - 1; ++j) {
                    if (v[j] < v[j + 1]) {
                        std::swap(v[j], v[j + 1]);
                    }
                }
            }
        }
            
        
        
    }    
};

int main()
{
    try {
        std::vector<double> v{5.2,-5.1,6,10.001,1111};
        std::cout<<"WEKTOR\n";
        for (auto liczba : v) {
            std::cout << liczba << "\n";
        }
        auto s=BubbleSorter<double>(v);
        std::cout<<"\nSORTOWANIE BĄBELKOWE MALEJĄCO\n";
        s.sort(true);
        for (auto liczba : v) {
            std::cout << liczba << "\n";
        }
        std::cout<<"\nSORTOWANIE BĄBELKOWE ROSNĄCO\n";
        s.sort(false);
        for (auto liczba2 : v) {
            std::cout << liczba2 << "\n";
        }
    
    }catch(const std::exception& e) {
        std::cout << e.what() << std::endl;}
    return 0;
}