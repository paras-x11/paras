//M3_19 Calculate compound interest.
/*
Formula
A = P(1 + r/n})^{nt}
A	=	final amount
P	=	initial principal balance
r	=	interest rate
n	=	number of times interest applied per time period
t	=	number of time periods elapsed
*/

#include<stdio.h>
#include<math.h>
void main(){
    int p, n, t;
    double a;
    double r;
    double p1;

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

    printf("compound interest is: %lf",a);

}