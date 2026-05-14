// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int n,wt[20],bt[20],rem_bt[20],tat[20];
    int i,tq,remain,time=0;
    float avg_tat=0,avg_wt=0;
    
    printf("enter number of processes:");
    scanf("%d",&n);
    remain=n;
    for(i=0;i<n;i++){
        printf("enter the burst time for processes%d:",i+1);
        scanf("%d",&bt[i]);
        rem_bt[i]=bt[i];
    }
    
    printf("enter the time quantum:");
    scanf("%d",&tq);
    for(i=0;remain!=0;){
        if(rem_bt[i]<=tq && rem_bt[i]>0){
            time+=rem_bt[i];
            rem_bt[i]=0;
            remain--;
            tat[i]+=time;
            wt[i]=tat[i]-bt[i];
        }
        else if(rem_bt[i]>0){
            rem_bt[i]-=tq;
            time+=tq;
        }
        if(i==n-1){
            i=0;
        }
        else{
            i++;
        }
    }
    printf("\nProcess\tBT\tWT\tTAT\n");
    for(int i=0; i < n; i++){
        avg_tat+=tat[i];
        avg_wt+=wt[i];
        printf("P\t%d\t%d\t%d\t%d\n",i+1, bt[i], wt[i], tat[i]);
    }
    printf("\nAverage Waiting Time = %.2f", avg_wt/n);
    printf("\nAverage Turnaround Time = %.2f", avg_tat/n);
        
}