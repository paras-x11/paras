// 23. C Program to Reverse a Number Using FOR Loop.

#include<stdio.h>
void main(){
    int num,rev=0, rem, temp;
    
    printf("\nEnter the number : ");
    scanf("%d",&num);

    for(; num>0; num /= 10){

        rem = num % 10;
        rev = (rev*10) + rem;
        
    }

    printf("\nRevers: %d",rev);
   
}