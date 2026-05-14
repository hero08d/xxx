#include<stdio.h>
#include<stdlib.h>
int main(){
    int n,bt[20],tat[20],wt[20];
    float avg_tat=0,avg_wt=0;
    printf("enter the no of process:");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        
        printf("enter the burst time for p%d:",i+1);
        scanf("%d",&bt[i]);
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
        printf("P%d\t%d\t%d\t%d\n",i+1, bt[i], wt[i], tat[i]);
    }
    printf("\nAverage Waiting Time = %.2f", avg_wt/n);
    printf("\nAverage Turnaround Time = %.2f", avg_tat/n);
}