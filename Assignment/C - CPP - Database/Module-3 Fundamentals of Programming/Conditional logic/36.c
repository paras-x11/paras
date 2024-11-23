/*
36. Write a C program to input electricity unit charges and calculate total 
electricity bill according to the given condition: 
For first 50 units Rs. 0.50/unit 
For next 100 units Rs. 0.75/unit 
For next 100 units Rs. 1.20/unit 
For unit above 250 Rs. 1.50/unit 
An additional surcharge of 20% is added to the bill */

#include<stdio.h>
void main(){
    float u, charge, bill_amount, surcharge;

    printf("\nEnter the unit: ");
    scanf("%f",&u);

    if(u <= 50){

        bill_amount = 0.50 * u;
        surcharge = bill_amount * 0.20;

        printf("\nelectricity bill is: %.2f",bill_amount + surcharge);
    }

    else if (u <= 150){

        bill_amount = (50 * 0.50) + ((u - 50) * 0.75);
        surcharge = bill_amount * 0.20;

        printf("\nelectricity bill is: %.2f",bill_amount + surcharge);
    }
    
    else if (u <= 250){

        bill_amount = (50 * 0.50) + (100 * 0.75) + ((u - 150) * 1.20);
        surcharge = bill_amount * 0.20;

        printf("\nelectricity bill is: %.2f",bill_amount + surcharge);
    }

    else{

        bill_amount = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((u - 250) * 1.50);
        surcharge = bill_amount * 0.20;

        printf("\nelectricity bill is: %.2f",bill_amount + surcharge);
    }
}

/*
#include<stdio.h>
void main(){
    int u, charge, bill_amount, surcharge;

    printf("\nEnter the unit: ");
    scanf("%d",&u);

    if((u > 0) && (u <= 50)){

        bill_amount = 0.50 * u;
        surcharge = bill_amount * 0.20;

        printf("\nelectricity bill is: %d",bill_amount + surcharge);
    }

    else if ((u > 50) && (u <= 150)){

        bill_amount = 0.75 * u;
        surcharge = bill_amount * 0.20;

        printf("\nelectricity bill is: %d",bill_amount + surcharge);
    }
    
    else if ((u > 150) && (u <= 250)){

        bill_amount = 1.20 * u;
        surcharge = bill_amount * 0.20;

        printf("\nelectricity bill is: %d",bill_amount + surcharge);
    }

    else{

        bill_amount = 1.50 * u;
        surcharge = bill_amount * 0.20;

        printf("\nelectricity bill is: %d",bill_amount + surcharge);
    }
}
*/