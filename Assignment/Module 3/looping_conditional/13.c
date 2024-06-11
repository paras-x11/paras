// 13. calculate the Factorial of a Given Number using while loop.

#include<stdio.h>
void main(){
    int i=1, n, fact=1, temp;

    printf("Enter number: ");
    scanf("%d",&n);

    temp = n;

    while(i<=n)
    {
        fact = fact * i;
        i++;
    }

    printf("\nFactorial of %d is: %d",temp,fact);   
}