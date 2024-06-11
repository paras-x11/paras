//18. Write a C Program to Print the Multiplication Table of N 

#include<stdio.h>
void main(){
    int n, i, m, res;

    printf("\nEnter which number's table you want: ");
    scanf("%d",&n);

    printf("\nEnter multiplier: ");
    scanf("%d",&m);

    for(i=1; i<=m; i++){
        
        res = n * i;

        printf("\n%d ",res);
    }
   
}