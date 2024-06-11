//M3_24 Accept 5 employees name and salary and count average and total salary.

#include<stdio.h>
void main(){
    int a, b, c, d, e, sum, avg;

    printf("\nEnter the 1st employee's salary: ");
    scanf("%d",&a);

    printf("\nEnter the 2nd employee's salary: ");
    scanf("%d",&b);
    
    printf("\nEnter the 3rd employee's salary: ");
    scanf("%d",&c);

    printf("\nEnter the 4th employee's salary: ");
    scanf("%d",&d);

    printf("\nEnter the 5th employee's salary: ");
    scanf("%d",&e);

    avg = (a+b+c+d+e)/5;
    printf("\nAverage salary is: %d",avg);
   
    sum = a + b + c + d + e;
    printf("\nTotal salary is: %d",sum);
}