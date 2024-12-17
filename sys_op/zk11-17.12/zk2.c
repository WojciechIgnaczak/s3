#include <string.h>
 #include <sys/stat.h>
 #include <sys/mman.h>
 #include <fcntl.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <pthread.h>
#include <unistd.h>
#define TAB_LENGTH 10
typedef struct shared {
    int tab[TAB_LENGTH];
    pthread_mutex_t mutex;
} shared_t;
int main(int argc, char *argv[]) {
    
    struct stat statbuf;
    if(argc !=3)
    {
        printf("BŁĘDNA ILOSC ARGUMENTOW\n");
        return -1;
    }
    printf("argc=%d\n", argc);
    int number_of_proccess=atoi(argv[2]);
    if(number_of_proccess<=0)
    {
        printf("ZA MAŁO PROCESÓW\n");
        return -1;
    }

    int fd = open(argv[1], O_RDONLY); 
    if(fd==-1)
    {
        printf("BŁĄD\n");
        return -1;
    }
    printf("fd=%d\n", fd);
    if(fstat(fd, &statbuf)==-1)
    {
        printf("ERROR GET SIZE\n");
        close(fd);
        return -1;
    }
    fstat(fd, &statbuf); 
    printf("len=%ld\n", statbuf.st_size);
    char *content = mmap(NULL, statbuf.st_size, PROT_READ, MAP_SHARED, fd, 0);
    printf("content ptr=%p\n", content);
//z wykladu ALOKACJA PAMIECI WSPOLDZIELONES
    int prot = PROT_READ | PROT_WRITE; // odczyt i zapis
    int vis = MAP_SHARED | MAP_ANONYMOUS;
    shared_t *shr = (shared_t*)mmap(NULL, sizeof(shared_t), prot, vis, -1, 0);
    if (shr == NULL)
        return -1;

    pthread_mutexattr_t mutexattr;
    if (pthread_mutexattr_init(&mutexattr) != 0)
        return -2;
    if (pthread_mutexattr_setpshared(&mutexattr, PTHREAD_PROCESS_SHARED) != 0)
        return -3;
    if (pthread_mutex_init(&shr->mutex, &mutexattr) != 0)
        return -4;
//z wykladu \>
    if(shr==NULL) return -1;

    for(int i=0;i<TAB_LENGTH;i++)
    {
        shr->tab[i]=0;
    }
    /* TODO: sprawdzic ret value z mmap */
    for (int i = 0; i < statbuf.st_size; i++)
    {
        /* [48, 57] */
        if (content[i] >= '0' && content[i] <= '9') { 
            int val = content[i] - '0'; /* content[i] - 48 */
            /* Zwiększyć odpowiednią wartość w tablicy,
               która zlicza ilość wystąpień */
            shr->tab[val]++;
            //printf("%d", val);
        }
    }

    for(int i=0;i<TAB_LENGTH;i++)
    {
        printf("%d = %d\n",i,shr->tab[i]);
    }

// fork i podzial zakresow
    munmap(content, statbuf.st_size);
    close(fd);
    return 0;
}