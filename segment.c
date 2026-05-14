#include<stdio.h>
#include<stdlib.h>

struct segment{
    int limit;
    int base;
};
int main(){
    struct segment segtb[3]={{1000,234},{1200,254},{1400,546}};
    int segno,offset,phyadd;
    
    printf("enter the offset and segno:");
    scanf("%d%d",&offset,&segno);
    
    if(segno<0 || segno>=3){
        printf("invalid segno");
    }
    else if (offset>=segtb[segno].limit){
        printf("trap here");
    }
    else{
        phyadd=segtb[segno].base+offset;
        printf("the physical address is :%d",phyadd);
    }
}