//M3_3 WAP to find area and circumference of circle,

#include<stdio.h>
void main(){
    const int pi = 3.14;
    int r, area, circumference;

    printf("\nEnter the radius: ");
    scanf("%d", &r);

    area = pi*r*r;
    printf("\nArea of circle is: %d", area);

    circumference = 2*pi*r;
    printf("\ncircumference of circle is: %d", circumference);
}