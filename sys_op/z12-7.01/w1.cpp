// active wait - zajmuje 100% procesora
#include<iostream>
#include<thread>
#include <string>
#include <unistd.h>

std::string sharedString;
volatile bool flag=false;

void threadFunc()
{
    std::cout<<"watek oczekuje na zmiane flagi\n";
    while(!flag);
    sleep(3);
    std::cout<<"watek zaczyna dzialanie\n";
    std::cout<<sharedString<<std::endl;
    sharedString="kot ma ale";
    flag=false;
}

int main()
{
    std::thread t(threadFunc);

    sleep(2);
    sharedString="ala ma kota";
    std::cout<<"main zmienia flage\n";
    flag=true;
    while(flag);
    std::cout<<sharedString<<std::endl;
    t.join();
    return 0;
}