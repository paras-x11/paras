// 1
// 2 3
// 4 5 6 
// 7 8 9 10
// 11 12 13 14 15

#include<stdio.h>
void main(){
    int r, c, n=1;

    for(r=0; r<=5; r++){
        for(c=0; c<=r; c++){
            
            printf(" %02d",n);
            n++;
        }
    printf("\n");
    }
   
}