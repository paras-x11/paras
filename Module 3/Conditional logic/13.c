// M3_13 WAP to find minimum number among 3 numbers using ternary operator

#include <stdio.h>
void main(){
    int a, b, c, min;

    printf("Enter a: ");
    scanf("%d",&a);
    
    printf("Enter b: ");
    scanf("%d",&b);
    
    printf("Enter c: ");
    scanf("%d",&c);
    
    min = (a < b) ? ((a < c) ? a : c) : ((b < c) ? b : c);
    
    printf("\nMinimum nuber is %d",min);
}