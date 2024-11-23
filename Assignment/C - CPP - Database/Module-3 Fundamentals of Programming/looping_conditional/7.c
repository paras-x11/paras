// 7. WAP to print number in reverse order e.g.: number = 64728 ---> 82746

// 1234 -> 4321

#include<stdio.h>
void main(){
   
    int n,rem;
    int rev = 0;
    
    printf("\nEnter the number : ");
    scanf("%d",&n);

    while(n>0){

        rem = n % 10;
        rev = (rev*10) + rem;
        n = n / 10;

    }

    printf("\nrevrsed number is: %d",rev);
}

