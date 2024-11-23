// eeeee
//  dddd
//   ccc
//    bb
//     a

#include<stdio.h>
void main(){
    int r,c,s;
    char ch ='E';

    for(r=1; r<=5; r++){
        for(s=1; s<r; s++){
            printf("  ");
        }

        for(c=5; c>=r; c--){
            printf("%c ",ch);
        }
    ch--;
    printf("\n");
    }
   
}