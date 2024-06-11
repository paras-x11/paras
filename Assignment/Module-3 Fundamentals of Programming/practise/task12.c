//task 12:
// * - - - -
// - * - - -
// - - * - -
// - - - * -
// - - - - *

#include<stdio.h>
void main(){
    int r, c;
    for(r=1; r<=5; r++){
        for(c=1; c<=5; c++){
            
            if( (r==c) || (r==1) && (c==5) || (r==2) && (c==4) || (r==4) && (c==2) || ((r==5) && (c==1)) ){
            printf("* ");
            }
            else{
                printf("- ");
            }
        }
        printf("\n");
    }
   
}
