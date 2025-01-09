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

    if (argc != 3) {
        printf("BŁĘDNA ILOŚĆ ARGUMENTÓW\n");
        return -1;
    }

    int number_of_processes = atoi(argv[2]);
    if (number_of_processes <= 0) {
        printf("ZA MAŁO PROCESÓW\n");
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

    char *content = mmap(NULL, statbuf.st_size, PROT_READ, MAP_SHARED, fd, 0);
    if (content == MAP_FAILED) {
        printf("BŁĄD MAPOWANIA PLIKU\n");
        close(fd);
        return EXIT_FAILURE;
    }

    int prot = PROT_READ | PROT_WRITE;
    int vis = MAP_SHARED | MAP_ANONYMOUS;
    shared_t *shr = (shared_t *)mmap(NULL, sizeof(shared_t), prot, vis, -1, 0);
    if (shr == MAP_FAILED) {
        printf("BŁĄD ALOKACJI PAMIĘCI\n");
        munmap(content, statbuf.st_size);
        close(fd);
        return EXIT_FAILURE;
    }

    pthread_mutexattr_t mutexattr;
    if (pthread_mutexattr_init(&mutexattr) != 0 || pthread_mutexattr_setpshared(&mutexattr, PTHREAD_PROCESS_SHARED) != 0 || pthread_mutex_init(&shr->mutex, &mutexattr) != 0) 
    {
        printf("BŁĄD INICJALIZACJI MUTEX\n");
        munmap(content, statbuf.st_size);
        munmap(shr, sizeof(shared_t));
        close(fd);
        return EXIT_FAILURE;
    }

    for (int i = 0; i < TAB_LENGTH; i++) {
        shr->tab[i] = 0;
    }

    size_t segment_size = statbuf.st_size / number_of_processes;
    size_t remainder = statbuf.st_size % number_of_processes;

    pid_t pids[number_of_processes];

    for (int i = 0; i < number_of_processes; i++) {
        size_t start = i * segment_size;
        size_t end = (i == number_of_processes - 1) ? statbuf.st_size : start + segment_size;

        pid_t pid = fork();
        if (pid == -1) {
            printf("BŁĄD FORK\n");
            munmap(content, statbuf.st_size);
            munmap(shr, sizeof(shared_t));
            close(fd);
            return EXIT_FAILURE;
        }

        if (pid == 0) {
            int local_count[TAB_LENGTH] = {0};

            for (size_t j = start; j < end; j++) {
                if (content[j] >= '0' && content[j] <= '9') {
                    local_count[content[j] - '0']++;
                }
            }

            pthread_mutex_lock(&shr->mutex);
            for (int k = 0; k < TAB_LENGTH; k++) {
                shr->tab[k] += local_count[k];
            }
            pthread_mutex_unlock(&shr->mutex);

            munmap(content, statbuf.st_size);
            munmap(shr, sizeof(shared_t));
            exit(0);
        } else {
            pids[i] = pid;
        }
    }

    for (int i = 0; i < number_of_processes; i++) {
        waitpid(pids[i], NULL, 0);
    }

    for (int i = 0; i < TAB_LENGTH; i++) {
        printf("%d = %d\n", i, shr->tab[i]);
    }

    pthread_mutex_destroy(&shr->mutex);
    munmap(content, statbuf.st_size);
    munmap(shr, sizeof(shared_t));
    close(fd);

    return 0;
}
