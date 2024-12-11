#include <iostream>
#include <thread>
#include <vector>
#include <atomic>
std::atomic<int> zmienna=0;
void loop(int n)
{
    for(int i=0;i<100000;i++)
    {
        zmienna.fetch_add(1);
    }
}
int main()
{
    unsigned int hwThreads= std::thread::hardware_concurrency();
    hwThreads= hwThreads ? hwThreads : 1;
    std::vector<std::thread> threads;
    for(int i=0;i<hwThreads;i++)
    {
        threads.push_back(std::thread(loop,i));
    }
    for(int i=0;i<hwThreads;i++)
    {
        std::cout<<"oczekiwanie na watek"<<std::endl;
        threads[i].join();
    }

    std::cout<<zmienna.load()<<std::endl;
    
    return 0;

}