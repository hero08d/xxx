// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>
#define PAGE_SIZE 4
#define MEM_SIZE 20
#define NUM_PAGES 5 
int main() {
    int pagetb[NUM_PAGES]={2,3,4,6,7};
    int pyadd,logadd,offset,pageno;
    
    printf("enter the logical address:");
    scanf("%d",&logadd);
    
    if(logadd<0 || logadd>=MEM_SIZE){
        printf("invlid address");
    }
    pageno=logadd/PAGE_SIZE;
    offset=logadd%PAGE_SIZE;
    
    pyadd=(pagetb[pageno]*PAGE_SIZE)+offset;
    printf("Logical Address: %d -> Page: %d, Offset: %d\n", logadd, pageno, offset);
    printf("Mapped to Physical Address: %d\n", pyadd);

    return 0;
}
