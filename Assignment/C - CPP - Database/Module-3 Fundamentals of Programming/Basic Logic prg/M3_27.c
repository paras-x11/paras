//M3_27 Convert days into months.

#include<stdio.h>
void main(){
    int d, m;

    printf("Enter the days: ");
    scanf("%d",&d);

    m = d / 30;

    d = d % 30;

    printf("\n%d Months  ,   %d days",m,d);
}