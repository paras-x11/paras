//15.Calculate sum of 10 numbers using of while loop 

#include<stdio.h>
void main(){
    int n=0, number[10], sum;

    while(n<10){

        printf("\nEnter number %d: ",n+1);
        scanf("%d",&number[n]);
        
        sum = sum + number[n];
        n++;
    }

    printf("\n%d",sum);
  
}