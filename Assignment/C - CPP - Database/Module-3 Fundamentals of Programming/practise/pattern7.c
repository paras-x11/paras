//         * 
//        * *
//       * * *
//      * * * *
//     * * * * *
//    * * * * * *
//   * * * * * * *
//  * * * * * * * *
// * * * * * * * * *

#include<stdio.h>
void main(){
    int r, c, s;
   
    for(r=0; r<=8; r++){

        for(s=8; s>r; s--){
            printf(" ");
        }

        for(c=0; c<=r; c++){
            printf("* ");
        }

    printf("\n");
    }
   
}