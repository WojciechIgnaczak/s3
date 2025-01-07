//condition variable
#include<iostream>
#include<thread>
#include <string>
#include <unistd.h>
#include <mutex>
#include<condition_variable>

std::mutex mutex;
std::condition_variable cv;
std::string sharedString;
bool flag=false;

void threadFunc()
{
    std::cout<<"watek oczekuje na zmiane flagi\n";
    std::unique_lock lock(mutex);

    cv.wait(lock,[]{return flag;});
    std::cout<<"watek zaczyna dzialanie\n";
    std::cout<<sharedString<<std::endl;
    sharedString="zmiana w thread";

}

int main()
{
    std::thread t(threadFunc);

    sleep(3);
    {
        std::lock_guard lock(mutex);
        sharedString="zmiana w main()";
        flag=true;
        cv.notify_one();
    }

    // sharedString="ala ma kota";
    // std::cout<<"main zmienia flage\n";
    // flag=true;
    // while(flag);
    // std::cout<<sharedString<<std::endl;
    t.join();
    return 0;
}