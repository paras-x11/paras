//M3-5 Find area of cube formula : a=6l^2

#include<stdio.h>
void main(){
    int l ,area;

    printf("\nEnter length of cube: ");
    scanf("%d", &l);

    area = 6*l*l;

    printf("\nArea of cube  is: %d", area);
}