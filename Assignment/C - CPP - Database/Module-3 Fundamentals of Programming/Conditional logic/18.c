//18. Write a C program to calculate profit and loss on a transaction. 

#include<stdio.h>
void main(){
    int buy_price, sell_price, profit, loss;

    printf("\nEnter purchase price: ");
    scanf("%d",&buy_price);
    
    printf("\nEnter selling price: ");
    scanf("%d",&sell_price);

    if (sell_price > buy_price)
    {
        profit = sell_price - buy_price;
        printf("\nProfit is: %d",profit);
    }

    else if(buy_price > sell_price)
    {
        loss = buy_price - sell_price;
        printf("\nLoss is: %d",loss);
    }
    
    else{
        printf("\nNo profit or No Loss.");
    }
    
}