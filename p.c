// Online C compiler to run C program online
#include <stdio.h>
#include<stdlib.h>
int main() {
    int n,bt[20],tat[20],wt[20],pr[20],p[20],i,j,temp;
    float avg_tat=0,avg_wt=0;
    printf("enter the no of process:");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        p[i]=i+1;
        printf("enter the priority burst time for p%d:",i+1);
        scanf("%d%d",&pr[i],&bt[i]);
    }
    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            if(pr[i]>pr[j]){
                temp=pr[i];pr[i]=pr[j];pr[j]=temp;
                temp=bt[i];bt[i]=bt[j];bt[j]=temp;
                temp=p[i];p[i]=p[j];p[j]=temp;
            }
        }
    }
    
    wt[0]=0;
    for(int i=1;i<n;i++){
         wt[i]=wt[i-1]+bt[i-1];
    }
    for(int i=0;i<n;i++){
        tat[i]=wt[i]+bt[i];
        avg_tat+=tat[i];
        avg_wt+=wt[i];
    }
    printf("\nProcess\tBT\tWT\tTAT\n");
    for(int i=0; i < n; i++){
        printf("P\t%d\t%d\t%d\t%d\n",p[i], bt[i], wt[i], tat[i]);
    }
    printf("\nAverage Waiting Time = %.2f", avg_wt/n);
    printf("\nAverage Turnaround Time = %.2f", avg_tat/n);
}