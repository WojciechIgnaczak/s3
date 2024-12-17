//mmap mutex

#include <stdio.h>
#include <pthread.h>
#include<sys/mman.h>
#include <fcntl.h> //open
#include<unistd.h>
#define TAB_LENGTH 10
typedef struct shared{
    int tab[TAB_LENGTH];
    pthread_mutex_t mutex;
} shared_t;

int main(int argc,char * argv[])
{   
// wejście i otwarcie pliku
    if(argc <2)
    {
        printf("Błędne podane argumenty!\n");
    }
    int n=atoi(argv[2]); //ilość procesów
    char *path=argv[1]; //sciezka do pliku
    int fd=open(path,O_RDONLY); // TODO sprawdz ret value

// rozmiar pliku
    fseek(path, 0, SEEK_END); // seek to end of file
    size_t size = ftell(path); // get current file pointer
    fseek(path, 0, SEEK_SET);// rozmiar

// mmap
    char *file_content = mmap(NULL, size, PROT_READ, 0, fd, 0); // TODO spradz ret value

// oblicz rozmiar segmentow
    size_t segment_size=size/n;
    size_t remainder = size % n;
    pid_t pids[n];

//forkowanie procesu




    int prot = PROT_READ | PROT_WRITE;
    int vis= MAP_SHARED | MAP_ANONYMOUS;
    shared_t *shr= (shared_t*)mmap(NULL,sizeof(shared_t),prot,vis,-1,0);
    if(shr==NULL)
    {
        return -1;
    }
    pthread_mutexattr_t mutexattr;
    if (pthread_mutexattr_init(&mutexattr) != 0)
    {return -2;}
    if (pthread_mutexattr_setpshared(&mutexattr, PTHREAD_PROCESS_SHARED) != 0)
    {return -3;}
    if ( pthread_mutex_init(&shr->mutex, &mutexattr) != 0)
    {return -4;}

    pid_t pid=fork();
    switch(pid)
    {
        case -1: // nowy proces
            return -5;
        case 0: //coś nie tak
            child(shr);
            break;
        default: // stary proces
            parent(shr);
            break;
    }




// znak czy cyfra, zliczanie liczb, to przykład zmień na plik
    //char str[]="834848847578383848483838"; // zmien to na plik i rozmiar pliku !!!!!!!!!!!!!do wyjebania!!!!!!!
    unsigned long long int wystapienia[10];
    for (int i=0;i<size;i++)
    {
        pthread_mutex_lock(&shr->mutex); // zmien to bo wolne, podzile na tablice 10 elementowe ile procesow
        if(file_content[i]>='0' && file_content[i]<='9')
        {
            int val=file_content[i]-'0';
            //zwiekszyc odpowiednia wartosc tablicy ktora zlicza ilosc wystapien
            wystapienia[val]++;
        }
        pthread_mutex_unlock(&shr->mutex); // zmien to bo wolne, podzile na tablice 10 elementowe ile procesow

    }

// czyszczenie
    pthread_mutex_destroy(&shr->mutex);
    munmap(file_content,size);
    close(fd);
    return 0;
}