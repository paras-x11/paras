//M3_28 Convert years into days and months.

#include<stdio.h>
void main(){
    int d, m, y;

    printf("Enter number of years: ");
    scanf("%d",&y);

    m = y * 12;

    d = y * 365;

    printf("\n%d Months  ,  %d Days",m,d);
}