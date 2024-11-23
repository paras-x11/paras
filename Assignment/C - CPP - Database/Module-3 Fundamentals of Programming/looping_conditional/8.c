//8. Write a program to find out the max from given number (E.g., No: 1562 Max number is 6) 

#include<stdio.h>
void main(){
    int n, rem, max=0 ;

    printf("\nenter number: ");
    scanf("%d",&n);

    while(n > 0){
       
        rem = n % 10; 

        if(rem > max){
            max = rem;
        }

        n = n / 10;
    }
    printf("\nMax number is: %d",max);
}