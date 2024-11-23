// Module 3: 2. WAP to make a simple calc.

#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

void main(){
    int a ,b, c, ch;
    
    printf("\n");
    printf("opration guide: \n");
    printf("-------------------\n");
    printf("press 1 for addition: \npress 2 for substraction: \npress 3 for multiplication: \npress 4 for division: ");
    printf("\npress 5 for modulo: \n");
    printf("\nPress 6 for exit: ");

    start:
    printf("\n\nEnter choice: ");
    scanf("%d",&ch);

    switch (ch)
    {
    case 1 : 
        printf("\nenter a=");
        scanf("%d",&a);

        printf("enter b=");
        scanf("%d",&b);

        c=a+b;

        printf("\n%d + %d = %d",a,b,c);
    break;

    case 2 : 
        printf("\nenter a=");
        scanf("%d",&a);

        printf("enter b=");
        scanf("%d",&b);

        c=a-b;

        printf("\n%d - %d = %d",a,b,c);
    break;

    case 3 : 
        printf("\nenter a=");
        scanf("%d",&a);

        printf("enter b=");
        scanf("%d",&b);

        c=a*b;

        printf("\n%d * %d = %d",a,b,c);
    break;

    case 4 : 
        printf("\nenter a=");
        scanf("%d",&a);

        printf("enter b=");
        scanf("%d",&b);

        c=a/b;

        printf("\n%d / %d = %d",a,b,c);
    break;

    case 5 : 
        printf("\nenter a=");
        scanf("%d",&a);

        printf("enter b=");
        scanf("%d",&b);

        c=a % b;

        printf("\n%d modulo %d = %d",a,b,c);
    break;

    case 6 :
        printf("\nExited.");
        exit(0);
    break;

    default: printf("\ninvalid operation");
    break;
    }
    goto start;
}