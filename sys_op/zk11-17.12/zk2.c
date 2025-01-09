#include <string.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/wait.h>
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
   // printf("argc=%d\n", argc);
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
    //printf("fd=%d\n", fd);
    if(fstat(fd, &statbuf)==-1)
    {
        printf("ERROR GET SIZE\n");
        close(fd);
        return -1;
    }
    //fstat(fd, &statbuf); 
    //printf("len=%ld\n", statbuf.st_size);
    char *content = mmap(NULL, statbuf.st_size, PROT_READ, MAP_SHARED, fd, 0);
    if (content == MAP_FAILED) {
        perror("Error mapping file");
        close(fd);
        return EXIT_FAILURE;
    }
    //printf("content ptr=%p\n", content);
//z wykladu ALOKACJA PAMIECI WSPOLDZIELONES \>
    int prot = PROT_READ | PROT_WRITE; // odczyt i zapis
    int vis = MAP_SHARED | MAP_ANONYMOUS;
    shared_t *shr = (shared_t*)mmap(NULL, sizeof(shared_t), prot, vis, -1, 0);
    if (shr == MAP_FAILED)
        return EXIT_FAILURE;

    pthread_mutexattr_t mutexattr;
    if (pthread_mutexattr_init(&mutexattr) != 0)
        return -2;
    if (pthread_mutexattr_setpshared(&mutexattr, PTHREAD_PROCESS_SHARED) != 0)
        return -3;
    if (pthread_mutex_init(&shr->mutex, &mutexattr) != 0)
        return -4;
//z wykladu \>

    for(int i=0;i<TAB_LENGTH;i++)
    {
        shr->tab[i]=0;
    }
    /* TODO: sprawdzic ret value z mmap */

    

// fork i podzial zakresow
// podział zakresów
    size_t segment_size = statbuf.st_size / number_of_proccess;
    size_t remainder = statbuf.st_size % number_of_proccess;

    pid_t pids[number_of_proccess];

// Fork 
    //int*pid_table=malloc(sizeof(int)*number_of_proccess);
    for (int i = 0; i < number_of_proccess; i++) {
        //printf("WĄTEK: %d",i);
        //size_t added=(i>0) ? 1: 0;
        size_t start = i * segment_size;
       // size_t  lengt= segment_size + (i == number_of_proccess - 1 ? remainder : 0)-added;
        size_t end= (i == number_of_proccess-1) ? statbuf.st_size : start+segment_size;
        //printf("Długosc: %ld Start: %ld, Koniec: %ld, ad\n",segment_size,start,start+length);
        pid_t pid=fork();
       //printf("start: %ld, end: %ld", start,end);
        switch (pid) {
        case -1: /* coś poszło nie tak */
            printf("ERROR");
            return -5;
        case 0: /* jesteśmy w nowym procesie */
        //printf("CHILD: %d\n",pid_table[i]);
            //process segment
            int local_count[TAB_LENGTH]={0};
            for (int j = start; j < end; j++)
            {
            /* [48, 57] */
                if (content[j] >= '0' && content[j] <= '9') { 
                    //int val = content[i] - '0'; /* content[i] - 48 */
                    local_count[content[j]-'0']++;
                    /* Zwiększyć odpowiednią wartość w tablicy,
                    która zlicza ilość wystąpień */
                    //printf("%d", val);
                }
                
                //return 0;
            }
            pthread_mutex_lock(&shr->mutex); // wyniki do tablicy o dopiero mutex
            for(int k=0;k<TAB_LENGTH;k++)
            {
                shr->tab[k]+=local_count[k];
            }
            pthread_mutex_unlock(&shr->mutex);
        
        default: /* jesteśmy w starym procesie */
            pids[i]=pid;
            //printf("parent: %d\n",pid_table[i]);
        }
    }

// Wait
    for (int i = 0; i < number_of_proccess; i++) {
        waitpid(pids[i], NULL,0);
    }
    for(int i=0;i<TAB_LENGTH;i++)
    {
        printf("%d = %d\n",i,shr->tab[i]);
    }
    munmap(content, statbuf.st_size);
    pthread_mutex_destroy(&shr->mutex);

    close(fd);
    return 0;
}