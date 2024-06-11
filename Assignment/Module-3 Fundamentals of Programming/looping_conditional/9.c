//9. Write a program make a summation of given number (E.g., 1523 Ans: 11)

#include<stdio.h>
void main(){
    int n, sum=0;

    printf("\nenter number: ");
    scanf("%d",&n);

    while (n != 0)
    {
        sum = sum + n % 10;
        n = n / 10;
    }
    
     printf("\nsum of all digit is: %d",sum);
}


/*
for(; n > 0; n=n/10){

        sum = sum + n % 10;

    }
*/