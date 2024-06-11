//A
//B C
//D E F
//G H I J
//K L M N 0

#include<stdio.h>
void main(){
    int r, c;
    char ch='A';

    for(r=0; r<=5; r++){
        for(c=0; c<=r; c++)
        {
            printf(" %c",ch);
            ch++;
        }
    printf("\n");
    }
   
}