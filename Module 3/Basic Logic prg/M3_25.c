//M3_25 Accept 5 expense from user and find average of expense

#include<stdio.h>
void main(){
    int a, b, c, d, e, avg;

    printf("\nEnter the 1st expense: ");
    scanf("%d",&a);

    printf("\nEnter the 2nd expense: ");
    scanf("%d",&b);
    
    printf("\nEnter the 3rd expense: ");
    scanf("%d",&c);

    printf("\nEnter the 4th expense: ");
    scanf("%d",&d);

    printf("\nEnter the 5th expense: ");
    scanf("%d",&e);

    avg = (a+b+c+d+e)/5;
    printf("\nAverage expense is: %d",avg);
}