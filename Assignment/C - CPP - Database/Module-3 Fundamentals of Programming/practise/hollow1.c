//          *
//        * *
//      *   *
//    *     *
//  *       *
//    *     *
//      *   *
//        * *
//          *

#include<stdio.h>
void main(){
    int r, c, s;
    
    for(r=1; r<=5; r++){
        for(s=5; s>r; s--){
            printf("  ");
        }
        for(c=1; c<=r; c++){
            if( (r==3) && (c==2) || ((r==4) && (c==2 || c==3)) || ((r==5) && (c==2 || c==3 || c==4)) ){
                printf("  ");
            }
            else{
            printf(" *");
            }
        }

        printf("\n");
    }

    for(r=4; r>=0; r--){
        for(s=5; s>r; s--){
            printf("  ");
        }
        for(c=1; c<=r; c++){
            if( (r==3) && (c==2) || ((r==4) && (c==2 || c==3)) ){
                printf("  ");
            }
            else{
            printf(" *");
            }
        }

        printf("\n");
    }
}

