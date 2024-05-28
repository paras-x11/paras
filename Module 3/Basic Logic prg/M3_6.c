//M3-6 Find area of triangle formula: A= ½*b*h

#include<stdio.h>
void main(){
    float b , h, area;

    printf("\nEnter base of triangle: ");
    scanf("%f", &b);

    printf("\nEnter height of triangle: ");
    scanf("%f", &h);

    area = 0.5*b*h;

    printf("\nArea of triangle is: %f", area);
}