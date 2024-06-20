// task 15:
//1. WAP to find weather the number is palindrome or not using function.

#include<stdio.h>

void check(int n){
    int rem, rev=0, temp;

    temp = n;

    while(n != 0){
    rem = n % 10;
    rev = (rev * 10) + rem;
    n = n / 10;
    }

    if( rev == temp ){
        printf("\n%d is pallindrome.",temp);
    }
    else{
        printf("\n%d is Not pallindrome.",temp);
    }

}

void main(){
    int n;

    printf("\nEnter NUmber: ");
    scanf("%d",&n);

    check(n);
}