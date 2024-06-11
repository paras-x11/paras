///5. WAP to print factorial of given number.

// 5 = 5*4*3*2*1 = 120

#include<stdio.h>
void main(){
    int n;
    int fact = 1;

    printf("\nEnter the number: ");
    scanf("%d",&n);

    while(n>0){

        fact = fact * n;
        n--;
    }
    printf("\nFactorial is: %d",fact);

}
