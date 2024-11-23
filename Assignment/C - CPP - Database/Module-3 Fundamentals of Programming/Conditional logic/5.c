//M3_5 Check Number Is Positive or Negative
#include<stdio.h>

void main() {
    int n;
    
    printf("Enter number: ");
    scanf("%d",&n);
    
    if(n > 0){
        printf("\n%d is Positive Number",n);
    }
    
    else if (n < 0){
        printf("\n%d is Negative Number",n);
    }
    
    else{
        printf("\nYou entered Zero",n);
    }
}