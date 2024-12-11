#include <iostream>
#include <thread>
#include <vector>
void loop(int n)
{
    for(int i=0;i<200000000;i++);
    std::cout<<"koniec watku "<<n<<std::endl;
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

    
    return 0;

}