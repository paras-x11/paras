//           * 
//         * * *
//       * * * * *
//     * * * * * * *
//   * * * * * * * * *
 

// #include<stdio.h>
// void main(){
//     int r, c, s;

//     for(r=1; r<=5; r++){

//         for(s=5; s>=r; s--){
//             printf("  ");
//         }

//         for(c=1; c<=(2*r)-1; c++){
//             printf("* ");
//         }
//     printf("\n");
//     }
   
// }




//           * 
//         * * *
//       * * * * *
//     * * * * * * *
//   * * * * * * * * *
//     * * * * * * *
//       * * * * *
//         * * *
//           *
          
#include<stdio.h>
void main(){
    int r, c, s;

    for(r=1; r<=5; r++){

        for(s=5; s>=r; s--){
            printf("  ");
        }

        for(c=1; c<=(2*r)-1; c++){
            printf("* ");
        }
    printf("\n");
    }

    for(r=4; r>=1; r--){

        for(s=5; s>=r; s--){
            printf("  ");
        }

        for(c=(r*2)-1; c>=1; c--){
            printf("* ");
        }
    printf("\n");
    }
}