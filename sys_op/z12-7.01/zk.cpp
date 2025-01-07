#include <sys/stat.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include<thread>
#include<mutex>
#include <vector>
#include<string>

#define TAB_LENGTH 10


std:: mutex mtx;

typedef struct shared {

    int tab[TAB_LENGTH];

    pthread_mutex_t mutex;

} shared_t;

void count_digits(size_t start,size_t end, const std::string &content, int* global_count){
    int local_count[TAB_LENGTH]={0};

    for (size_t j = start; j < end; j++) {

        if (content[j] >= '0' && content[j] <= '9') {

            local_count[content[j] - '0']++;
        }
    }

    std::lock_guard lock(mtx);

    for (size_t i=0; i < TAB_LENGTH; i++) {
        global_count[i]+=local_count[i];
    }

}

int main(int argc, char *argv[]) {

    struct stat statbuf;

    if (argc != 3) {

        printf("BŁĘDNA ILOŚĆ ARGUMENTÓW\n");

        return -1;

    }

    int number_of_thread = atoi(argv[2]);

    if (number_of_thread <= 0) {

        printf("ZA MAŁO WĄTKÓW\n");

        return -1;

    }

    int fd = open(argv[1], O_RDONLY);

    if (fd == -1) {

        printf("BŁĄD OTWIERANIA PLIKU\n");

        return -1;

    }

    if (fstat(fd, &statbuf) == -1) {

        printf("BŁĄD POBRANIA ROZMIARU\n");

        close(fd);

        return -1;
    }
    
    char* content = (char*)mmap(NULL, statbuf.st_size, PROT_READ, MAP_SHARED, fd, 0);

    if (content == MAP_FAILED) {

        printf("BŁĄD MAPOWANIA PLIKU\n");

        close(fd);

        return EXIT_FAILURE;

    }


    int global_count[TAB_LENGTH]={0};
    size_t segment_size = statbuf.st_size / number_of_thread;

    size_t remainder = statbuf.st_size % number_of_thread;

    std::vector<std::thread> threads;

    for (int i = 0; i < number_of_thread; i++) {

        size_t start = i * segment_size;

        size_t end = (i == number_of_thread - 1) ? statbuf.st_size : start + segment_size;
        // wywołanie funckji digit_count na wątku
        threads.push_back(std::thread(start,end,std::ref(content),std::ref(global_count)));
    }


    for(auto &thread : threads)
    {
        thread.join();
    }
    for (int i = 0; i < TAB_LENGTH; i++) {

        printf("%d = %d\n", i, global_count[i]);

    }


    return 0;

}

