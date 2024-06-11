//task 14:
//2. WAP to find max of 3 numbers using ternary operator and function.

#include<stdio.h>

int max(int a, int b, int c){

    printf("\nEnter number 1: ");
    scanf("%d",&a);

    printf("\nEnter number 2: ");
    scanf("%d",&b);

    printf("\nEnter number 3: ");
    scanf("%d",&c);

    (a>b) ? ((a>c) ? printf("%d is max.",a) : printf("%d is max.",c)) : ((b>c) ? printf("%d is max.",b) : printf("%d is max.",c)) ;

}

void main(){
    int x,y,z;
    
    max(x,y,z);
}
