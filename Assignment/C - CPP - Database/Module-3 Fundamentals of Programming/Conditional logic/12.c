// M3_12 WAP to find maximum number among 3 numbers using ternary operator

#include <stdio.h>
void main(){
    int a, b, c, max;

    printf("Enter a: ");
    scanf("%d",&a);
    
    printf("Enter b: ");
    scanf("%d",&b);
    
    printf("Enter c: ");
    scanf("%d",&c);
    
    max = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
    
    printf("\nMaximum nuber is %d",max);
}
