// * * * * * * *
// *   *   *   *
// * * *   *   *
// *       *   *
// * * * * *   *
// *           *
// * * * * * * *

#include<stdio.h>
void main(){
    int r,c;

    for(r=1; r<=7; r++){

        for(c=1; c<=7; c++){
            // if( (r==1 || r==7 || c==1 || c==7 ) || ((r==5) && (c==2 || c==3 || c==4 || c==5)) || ((c==5) && (r==2 || r==3 || r==4 )) || 
            //     ((r==3) && (c==2 || c==3)) || ((r==2) && (c==3)) ){
            //     printf("* ");
            // }
            // else{
            //     printf("  ");
            // }

            if( ((r==2) && (r==c || c==4 || c==6)) || ((r==3) && (c==4 || c==6)) || ((r==4) && (c==2 || c==3 || c==4 || c==6)) || 
                ((r==5) && (c==6) || ((r==6) && (c==2 || c==3 || c==4 || c==5 || c==6))) ){
                 printf("  ");
            }
            else{
                printf("* ");
            }
        }
        printf("\n");
    }
   
}


// #include <stdio.h>

// int main() {
//     int i, j;
//     int rows = 7; // Total number of rows in the pattern

//     for(i = 0; i < rows; i++) {
//         for(j = 0; j < rows; j++) {
//             // Conditions to print '*'
//             if((i==2) && (j==3) ){
//                 printf("  ");
//             }
//             else if ((i == 0) || (i == rows - 1) || 
//                 (j == 0) || (j == rows - 1) ||
//                 (i == 2 && j < rows - 2) || 
//                 (i == 4 && j < rows - 2) || 
//                 (i == 1 && j % 2 == 0 && j < rows - 1) || 
//                 (i == 3 && j == 4)) {
//                 printf("* ");
//             }
//             else {
//                 printf("  "); // Print space for other positions
//             }
//         }
//         printf("\n"); // Move to the next line after each row
//     }
//     return 0;
// }

