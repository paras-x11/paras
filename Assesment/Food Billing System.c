// Write a program to demonstrate a Food Billing System. 
 
// • Display the Menu using appropriate codes. 
 
// • For Menu kinds of Programming , use the core logic of Loops/conditional statements. 
 
// • You need to strictly follow the syntaxes’s of that logic which you are using. 
 
// • Write the necessary comments for better understanding to you as well as to the faculty. 
 
// Adhere to the coding principles  
 
// Execution Flow of the Project: 
  
// o First, display the food items available  
 
// o Then after the user can choose any of the item displayed 
 
// o Also take the quantity of selected food item by the customer, then ask user that he/she wanna select more?  
 
// o If yes then again display the food items available and take an order from the customer. Here, you have to consider the total bill as the
//   price of food items previously selected plus the price of new items added should display as a whole bill. 
 
// o If no then display the final bill on the screen 

#include<stdio.h>
int p, b, d, i, choice;
int previous_sum, total=0;

void menu();

void main(){
    char ch;
    
    menu();

    start_b:
    while ((getchar()) != '\n'); 
    
    printf("\nDo you want to place more order (y or n): ");
    scanf("%c", &ch);

    if (ch == 'y' || ch == 'Y') {
        
        menu();
        
        goto start_b;

    } 

    else if (ch == 'n' || ch == 'N') {

        printf("\n>> Your Final Amount is: %d",total); 

    }
    else {

        printf("\nPlease Select (y or n)."); 

        goto start_b;
    }
}

void menu(){

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

            previous_sum = p*180;
            printf("\nAmount: %d",previous_sum);
            total = total + previous_sum;
            printf("\nTotal Amount= %d",total);
        break;
    
    case 2: printf("\nYou Have Selected Burger.");
            printf("\nEnter Quantity: ");
            scanf("%d",&b);

            previous_sum = b*100;
            printf("\nAmount: %d",b*100);
            total = total + previous_sum;
            printf("\nTotal Amount= %d",total);
        break;

    case 3: printf("\nYou Have Selected Dosa.");
            printf("\nEnter Quantity: ");
            scanf("%d",&d);

            previous_sum = d*120;
            printf("\nAmount: %d",d*120);
            total = total + previous_sum;
            printf("\nTotal Amount= %d",total);
        break;

    case 4: printf("\nYou Have Selected Idli.");
            printf("\nEnter Quantity: ");
            scanf("%d",&i);
            
            previous_sum = i*50;
            printf("\nAmount: %d",i*50);
            total = total + previous_sum;
            printf("\nTotal Amount= %d",total);
        break;

    default: printf("\n<< Please Enter 1 to 4 According To Menu. >>\n");
             goto start;
        break;
    }  
}