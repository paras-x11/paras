// 1. Write a C program to accept two integers and check whether they are equal or not.

#include<stdio.h>

void main(){
    int a, b;

    printf("Enter first numbers: ");
    scanf("%d",&a);

    printf("Enter second numbers: ");
    scanf("%d",&b);

    if(a == b){
        printf("\nBoth numbers are same.");
    }
    else{
        printf("\nBoth numbers are not same.");
    }
}