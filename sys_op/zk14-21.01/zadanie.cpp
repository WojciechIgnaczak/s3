#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <map>
#include<cmath>
#include <exception>
class BuddyAllocator
{
public:
    BuddyAllocator(size_t _size, unsigned int _limit)
    {
        size=_size;
        limit=_limit;
        if (size%2 !=0)
        {
            throw std::logic_error("size must be the power of 2.");
        }

    }
    size_t size;
    unsigned int limit;
    std::map<unsigned int, unsigned int> mapa;
    ~BuddyAllocator(){};
    std::pair<size_t, size_t> alloc(size_t size)
    {
        unsigned int block_size = pow(2,(ceil(log2(size))));
        auto alokacja = std::make_pair(10, block_size);   
        return alokacja;     
    }
    void free(unsigned int address, size_t size)
    {

    }

};

int main()
{
    try{
        BuddyAllocator b(1024,5);
    }
    catch(const std::exception &e)
    {
        std::cout<<e.what()<<std::endl;
    }
    return 0;
}