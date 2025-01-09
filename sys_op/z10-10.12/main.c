#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>

char *buffer = NULL;
size_t buffer_size = 0;
char *file_path = NULL;
int running = 1;

void load_file_to_buffer() {
    FILE *file = fopen(file_path, "r");
    if (!file) {
        return;
    }

    fseek(file, 0, SEEK_END);
    buffer_size = ftell(file);
    fseek(file, 0, SEEK_SET);


    free(buffer);
    buffer = malloc(buffer_size + 1);
    if (!buffer) {
        fclose(file);
        return;
    }

    fread(buffer, 1, buffer_size, file);
    buffer[buffer_size] = '\0';

    fclose(file);
}

void clear_buffer() {
    free(buffer);
    buffer = NULL;
    buffer_size = 0;
}

void handle_sigusr1(int signum) {
    (void)signum;
    load_file_to_buffer();
}

void handle_sigusr2(int signum) {
    (void)signum;
    clear_buffer();
}

void handle_sigint(int signum) {
    (void)signum;
    printf("\nCzy na pewno zakończyć program (y/n): ");
    char choice = getchar();
    if (choice == 'y') {
        running = 0;
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Nie podano pliku.\n");
        return -1;
    }

    file_path = argv[1];

    struct sigaction sa_usr1 = { .sa_handler = handle_sigusr1 };
    struct sigaction sa_usr2 = { .sa_handler = handle_sigusr2 };
    struct sigaction sa_int = { .sa_handler = handle_sigint };

    sigaction(SIGUSR1, &sa_usr1, NULL);
    sigaction(SIGUSR2, &sa_usr2, NULL);
    sigaction(SIGINT, &sa_int, NULL);

    load_file_to_buffer();

    while (running) {
        if (buffer) {
            printf("%s", buffer);
        } else {
            printf("Buffer pusty!\n");
        }
        sleep(1);
    }

    clear_buffer();
    return 0;
}
