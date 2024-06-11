//M3_32 Accept 2 numbers and find out its sum check it size.

#include<stdio.h>
void main(){
    int a, b, sum, size;

    printf("\nEnter 1st number: ");
    scanf("%d",&a);
    printf("\nEnter 2nd number: ");
    scanf("%d",&b);

    sum = a + b;

    printf("\nThe sum is: %d",sum);

    printf("\nSize of the sum in bytes is: %d",sizeof(sum));
}