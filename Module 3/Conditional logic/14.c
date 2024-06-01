//M3_14 WAP to find the largest of 3 numbers.

#include<stdio.h>
void main(){
    int a, b, c;

    printf("Enter a: ");
    scanf("%d",&a);
    
    printf("Enter b: ");
    scanf("%d",&b);
    
    printf("Enter c: ");
    scanf("%d",&c);
    
    if ((a > b) && (a >c))
    {
        printf("%d is greatest.",a);
    }

    else if ((b > a) && (b > c))
    {
        printf("%d is greatest.",b);
    }
    
    else{
        printf("%d is greatest.",c);
    }
}