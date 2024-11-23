// 31. WAP to read any month number in integer and display the number of days for this month.

#include<stdio.h>
void main(){
    int n;
    
    printf("\nEnter the number of month: ");
    scanf("%d",&n);
    
    if((n > 0) && (n<13)){
        if((n==1) || (n==3) || (n==5) || (n==7) || (n==8) || (n==10) || (n==12)){
            printf("\nThis month have 31 days.");
        }
        else if(n==2){
            printf("\nThis month have 28 or 29 days.");
        }
        else{
            printf("\nThis month have 30 days.");
        }
    }
    else{
        printf("\ninvalid Month number.\nEnter the month between 1 and 12.");
    }
}