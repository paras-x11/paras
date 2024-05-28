//M3_21 Accept 2 numbers from user and swap 2 numbers with using 3rd variable and without using 3rd variable

#include<stdio.h>
void main(){
    int a,b;

    printf("Enter first number a: ");
    scanf("%d",&a);
    
    printf("Enter second number b: ");
    scanf("%d",&b);

    printf("\na=%d    b=%d",a,b);
    printf("\n-------------------");

    a = a + b;
    b = a - b;
    a = a - b;

    printf("\nAfter swapping,");
    printf("\n-------------------");
    printf("\na=%d    b=%d",a,b);

}