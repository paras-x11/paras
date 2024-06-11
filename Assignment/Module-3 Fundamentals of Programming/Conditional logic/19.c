/*
19. Write a program in C to calculate and print the electricity bill of a given 
customer. The customer ID, name, and unit consumed by the user should 
be captured from the keyboard to display the total amount to be paid to the 
customer. The charge are as follow : 
            Unit                  Charge/unit 
upto 350                            @1.20 
350 and above but less than 600     @1.50 
600 and above but less than 800     @1.80 
800 and above                       @2.00 */

#include<stdio.h>
void main(){
    int id, unit, pay_amount;
    char name[10];

    printf("Enter customer id: ");
    scanf("%d",&id);

    printf("\nEnter customer name: ");
    scanf("%c",&name);
    gets(name);

    printf("\nEnter the unit consumed by customer: ");
    scanf("%d",&unit);

    if(unit <= 350){
        pay_amount = unit * 1.20;
        printf("\nAmount to be paid: %d",pay_amount);
    }

    else if((unit >= 351) && (unit <= 600)){
        pay_amount = unit * 1.50;
        printf("\nAmount to be paid: %d",pay_amount);
    }

    else if((unit >= 601) && (unit <= 800)){
        pay_amount = unit * 1.80;
        printf("\nAmount to be paid: %d",pay_amount);
    }

    else{
        pay_amount = unit * 2.00;
        printf("\nAmount to be paid: %d",pay_amount);
    } 
}