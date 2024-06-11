//M3_23 WAP to calculate swap 2 numbers with using of multiplication and division.

#include<stdio.h>
void main(){
    int a,b;

    printf("Enter first number a: ");
    scanf("%d",&a);
    
    printf("Enter second number b: ");
    scanf("%d",&b);

    printf("\na=%d    b=%d",a,b);
    printf("\n-------------------");

    a = a * b;
    b = a / b;
    a = a / b;

    printf("\nAfter swapping,");
    printf("\n-------------------");
    printf("\na=%d    b=%d",a,b);

}