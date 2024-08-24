//M3_3 WAP to find area and circumference of circle,

#include<stdio.h>
void main(){
    const float pi = 3.14;
    float r, area, circumference;

    printf("\nEnter the radius: ");
    scanf("%f", &r);

    area = pi*r*r;
    printf("\nArea of circle is: %f", area);

    circumference = 2*pi*r;
    printf("\ncircumference of circle is: %f", circumference);
}