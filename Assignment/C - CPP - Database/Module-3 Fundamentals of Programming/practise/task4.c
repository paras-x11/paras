//task4:
//*
//* *
//*   *
//*     *
//* * * * *

#include<stdio.h>
void main(){
    int r, c;

    for(r=0; r<=5; r++){
    
        for (c = 0; c<=r; c++){
        
            if(c==0||c==5||c==r||r==5){
                printf(" *");
            }
            else{
                printf("  ");
            }
        }
        printf("\n");
    }
}