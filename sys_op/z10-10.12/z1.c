#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
char *file_path;
char *buffer;
char *buffer_size;
int stop_program=0;
int clear=0;
int reload_buffer=0;

void load_file(){
    
    FILE *file=fopen(file_path,"r");
    if(file==NULL){
        fprintf(stderr,"Błąd pliku\n");
        return;
    }

    fseek(file, 0 , SEEK_END);
    size_t size= ftell(file);
    fseek( file, 0, SEEK_SET );
    fclose(file);
    free(buffer);
}
void clear_buffer(){
    free(buffer);
    buffer=NULL;
}

void signusr1_handler(int sig){
    (void)sig;
    reload_buffer=1;
    //reload musze zrobic
}

void signusr2_handler(int sig){
    (void)sig;
    clear=1;
}

void signint_handler(int sig){
    (void)sig;
    stop_program=1;
}

int main(int argc, char *argv[]) {
    struct sigaction sa_usr1={0};
    struct sigaction sa_usr2={0};
    struct sigaction sa_int={0};
    sa_usr1.sa_handler=signusr1_handler;
    sa_usr2.sa_handler=signusr2_handler;
    sa_int.sa_handler=signint_handler;

    sigaction(SIGUSR1, &sa_usr1,NULL);
    sigaction(SIGUSR2, &sa_usr1,NULL);
    sigaction(SIGINT, &sa_usr1,NULL);

    if (argc < 2) {
        fprintf(stderr,"Brak pliku\n");
        return -1;
    }
    load_file();
    
    while(1)
    {
        if(stop_program){
            printf("\n Czy chcesz wyjść z programy? (y/n)");
            char response=getchar();
            if(response=='y')
            {
                break;
            }else{
                stop_program=0;
            }
        }

        if(reload_buffer)
        {
            load_file();
            reload_buffer=0;
        }

        if(clear)
        {
            clear_buffer();
        }

        if(buffer != NULL)
        {
            printf("%s",buffer);
        }else{
            printf("Bufor pusty");
        }

        sleep(1);
    }

    free(buffer);
    return 0;
}