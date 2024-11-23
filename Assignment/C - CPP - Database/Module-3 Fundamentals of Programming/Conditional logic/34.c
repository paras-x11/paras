//34. Accept month number and display month name.

#include<stdio.h>
#include<stdlib.h>

void main(){
    int ch;

    printf("\nPress 0 for Exit.");
   
    while(1){ 
        printf("\n ");
        printf("\nEnter the number of month : ");
        scanf("%d",&ch);

        switch (ch)
        {
            case 1 :
                printf("\nJanuary.");
                break;
            
            case 2 :
                printf("\nFebruary.");
                break;
            
            case 3 :
                printf("\nMarch.");
                break;

            case 4 :
                printf("\nApril.");
                break;
                
            case 5 :
                printf("\nMay.");
                break;
            
            case 6 :
                printf("\nJune.");
                break;
            
            case 7 :
                printf("\nJuly.");
                break;

            case 8 :
                printf("\nAugust.");
                break;

            case 9 :
                printf("\nSeptember.");
                break;
                
            case 10 :
                printf("\nOctober.");
                break;
            
            case 11 :
                printf("\nNovember.");
                break;
            
            case 12 :
                printf("\nDecember.");
                break;
            
            case 0 :
                printf("\nExited.");
                exit(0);

            default:
                printf("\nInvalid month number.");
                break;
        }
    }

}