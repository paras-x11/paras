// 10. WAP to perform Palindrome number using for loop and function 

#include<stdio.h>
int revrse(int n){
    int rev = 0, rem;

    for(; n>0; n/=10){
        rem = n % 10;
        rev = rev*10 + rem;
    }

    return rev;
}

void main(){
    int number;

    printf("\nEnter number: ");
    scanf("%d",&number);

    int temp = number;

    int rev = revrse(number);

    if(temp == rev){
        printf("\nNumber is palindrome.");
    }
    else{
        printf("\nNumber is not palindrome.");
    }
}