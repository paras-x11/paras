//10. WAP to check whether a number is negative, positive or zero. 

#include<stdio.h>
void main(){
    int n;

    printf("\nEnter Number: ");
    scanf("%d",&n);

    ((n > 0) || (n < 0)) ? ((n < 0) ? printf("%d is negative.",n) : printf("%d is positive.",n)) : printf("\nYou entered zero.");

}