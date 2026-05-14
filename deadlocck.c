#include <stdio.h>
#include <stdbool.h>

int main(){
    int n,m,i,j,k,y;
    bool flag;
    printf("enter the number of processes:");
    scanf("%d",&n);
    printf("enter the number of resources:");
    scanf("%d",&m);
    
    int alloc[n][m],max[n][m],avail[m],need[n][m];
    printf("enter the allocation maxtrix\n");
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            scanf("%d",&alloc[i][j]);
        }
    }
    
    printf("enter the max maxtrix\n");
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            scanf("%d",&max[i][j]);
        }
    }
    
    printf("enter the available\n");
    for(i=0;i<m;i++){
        scanf("%d",&avail[i]);
    }
    
    // FIX 1: Max - Alloc
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            need[i][j]=max[i][j]-alloc[i][j];
        }
    }
    
    bool finish[n];
    int safeseq[n],ind=0;
    
    // FIX 2: Used 'k' instead of 'i'
    for(k=0;k<n;k++){
        finish[k]=false;
    }
    
    for(k=0;k<n;k++){
        for(i=0;i<n;i++){
            if(!finish[i]){
                flag=true; // FIX 3a: Removed 'bool' to use the global flag
                for(j=0;j<m;j++){
                    if(need[i][j]>avail[j]){
                        flag=false;
                        break;
                    }
                }
                
                // FIX 3b: Moved this block INSIDE the if(!finish[i]) block
                if(flag){
                    safeseq[ind++]=i;
                    for(y=0;y<m;y++){
                        avail[y]+=alloc[i][y];
                    }
                    finish[i]=true;
                }
            } 
        }
    }
    
    bool safe=true;
    for(i=0;i<n;i++){
        if(!finish[i]){
            safe=false;
            printf("deadlock detected not safe \n");
            break;
        }
    }
    
    // Minor format fix to print all processes nicely
    if(safe){
        printf("System is SAFE. Sequence: ");
        for(i=0;i<n;i++){
            printf("P%d ",safeseq[i]);
        }
        printf("\n");
    }
    
    return 0;
}