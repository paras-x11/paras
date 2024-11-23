//3. WAP to check if the given year is a leap year or not. 

#include<stdio.h>
void main(){
    int y;

    printf("Enter the year: ");
    scanf("%d",&y);
  
    if((y % 4 == 0) && (y % 100 != 0) || (y % 400 == 0)){
        printf("\n%d is leap year.",y);
    }
    else{
            printf("\n%d is not a leap year.",y);
    }
}