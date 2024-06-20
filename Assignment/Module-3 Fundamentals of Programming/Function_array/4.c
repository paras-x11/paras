// 4. WAP to find factorial using recursion 

#include<stdio.h>

int factorial(int n){

    if(n<=1){
        return 1;
    }
    else{        
        return n*factorial(n-1);
    }
    
}

void main(){
    int n;

    printf("\nEnter number: ");
    scanf("%d",&n);
    printf("\nFactorial of %d is: %d\n",n,factorial(n));
   
}