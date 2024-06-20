// task 15:
// 4. calculate sum of natural number using while loop 
// formula: ((n)*(n+1)) / 2;

#include<stdio.h>
void main(){
    int n, sum=0, i=1;

    printf("\nEnter number: ");
    scanf("%d",&n);

    while(n != 0){
        sum = sum + n;
        n--;
    }
    printf("\nSum is: %d",sum);


    // while(i != 0){                   // Define int i=1;

    // sum= ((n)*(n+1)) / 2;
    // i--;

    // }
    // printf("\nSum of %d natural numbers is: %d",n,sum);

}