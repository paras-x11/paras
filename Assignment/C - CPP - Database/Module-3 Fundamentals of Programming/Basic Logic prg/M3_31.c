//M3_31 Convert kilometers into meters.

#include<stdio.h>
void main(){
    int m, km;

    printf("Enter kilo meters: ");
    scanf("%d",&km);

    m = km * 100;

    printf("\n%d Meters.",m);
}