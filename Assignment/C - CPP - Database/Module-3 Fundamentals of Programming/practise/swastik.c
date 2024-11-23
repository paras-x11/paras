// *       * * * * *
// *       *
// *       *
// *       *
// * * * * * * * * *
//         *       *
//         *       *
//         *       *
// * * * * *       *

#include<stdio.h>
void main(){
    int r, c;

    for(r=1; r<=4; r++){
        for(c=1; c<=9; c++){

            if(c==1 || c==5 || ((r==1) && (c==5 || c==6 || c==7 || c==8 ||c==9)) ){
                printf("* ");
            }
            else{ 
                printf("  ");
            }
        }
        printf("\n");
    }

    for(r=1; r<=5; r++){
        for(c=1; c<=9; c++){

            if(r==1 || c==9 || c==5 || ((r==5) && (c==1 || c==2 || c==3 || c==4 ||c==5)) ){
                printf("* ");
            }
            else{ 
                printf("  ");
            }
        }
        printf("\n");
    }
   
}