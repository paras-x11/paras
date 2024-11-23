//10. Write a program you have to make a summation of first and last Digit. (E.g., 1234 Ans: 5)

#include<stdio.h>
void main(){
    int n, f, l;

    
    printf("\nenter number: ");
    scanf("%d",&n);

    l = n % 10;

    while (n>=10)
    {
        n = n / 10;
    }

    f = n;

    printf("\nSum of first and last digit is: %d",f+l);
   
}


/*
for(; f>=10 ; n=n/10)
    {
       f = n; 
    }
*/