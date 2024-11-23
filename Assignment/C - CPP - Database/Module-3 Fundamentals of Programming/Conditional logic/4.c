//M3_4  WAP to make simple calculator (operation include Addition, Subtraction, Multiplication, Division, modulo) uusing conditional statement.

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
        printf("enter a=");
        scanf("%d",&a);

        printf("enter b=");
        scanf("%d",&b);

        c=a+b;

        printf("a + b = %d",c);
    break;

    case 2 : 
        printf("enter a=");
        scanf("%d",&a);

        printf("enter b=");
        scanf("%d",&b);

        c=a-b;

        printf("a - b = %d",c);
    break;

    case 3 : 
        printf("enter a=");
        scanf("%d",&a);

        printf("enter b=");
        scanf("%d",&b);

        c=a*b;

        printf("a * b = %d",c);
    break;

    case 4 : 
        printf("enter a=");
        scanf("%d",&a);

        printf("enter b=");
        scanf("%d",&b);

        c=a/b;

        printf("a - b = %d",c);
    break;

    case 5 : 
        printf("enter a=");
        scanf("%d",&a);

        printf("enter b=");
        scanf("%d",&b);

        c=a % b;

        printf("a modulo b = %d",c);
    break;

    case 6 :
        printf("Exited.");
        exit(0);
    break;

    default: printf("\ninvalid operation");
    break;
    }
    goto start;
}