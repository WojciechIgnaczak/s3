//mmap mutex

#include <stdio.h>
#include <pthread.h>
#include<sys/mman.h>
#define TAB_LENGTH 10
typedef struct shared{
    int tab[TAB_LENGTH];
    pthread_mutex_t mutex;
} shared_t;

child(shared_t *shr)
{
    int n=0;
    while(1)
    {
        pthread_mutex_lock(&shr->mutex);
        for(int i=0;i<TAB_LENGTH;i++)
        {
            shr->tab[i]=n;
        }
        pthread_mutex_unlock(&shr->mutex);

        n++;
    }
}

parent(shared_t *shr)
{
    int n=0;
    while(1)
    {
        pthread_mutex_lock(&shr->mutex);

        for(int i=0;i<TAB_LENGTH;i++)
        {
            printf("%d ",shr->tab[i]);
        }
        pthread_mutex_unlock(&shr->mutex);

        printf("\n");
    }
}
int main()
{
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
    pthread_mutex_destroy(&shr->mutex);
    munmap(shr, sizeof(shared_t));
    return 0;
}