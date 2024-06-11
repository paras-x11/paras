//task 14:
//3. WAP using function to swap 2 numbers without using 3rd variable.

#include<stdio.h>
int a, b;

int swap(){
    
    printf("\na = ");
    scanf("%d",&a);
    printf("b = ");
    scanf("%d",&b);

    a = a + b;
    b = a - b;
    a = a - b;

    printf("\nAfter swapping:");
    printf("\n----------------------");
    printf("\na = %d",a);
    printf("\nb = %d",b);
}


void main(){
   swap();
}