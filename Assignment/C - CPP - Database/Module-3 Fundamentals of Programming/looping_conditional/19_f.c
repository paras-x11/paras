// *
// *  *
// *  *  *
// *  *  *  *
// *  *  *  *  *
// *  *  *  *  *  *
// *  *  *  *  *
// *  *  *  *
// *  *  * 
// *  *
// *

#include<stdio.h>

void main() {
    int r, c, s;

    for(r = 0; r <= 5; r++) { 

        for(c = 0; c <=r; c++) {
            printf("* ");
        }

        printf("\n");
    }

    for(r = 0; r < 5; r++) { 
        
        for(c=5; c>r; c-- ){
            printf("* ");
        }

        printf("\n");
    }   
}