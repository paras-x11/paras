//30. If bill exceeds Rs. 800 then a surcharge of 18% will be charged and the minimum bill should be of Rs. 256/-

#include<stdio.h>
void main(){
    float bill_amount, surcharge;

    printf("\nEnter the bill amount: ");
    scanf("%f",&bill_amount);

    if ((bill_amount >= 256) && (bill_amount <= 800))
    {
        printf("\nNo surcharge will be charged.");
        printf("\nYour Bill Is: %.2f",bill_amount);
    }
    
    else if (bill_amount > 800)
    {
        surcharge = bill_amount * 0.18;
        printf("\nSurcharge: %.2f",surcharge);

        bill_amount = bill_amount + surcharge;
        printf("\nYour Bill Is: %.2f",bill_amount);
    }

    else{
        printf("\nMinimum bill should be Rs. 256/-");
    }
    
}