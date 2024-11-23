// 1
// 1 0
// 1 0 1
// 1 0 1 0
// 1 0 1 0 1

#include<stdio.h>
void main(){
    int r, c;

    for(r=0; r<5; r++){

        for(c=0; c<=r; c++){

            if(c % 2 == 0){
                printf("1 ");
            }
            else{
                printf("0 ");
            }
        }
    printf("\n");
    }
   
}