//M3_30 WAP to convert years into days and days into years.

#include<stdio.h>
#include<stdlib.h>
void main(){
    int y, d, ch;

    start:

    printf("\nChoose 1 for conver years into days. \nChoose 2 for convert days into years.\n");
    printf("\nChoose 3 for exit. ");

    printf("\nEnter your choice: ");
    scanf("%d",&ch);

    if(ch == 1){
        printf("Enter year: ");
        scanf("%d",&y);

        d = y * 365;

        printf("\n%d Days",d);
        goto start;
    }

    else if (ch == 2){

        printf("\nEnter days: ");
        scanf("%d",&d);

        y = d / 365;

        printf("\n%d Years  ,  %d Days",y,d%365);
        goto start;
    }

    else if (ch == 3)
    {
        printf("Exied.");
        exit(0);
    }
    
    else
    {
        printf("\ninvalid choice.\n");
        goto start;
    }
    
}
