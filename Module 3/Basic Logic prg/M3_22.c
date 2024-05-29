/*
M3_22 Calculate compound interest (Compound Interest formula:
    a. Formula to calculate compound interest annually is given by: Amount = P(1 + r/n})^{nt}
    b. Compound Interest = Amount - P
*/

#include<stdio.h>
#include<math.h>
void main(){
    int p, n, t;
    double a, r, pi, ci;

    printf("Enter the principal amount: ");
    scanf("%d",&p);

    printf("Enter the interest rate: ");
    scanf("%lf",&r);

    printf("Enter the number of times interest applied per time period n: ");
    scanf("%d",&n);

    printf("Enter the number of time periods t: ");
    scanf("%d",&t);

    r = r / 100;

    a = p * pow(1 + r / n, n * t);

    printf("\ncompound interest by formula,");
    printf("\n---------------------------------------------------------------------------");
    printf("\nAmount = P(1 + r/n})^{nt} is:\t\t->\t%lf",a);
    printf("\n---------------------------------------------------------------------------");
    printf("\n");

    ci = a - p;
    
    printf("\ncompound interest by formula,");
    printf("\n---------------------------------------------------------------------------");
    printf("\ncompound interest = Amount - P is:\t ->\t%lf",ci);
    printf("\n---------------------------------------------------------------------------");
}