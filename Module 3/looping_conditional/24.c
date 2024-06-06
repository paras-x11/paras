// 24. 1 + 2 + 3 + 4 + 5 + ... + n 

#include<stdio.h>
void main(){
    int n, sum=0;

    printf("\nEnter the number : ");
    scanf("%d",&n);

    for(int i=0; i<=n; i++){
        sum = sum + i;
    }

    printf("\nSum is: %d",sum);
   
}