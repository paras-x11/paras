//16. Calculate the Sum of Natural Numbers Using the While Loop 

#include<stdio.h>
void main(){
    int n, sum=0;

    printf("\nEnter the numer: ");
    scanf("%d",&n);

    for(int i=0; i<=n; i++){
        sum = sum + i;
    }
   
    printf("\nSum of natural numbers till %d is: %d",n,sum);

}