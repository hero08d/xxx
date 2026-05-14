// Online C compiler to run C program online
#include <stdio.h>
#include<stdlib.h>
int mutex=1;
int full=0;
int empty;
int buffersize;
    
int signal(int s){
    return ++s;
}
    
int wait(int s){
    return --s;
}
    
void producer(){
    mutex=wait(mutex);
    empty=wait(empty);
    full=signal(full);
    printf("full:%d|empty:%d",full,empty);
    mutex=signal(mutex);
}
    
void consumer(){
    mutex=wait(mutex);
    full=wait(full);
    empty=signal(empty);
    printf("full:%d|empty:%d",full,empty);
    mutex=signal(mutex);    
}
int main(){
    int choice;
    printf("enter buffersize:");
    scanf("%d",&buffersize);
    empty=buffersize;
    while(1){
        printf("\n1.consumer\t 2. producer \t 3.exit\n");
        printf("\nenter the choice:");
        scanf("%d",&choice);
        switch (choice) {
            case 1:
                if (full != 0) consumer();
                else printf("Buffer Empty!\n");
                break; // Essential!

            case 2:
                if (empty != 0) producer();
                else printf("Buffer Full!\n");
                break; // Essential!

            case 3:
                exit(0);

            default:
                printf("Invalid choice\n");
        }
    }
}