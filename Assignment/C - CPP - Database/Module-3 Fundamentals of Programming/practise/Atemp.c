#include<stdio.h>
#include<stdlib.h>

int main(){
    int p, b, d, i, choice;
    char ch='y';

    start:
    printf("\n---------------Menu---------------\n");
    printf("\n1.Pizza           price = 180rs/pcs");
    printf("\n2.Burger          price = 100rs/pcs");
    printf("\n3.Dosa            price = 120rs/pcs");
    printf("\n4.Idli            price = 50rs/pcs\n");

    printf("\nPlease Enter Your Choice: ");
    scanf("%d", &choice);

    switch (choice)
    {
    case 1: printf("\nYou Have Selected Pizza.");
            printf("\nEnter Quantity: ");
            scanf("%d",&p);

            printf("\nAmount: %d",p*180);
        break;
    
    case 2: printf("\nYou Have Selected Burger.");
            printf("\nEnter Quantity: ");
            scanf("%d",&b);

            printf("\nAmount: %d",b*180);
        break;

    case 3: printf("\nYou Have Selected Dosa.");
            printf("\nEnter Quantity: ");
            scanf("%d",&d);

            printf("\nAmount: %d",d*180);
        break;

    case 4: printf("\nYou Have Selected Idli.");
            printf("\nEnter Quantity: ");
            scanf("%d",&i);

            printf("\nAmount: %d",i*180);
        break;

    case 0: printf("\nExited.");
            exit(0);
        break;

    default: printf("\n<< Please Enter 1 to 4 According To Menu. >>\n");
             
        break;
    }

    printf("\nDo You Want To Place More Order: y or n: ");
    scanf("%c", &ch);

    do{
        
        menu();
    
    }while(ch == 'y' || ch == 'Y');
    
    
    return 0;
}
 