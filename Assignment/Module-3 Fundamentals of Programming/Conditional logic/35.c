//35. Accept the input month number and print number of days in that month. 

#include<stdio.h>
#include<stdlib.h>

void main(){
    int n;
    
    printf("\nPress 0 for Exit.");

    while(1){
        printf("\n ");
        printf("\nEnter the number of month: ");
        scanf("%d",&n);

        switch (n)
        {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                printf("\nThis month have 31 days.");
            break;

            case 2:
                printf("\nThis month have 28 or 29 days.");
            break;

            case 4:
            case 6:
            case 9:
            case 11:
                printf("\nThis month have 30 days.");
            break;

            case 0:
                printf("\nExited.");
                exit(0);
            break;
    
            default:
                printf("\ninvalid Month number.\nEnter the month between 1 and 12.");
            break;
        }
    }
}