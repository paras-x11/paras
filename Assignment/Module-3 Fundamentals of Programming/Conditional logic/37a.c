// 37. WAP to show 
// a. Monday to Sunday using switch case 


#include<stdio.h>
#include<stdlib.h>

void main(){
    int week_day;

    printf("\nPress 0 for Exit.");

    while(1){ 
    printf("\n ");
    printf("\nEnter the number of week day : ");
    scanf("%d",&week_day);

    switch (week_day)
    {
    case 1 :
        printf("\nSunday.");
        break;
    
    case 2 :
        printf("\nMonday.");
        break;
    
    case 3 :
        printf("\nTuesday.");
        break;

    case 4 :
        printf("\nWednesday.");
        break;
        
    case 5 :
        printf("\nThursday.");
        break;
    
    case 6 :
        printf("\nFriday.");
        break;
    
    case 7 :
        printf("\nSaturday.");
        break;
    
    case 0 :
        printf("\nExited.");
        exit(0);

    default:
        printf("\nInvalid week number.");
        break;
    }}

}