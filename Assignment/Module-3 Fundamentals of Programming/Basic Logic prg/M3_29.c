//M3_29. Convert minutes into seconds and hours

#include<stdio.h>
void main(){
    int s, m, h;

    printf("Enter the minutes: ");
    scanf("%d",&m);
    
    s = m * 60;

    h = m / 60;

    m = m % 60;

    printf("\n%d Seconds  ,  %d Hours %d Minutes",s,h,m);
}