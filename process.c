#include<stdio.h>
#include<stdlib.h>
#include<sys/wait.h>
#include<sys/types.h>
#include<unistd.h>
#include<fcntl.h>

int main(){
    pid_t pid;
    int fd,status;
    
    printf("parent process is:%d",getpid());
    fd=open("file1.txt",O_CREAT|O_WRONLY,0644);
    
    if(fd<0){
        printf("file failed");
        exit(1);
    }
    
    printf("file opened:%d",fd);
    
    pid=fork();
    
    if(pid<0){
        printf("child processes failed");
    }
    
    if(pid==0){
        printf("child processes created");
        printf("child process id :%d",getpid());
        close(fd);
    }
    else{
        wait(&status);
        printf("parent process resumed");
        printf("parent process status:%d",status);
        printf("parent process to exit");
        close(fd);
    }
}