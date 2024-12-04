#include<iostream>
#include<exception>
int main(){
    while(1){
        try{
            int *tab=new int[1000];
            throw std::exception();
        }catch(const std::exception &e){
            
        }
    }
    return 0;
}