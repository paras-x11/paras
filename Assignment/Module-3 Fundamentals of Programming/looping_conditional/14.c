// 14. Accept 5 numbers from user and find those numbers factorials.

#include<stdio.h>
void main(){
    int i, n, number[5], fact[5];
    
    for(n=0; n<5; n++){

        printf("Enter number %d: ",n+1);
        scanf("%d",&number[n]);

    }

    for(n=0; n<5; n++){
        fact[n]=1;
        
        for(i=1; i<=number[n]; i++){
            fact[n] = fact[n] * i;
        }

        printf("\nFactorial of %d is: %d",number[n],fact[n]);  
    }
}