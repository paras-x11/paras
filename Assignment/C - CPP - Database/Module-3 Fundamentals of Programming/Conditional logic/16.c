/*
16. Write a C program to read temperature in centigrade and display a suitable 
message according to the temperature state below: 
Temp < 0 then Freezing weather 
Temp 0-10 then Very Cold weather 
Temp 10-20 then Cold weather 
Temp 20-30 then Normal in Temp 
Temp 30-40 then Its Hot 
Temp >=40 then Its Very Hot */

#include<stdio.h>
void main(){
    int t;

    printf("\nEnter temprature in centigrade: ");
    scanf("%d",&t);

    if (t < 0)
    {
        printf("\nFreezing weather.");
    }

    else if ((t >= 0) && (t <= 10))
    {
        printf("\nVery Cold weather.");
    }
    
    else if ((t >= 11) && (t <= 20))
    {
        printf("\nCold weather.");
    }

    else if ((t >= 21) && (t <= 30))
    {
        printf("\nNormal in Temp.");
    }

    else if ((t >= 31) && (t <= 40))
    {
        printf("\nIts Hot.");
    }

    else{
        printf("\nIts Very Hot.");
    }
    
}