//        *
//       * *
//      * * *
//     * * * *
//    * * * * *
//   * * * * * *
//  * * * * * * *
// * * * * * * * *

#include<stdio.h>
void main(){
    int r, c, s;

    for(r=1; r<=5; r++){

        for(s=5; s>r; s--){
            printf(" ");
        }

        for(c=1; c<=r; c++){
            printf("* ");
        }

    printf("\n");
    }
   
}