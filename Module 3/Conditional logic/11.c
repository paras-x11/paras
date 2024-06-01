// M3_11 WAP to find number is even or odd using ternary operator.

#include <stdio.h>
void main (){
    int n;
    
    printf("Enter Number: ");
    scanf("%d",&n);
    
    (n % 2 == 0) ? printf("\nEven") : printf("\nOdd");
}