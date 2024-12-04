//shared pointer
#include<iostream>

template <typename T>

class SharePtr{
private:
    int *refCounter;
    T *ptr;

public:
    SharePtr(T*ptr){
        this->ptr=ptr;
        this->refCounter=new int;
        *this->refCounter=1;
    }
    SharePtr(const SharePtr& other){
        std::cout<<"Kopiuowanie\n";
    this-> refCounter=other.refCounter;
    this->ptr=other.ptr;
    (*this->refCounter)++;  
    }
    ~SharePtr()
    {
        (*this->refCounter)--;  
        if(*this->refCounter==0){
            std::cout<<"Zwalnianiae pamieci\n";
            delete refCounter;
            delete ptr;
        }
    }
};

int main(){

    SharePtr<int> jakisInt(new int);
    
    SharePtr<int> Kopia(jakisInt);
    SharePtr<int> Kopia2(jakisInt);
    SharePtr<int> Kopia3(jakisInt);
    SharePtr<int> Kopia4(jakisInt);
    SharePtr<int> Kopia5(jakisInt);

    return 0;
}

