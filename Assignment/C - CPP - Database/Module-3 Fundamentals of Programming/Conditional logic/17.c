// 17. Write a C program to check whether a triangle can be formed with the given values for the angles. 

#include<stdio.h>
void main(){
    int a, b, c, sum;

    printf("\nIf the sum of three angles are 180 then triangle can be formed.");

    printf("\nEnter angle a: ");
    scanf("%d",&a);
    
    printf("\nEnter angle b: ");
    scanf("%d",&b);
    
    printf("\nEnter angle c: ");
    scanf("%d",&c);

    sum = a + b + c;

    if (sum == 180)
    {
        printf("\nA triangle can be formed.");
    }

    else{
        printf("\nA triangle can not be formed.");
    }
}