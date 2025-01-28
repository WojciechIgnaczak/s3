CanvasListBookmark folder
Loading history...
  9:16 AM

#include <iostream>
#include <cstdlib>
using namespace std;
void foo(int &a){
// Zmień wartość przekazanej zmiennej o losową liczbę
// z przedziału [1,10]
    a=a+rand()%10+1;
}
int main(){
srand( time( NULL ) );
int a = 3;
foo(a);
// W tym momencie `a` powinno mieć wartość zmienioną o losową
// liczbę z przedziału [1,10], a więc powinno być
// w zakresie [4, 13]
cout << a << endl;
return EXIT_SUCCESS;
}













#include <iostream>
using namespace std;

class Foo {
private:
    int id;
    static int count; 

public:
    
    Foo() {
        id =++count;
    }

    
    int getId() {
        return id;
    }
};


int Foo::count = 0;

int main() {
    Foo a, b, c, d;
    cout << a.getId() << endl; // Powinno zostać wypisane 1
    cout << b.getId() << endl; // Powinno zostać wypisane 2
    cout << c.getId() << endl; // Powinno zostać wypisane 3
    cout << d.getId() << endl; // Powinno zostać wypisane 4

    return 0;}

#include <iostream>
using namespace std;
class Clock{
    private:
        int year,month,day,hour,minute,second;
    public:
        void display();
        void setTime(int year,int month,int day,int hour,int minute,int second=0)
        {
            this->year=year;
            this->month=month;
            this->day=day;
            this->hour=hour;
            this->minute=minute;
            this->second=second;
            display();
        }
        void setTime(int year,int month,int day)
        {
            this->year=year;
            this->month=month;
            this->day=day;
            display();
        }
        void setTime(int hour,int minute)
        {
            this->hour=hour;
            this->minute=minute;
            display();
        }
};

void Clock::display(){
    if(year<10){cout<<"0";} cout<<year<<"-";
    
    if(month<10){cout<<"0"; }cout<<month<<"-";

    if(day<10){cout<<"0";} cout<<day<<" ";

    if(hour < 10){cout << "0";} cout << hour << ":";
    
    if(minute < 10){cout << "0";} cout << minute << ":";
        
    if(second < 10){cout << "0";} cout << second << endl;
}


int main()
{
    Clock c;
// Ustawienie 2024-05-10, 08:30:20
    c.setTime(2024, 5, 10, 8, 30, 20);
// Ustawienie 2024-05-10, 08:30:00
    c.setTime(2024, 5, 10, 8, 30);
// Ustawienie 2024-05-10, godzina pozostaje bez zmian
    c.setTime(2024, 5, 10);
// Ustawienie godziny na 08:30:00, data pozostaje bez zmian
    c.setTime(8, 30);

    return 0;
}
#include <iostream>
using namespace std;
class A{
    private:
        int a,b;
    public:
    A(int a,int b): a(a),b(b){}
    
    int getA(){
        return a;
    }
    
    int getB(){
    return b;
    }
};

class B {
    private:
        int c;
        A klasaA;
    public:
        int d;
        B(int c,int d, int klasaAa, int klasaAb): c(c),d(d),klasaA(klasaAa,klasaAb){}
        void info() {
            cout << "c: " << c << endl;
            cout << "d: " << d << endl;
            cout << "klasaA.a: " << klasaA.getA() << endl;
            cout << "klasaA.b: " << klasaA.getB() << endl;
        }
};

int main(){
    
    B b(1,2,3,4);
    B * pb;
    pb = &b;
  
    pb -> info();
    return 0;
}

  10:54 AM
zadanie.c 

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

​

typedef struct shared {

    int tab[TAB_LENGTH];

    pthread_mutex_t mutex;

} shared_t;

​

int main(int argc, char *argv[]) {

    struct stat statbuf;

​

    if (argc != 3) {

        printf("BŁĘDNA ILOŚĆ ARGUMENTÓW\n");

        return -1;

    }

​

    int number_of_processes = atoi(argv[2]);

    if (number_of_processes <= 0) {

        printf("ZA MAŁO PROCESÓW\n");

        return -1;

    }

​

    int fd = open(argv[1], O_RDONLY);

    if (fd == -1) {

        printf("BŁĄD OTWIERANIA PLIKU\n");

        return -1;

    }

​

    if (fstat(fd, &statbuf) == -1) {

        printf("BŁĄD POBRANIA ROZMIARU\n");

        close(fd);

        return -1;

    }

​

    char *content = mmap(NULL, statbuf.st_size, PROT_READ, MAP_SHARED, fd, 0);

    if (content == MAP_FAILED) {

        printf("BŁĄD MAPOWANIA PLIKU\n");

        close(fd);

        return EXIT_FAILURE;

    }

​

    int prot = PROT_READ | PROT_WRITE;

    int vis = MAP_SHARED | MAP_ANONYMOUS;

    shared_t *shr = (shared_t *)mmap(NULL, sizeof(shared_t), prot, vis, -1, 0);

    if (shr == MAP_FAILED) {

        printf("BŁĄD ALOKACJI PAMIĘCI\n");

        munmap(content, statbuf.st_size);

        close(fd);

        return EXIT_FAILURE;

    }

​

    pthread_mutexattr_t mutexattr;

    if (pthread_mutexattr_init(&mutexattr) != 0 || pthread_mutexattr_setpshared(&mutexattr, PTHREAD_PROCESS_SHARED) != 0 || pthread_mutex_init(&shr->mutex, &mutexattr) != 0) 

    {

        printf("BŁĄD INICJALIZACJI MUTEX\n");

        munmap(content, statbuf.st_size);

        munmap(shr, sizeof(shared_t));

        close(fd);

        return EXIT_FAILURE;

    }

​

    for (int i = 0; i < TAB_LENGTH; i++) {

        shr->tab[i] = 0;

    }

​

    size_t segment_size = statbuf.st_size / number_of_processes;

    size_t remainder = statbuf.st_size % number_of_processes;

​

    pid_t pids[number_of_processes];

​

    for (int i = 0; i < number_of_processes; i++) {

        size_t start = i * segment_size;

        size_t end = (i == number_of_processes - 1) ? statbuf.st_size : start + segment_size;

​

        pid_t pid = fork();

        if (pid == -1) {

            printf("BŁĄD FORK\n");

            munmap(content, statbuf.st_size);

            munmap(shr, sizeof(shared_t));

            close(fd);

            return EXIT_FAILURE;

        }

​

        if (pid == 0) {

            int local_count[TAB_LENGTH] = {0};

​

            for (size_t j = start; j < end; j++) {

                if (content[j] >= '0' && content[j] <= '9') {

                    local_count[content[j] - '0']++;

                }

            }

​

            pthread_mutex_lock(&shr->mutex);

            for (int k = 0; k < TAB_LENGTH; k++) {

                shr->tab[k] += local_count[k];

            }

            pthread_mutex_unlock(&shr->mutex);

​

            munmap(content, statbuf.st_size);

            munmap(shr, sizeof(shared_t));

            exit(0);

        } else {

            pids[i] = pid;

        }

    }

​

    for (int i = 0; i < number_of_processes; i++) {

        waitpid(pids[i], NULL, 0);

    }

​

    for (int i = 0; i < TAB_LENGTH; i++) {

        printf("%d = %d\n", i, shr->tab[i]);

    }

​

    pthread_mutex_destroy(&shr->mutex);

    munmap(content, statbuf.st_size);

    munmap(shr, sizeof(shared_t));

    close(fd);

​

    return 0;

}

